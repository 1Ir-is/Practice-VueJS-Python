from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from typing import List
from datetime import timedelta

import models, schemas, crud

from database import SessionLocal, engine
from config import HOST, PORT
from auth import create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES, get_current_user, get_db

models.Base = models.__dict__.get('Product').__class__.__mro__ 

from database import Base
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Product CRUD API", version="1.0")

#CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#Routes

@app.post("/products", response_model=schemas.ProductOut, status_code=status.HTTP_201_CREATED)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    return crud.create_product(db, product, owner_id=current_user.id)

@app.get("/products", response_model=List[schemas.ProductOut])
def read_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    return crud.get_products(db, owner_id=current_user.id, skip=skip, limit=limit)


@app.get("/products/{product_id}", response_model=schemas.ProductOut)
def read_product(product_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    db_product = crud.get_product(db, product_id)
    if db_product is None or db_product.owner_id != current_user.id:
        raise HTTPException(status_code=404, detail="Product not found!")
    return db_product

@app.put("/products/{product_id}", response_model=schemas.ProductOut)
def update_product(product_id : int, product: schemas.ProductUpdate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    db_product = crud.update_product(db, product_id, product)
    if db_product is None or db_product.owner_id != current_user.id:
        raise HTTPException(status_code=404, detail="Product not found!")
    
    return db_product


@app.delete("/products/{product_id}", response_model=schemas.ProductOut)
def delete_product(product_id : int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    db_product = crud.delete_product(db, product_id)
    if db_product is None or db_product.owner_id != current_user.id:
        raise HTTPException(status_code=404, detail="Product not found!")
    return db_product


@app.post("/auth/register", response_model=schemas.UserOut, status_code=status.HTTP_201_CREATED)
def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    user = crud.create_user(db, user)
    return user

@app.post("/auth/token", response_model=schemas.Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = crud.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}