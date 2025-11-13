from repository import ProductRepository
from service import ProductService
from view import ProductView
from controller import ProductController

def main():
    product_repository = ProductRepository()
    product_service = ProductService(product_repository)
    product_view = ProductView()
    product_controller = ProductController(product_view, product_service)
    product_controller.run()

if __name__ == "__main__":
    main()