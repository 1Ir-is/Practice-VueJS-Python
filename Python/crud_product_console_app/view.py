from typing import List
from models import Product

class ProductView:

    @staticmethod
    def show_menu():
        print("=== Product Management ===")
        print("1. Create Product")
        print("2. List Products")
        print("3. Get Product by ID")
        print("4. Update Product")
        print("5. Delete Product")
        print("6. Exit")

    @staticmethod
    def input_prompt(prompt: str) -> str:
        return input(prompt)
    
    @staticmethod
    def show_error(message: str):
        print("Error: " + message)

    @staticmethod
    def show_message(message: str):
        print(message)

    @staticmethod
    def list_products(products: List[Product]):
        if not products:
            print("No products available.")
            return
        print("=== Product List ===")
        for product in products:
            print(f"ID: {product.id}, Name: {product.name}, Price: {product.price}, Description: {product.description}")

    @staticmethod
    def show_product(product: Product):
        print("=== Product Details ===")
        print(f"ID: {product.id}")
        print(f"Name: {product.name}")
        print(f"Price: {product.price}")
        print(f"Description: {product.description}")