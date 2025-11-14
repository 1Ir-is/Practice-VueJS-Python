# sửa create_order, delete_book return type, và một số cải tiến
from sqlalchemy.orm import Session
import models, schemas
from typing import List, Optional
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def get_user_by_email(db: Session, email: str) -> Optional[models.User]:
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user: schemas.UserCreate, is_admin: bool = False) -> models.User:
    hashed_pw = get_password_hash(user.password)
    db_user = models.User(
        email=user.email,
        hashed_password=hashed_pw,
        first_name=user.first_name,
        last_name=user.last_name,
        is_admin=is_admin
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def authenticate_user(db: Session, email: str, password: str) -> Optional[models.User]:
    user = get_user_by_email(db, email)
    if not user or not verify_password(password, user.hashed_password):
        return None
    return user

def create_book(db: Session, book: schemas.BookCreate, owner_id: int, image_url: Optional[str] = None) -> models.Book:
    db_book = models.Book(**book.dict(), owner_id=owner_id, image_url=image_url)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def get_books(db: Session, skip: int = 0, limit: int = 100) -> List[models.Book]:
    return db.query(models.Book).offset(skip).limit(limit).all()

def get_book(db: Session, book_id: int) -> Optional[models.Book]:
    return db.query(models.Book).filter(models.Book.id == book_id).first()

def update_book(db: Session, book_id: int, data: dict) -> Optional[models.Book]:
    book = get_book(db, book_id)
    if not book:
        return None
    for key, value in data.items():
        setattr(book, key, value)
    db.add(book)
    db.commit()
    db.refresh(book)
    return book

def delete_book(db: Session, book_id: int) -> Optional[models.Book]:
    book = get_book(db, book_id)
    if not book:
        return None
    db.delete(book)
    db.commit()
    return book

def create_order(db: Session, user_id: int, order_in: schemas.OrderCreate):
    db_order = models.Order(user_id=user_id, status="pending", total=0.0)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)

    total = 0.0
    items = []

    for item in order_in.items:
        book = get_book(db, item.book_id)
        if not book:
            raise ValueError(f"Book with id {item.book_id} not found")
        if book.stock < item.quantity:
            raise ValueError(f"Not enough stock for book id {item.book_id}")
        
        unit_price = float(book.price)
        order_item = models.OrderItem(
            order_id=db_order.id,        # <-- SỬA: đúng trường là order_id
            book_id=item.book_id,
            quantity=item.quantity,
            unit_price=unit_price
        )

        db.add(order_item)
        book.stock -= item.quantity
        total += unit_price * item.quantity
        items.append(order_item)

    db.commit()
    db.refresh(db_order)
    db_order.total = total
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order