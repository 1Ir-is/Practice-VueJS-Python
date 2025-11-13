from typing import List, Optional

from repository import ProductRepository, ProductNotFoundError
from models import Product

class ProductService:
    def __init__(self, product_repository: ProductRepository):
        self.product_repository = product_repository

    def create_product(self, name: str, price: float, description: str = "") -> Product:
        if not name or not name.strip():
            raise ValueError("Product name cannot be empty.")
        if price < 0:
            raise ValueError("Product price cannot be negative.")
        return self.product_repository.create(name=name.strip(), price=price, description=description.strip())
    
    def list_products(self) -> List[Product]:
        return self.product_repository.list_all()
    
    def get_product(self, product_id: int) -> Product:
        return self.product_repository.get(product_id)
    
    def update_product(self, product_id: int, name: Optional[str] = None, price: Optional[float] = None, description: Optional[str] = None) -> Product:
        if name is not None and not name.strip():
            raise ValueError("Product name cannot be empty.")
        if price is not None and price < 0:
            raise ValueError("Product price cannot be negative.")
        return self.product_repository.update(product_id, name=name.strip() if name is not None else None, price=price, description=description.strip() if description is not None else None)
    
    def delete_product(self, product_id: int) ->  None:
        self.product_repository.delete(product_id)
        