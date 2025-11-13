from typing import Dict, List, Optional
import itertools

from models import Product

class ProductNotFoundError(Exception):
    pass

class ProductRepository:
    def __init__(self):
        self.id_counter = itertools.count(1)
        self.products: Dict[int, Product] = {}
        
    def create(self, name: str, price: float, description: str = "") -> Product:
        new_id = next(self.id_counter)
        product = Product(id=new_id, name=name, price=price, description=description)
        self.products[new_id] = product
        return product
    
    def get(self, product_id: int) -> Product:
        product = self.products.get(product_id)
        if product is None:
            raise ProductNotFoundError(f"Product with id {product_id} not found.")
        return product
    
    def list_all(self) -> List[Product]:
        return list(self.products.values())

    def update(self, product_id: int, name: Optional[str] = None, price: Optional[float] = None, description: Optional[str] = None) -> Product:
        product = self.get(product_id)
        if name is not None:
            product.name = name
        if price is not None:
            product.price = price
        if description is not None:
            product.description = description

        return product
    
    def delete(self, product_id: int) -> None:
        if product_id not in self.products:
            raise ProductNotFoundError(f"Product with id {product_id} not found.")
        del self.products[product_id]