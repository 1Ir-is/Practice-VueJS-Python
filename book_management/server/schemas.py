from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List
from datetime import datetime

# --- Users ---
class UserBase(BaseModel):
    email: EmailStr
    first_name: Optional[str] = None
    last_name: Optional[str] = None

class UserCreate(UserBase):
    password: str = Field(..., min_length=6)

class UserOut(UserBase):
    id: int
    is_active: bool
    is_admin: bool

    # Pydantic v2: use model_config to enable from_attributes (previously orm_mode)
    model_config = {"from_attributes": True}

# --- Auth token ---
class Token(BaseModel):
    access_token: str
    token_type: str

# --- Books ---
class BookBase(BaseModel):
    title: str
    author: Optional[str] = None
    description: Optional[str] = None
    price: float
    stock: int = 0

class BookCreate(BookBase):
    pass

class BookUpdate(BaseModel):
    title: Optional[str]
    author: Optional[str]
    description: Optional[str]
    price: Optional[float]
    stock: Optional[int]

class BookOut(BookBase):
    id: int
    image_url: Optional[str]
    owner_id: int
    created_at: Optional[datetime]

    model_config = {"from_attributes": True}

# --- Orders ---
class OrderItemCreate(BaseModel):
    book_id: int
    quantity: int

class OrderCreate(BaseModel):
    items: List[OrderItemCreate]

class OrderItemOut(BaseModel):
    id: int
    book_id: int
    quantity: int
    unit_price: float

    model_config = {"from_attributes": True}

class OrderOut(BaseModel):
    id: int
    total: float
    status: str
    items: List[OrderItemOut]

    model_config = {"from_attributes": True}