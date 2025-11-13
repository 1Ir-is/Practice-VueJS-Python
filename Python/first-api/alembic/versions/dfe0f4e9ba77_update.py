"""update

Revision ID: dfe0f4e9ba77
Revises: 
Create Date: 2025-11-13 00:00:00.000000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dfe0f4e9ba77'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # 1) Thêm column owner_id tạm thời cho phép NULL để tránh lỗi khi có dữ liệu cũ
    op.add_column('products', sa.Column('owner_id', sa.Integer(), nullable=True))

    # 2) Tạo user mặc định nếu chưa có user nào (để gán owner cho products cũ).
    #    Thay email/hashed_password theo ý bạn; hashed_password có thể là placeholder.
    #    Nếu bạn đã có users trong DB, phần INSERT sẽ không chạy nếu users tồn tại.
    op.execute("""
    INSERT INTO users (email, hashed_password, is_active)
    SELECT 'admin-local@example.com', 'changeme-hash', 1
    WHERE NOT EXISTS (SELECT 1 FROM users LIMIT 1);
    """)

    # 3) Gán owner_id cho tất cả products hiện có: gán bằng id của 1 user tồn tại (lấy user đầu tiên)
    #    Cách này an toàn nếu bạn muốn sản phẩm hiện có thuộc về user đầu tiên (thường admin vừa tạo).
    op.execute("""
    UPDATE products
    SET owner_id = (SELECT id FROM users LIMIT 1)
    WHERE owner_id IS NULL;
    """)

    # 4) Nếu bạn muốn owner_id bắt buộc (NOT NULL), chuyển sang NOT NULL
    op.alter_column('products', 'owner_id', nullable=False)

    # 5) Tạo foreign key bây giờ (sẽ không fail vì đã gán owner_id hợp lệ)
    op.create_foreign_key('fk_products_owner', 'products', 'users', ['owner_id'], ['id'])


def downgrade():
    # Hủy foreign key rồi drop column
    op.drop_constraint('fk_products_owner', 'products', type_='foreignkey')
    op.drop_column('products', 'owner_id')