# Chỉ phần liên quan (thay thế đoạn endpoints upload/auth/order nếu cần)
from fastapi import FastAPI, Depends, UploadFile, File, Form, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from typing import List
from datetime import timedelta

import models, schemas, crud
from database import SessionLocal, engine, Base
from config import HOST, PORT, ADMIN_EMAIL, ADMIN_PASSWORD
from auth import create_access_token, get_current_user, require_admin, get_db, ACCESS_TOKEN_EXPIRE_MINUTES
from cloudinary_utils import upload_file_to_cloudinary  # ensure this file exists

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Book Management API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def create_admin_user():
    db = SessionLocal()
    try:
        admin = crud.get_user_by_email(db, ADMIN_EMAIL)  # ok: positional db, email
        if not admin:
            from schemas import UserCreate
            admin_user = UserCreate(
                email=ADMIN_EMAIL,
                password=ADMIN_PASSWORD,
                first_name="Admin",
                last_name="User"
            )
            crud.create_user(db, admin_user, is_admin=True)
            print("Admin user created.")
        else:
            print("Admin user already exists.")
    finally:
        db.close()


def get_db_dependency():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/auth/register", response_model=schemas.UserOut)
def register_user(user: schemas.UserCreate, db: Session = Depends(get_db_dependency)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered!")
    return crud.create_user(db, user)

@app.post("/auth/token", response_model=schemas.Token)
def login_for_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db_dependency)):
    user = crud.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expire = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expire
    )
    return {"access_token": access_token, "token_type": "bearer"}


@app.post("/upload-image")
async def upload_image(file: UploadFile = File(...), current_user = Depends(require_admin)):
    try:
        content = await file.read()
        await file.close()
        url = upload_file_to_cloudinary(content)
        if not url:
            raise Exception("Upload returned no URL")
        return {"image_url": url}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Image upload failed: {e}")
    

@app.post("/books", response_model=schemas.BookOut, status_code=status.HTTP_201_CREATED)
async def create_book(
    title: str = Form(...),
    author: str | None = Form(None),
    description: str | None = Form(None),
    price: float = Form(...),
    stock: int = Form(0),
    image: UploadFile | None = File(None),
    db: Session = Depends(get_db_dependency),
    current_user = Depends(require_admin)
):
    try:
        image_url = None
        if image is not None:
            content = await image.read()
            await image.close()
            image_url = upload_file_to_cloudinary(content)
            if not image_url:
                raise Exception("Upload returned no URL")
        book_in = schemas.BookCreate(
            title=title,
            author=author,
            description=description,
            price=price,
            stock=stock
        )
        db_book = crud.create_book(db, book_in, owner_id=current_user.id, image_url=image_url)
        return db_book
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@app.get("/books", response_model=List[schemas.BookOut])
def list_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_db_dependency)):
    books = crud.get_books(db, skip=skip, limit=limit)
    return books

@app.get("/book/{book_id}", response_model=schemas.BookOut)
def get_book_by_id(book_id: int, db: Session = Depends(get_db_dependency)):
    book = crud.get_book(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@app.put("/books/{book_id}", response_model=schemas.BookOut)
def update_book(book_id: int, book_update: schemas.BookUpdate, db: Session = Depends(get_db_dependency), current_user = Depends(require_admin)):
    db_book = crud.update_book(db, book_id, book_update.dict(exclude_unset=True))
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book


@app.delete("/books/{book_id}", response_model=schemas.BookOut)
def delete_book(book_id: int, db: Session = Depends(get_db_dependency), current_user = Depends(require_admin)):
    db_book = crud.delete_book(db, book_id)
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book


@app.post("/orders", response_model=schemas.OrderOut)
def create_order(order_in: schemas.OrderCreate, db: Session = Depends(get_db_dependency), current_user = Depends(get_current_user)):
    try:
        order = crud.create_order(db, user_id=current_user.id, order_in=order_in)
        return order
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/orders", response_model=List[schemas.OrderOut])
def list_orders(db: Session = Depends(get_db_dependency), current_user = Depends(get_current_user)):
    orders = crud.get_orders_by_user(db, user_id=current_user.id)
    return orders

