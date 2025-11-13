# alembic/env.py (chỉ phần cần thay thế / thêm)
import os
import sys
from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context

# nếu project của bạn nằm ở thư mục cha so với alembic, thêm đường dẫn project
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# now import your models so metadata is available
# thay 'models' bằng module path thực tế nếu cần (ví dụ: app.models)
import models

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Optionally get DB URL from env var (recommended)
DATABASE_URL = os.getenv("DATABASE_URL", "mysql+pymysql://root:techzen123@localhost:3306/mydb")
config.set_main_option("sqlalchemy.url", DATABASE_URL)

# Interpret the config file for Python logging.
fileConfig(config.config_file_name)

target_metadata = models.Base.metadata

def run_migrations_offline():
    url = config.get_main_option("sqlalchemy.url")
    context.configure(url=url, target_metadata=target_metadata, literal_binds=True)
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata, compare_type=True)
        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()