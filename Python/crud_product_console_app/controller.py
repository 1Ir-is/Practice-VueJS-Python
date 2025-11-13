from view import ProductView
from service import ProductService
from repository import ProductRepository, ProductNotFoundError

class ProductController:
    def __init__(self, view: ProductView, service: ProductService):
        self.view = view
        self.service = service

    def run(self):
        while True:
            self.view.show_menu()
            choice = self.view.input_prompt("Select an option: ")
            if choice == "1":
                self._handle_create_product()
            elif choice == "2":
                self._handle_list()
            elif choice == "3":
                self._handle_view()
            elif choice == "4":
                self._handle_update()
            elif choice == "5":
                self._handle_delete()
            elif choice == "6":
                self.view.show_message("Exiting the application.")
                break
            else:
                self.view.show_error("Invalid choice. Please try again.")
            

    def _handle_create_product(self):
        try:
            name = self.view.input_prompt("Enter product name: ").strip()
            price_str = self.view.input_prompt("Enter product price: ").strip()
            price = float(price_str)
            description = self.view.input_prompt("Enter product description: ").strip()
            product = self.service.create_product(name=name, price=price, description=description)
            self.view.show_message(f"Product created with ID: {product.id}")
        except ValueError as ve:
            self.view.show_error(str(ve))
        except Exception as e:
            self.view.show_error(f"An unexpected error occurred: {str(e)}")
        
    def _handle_list(self):
        products = self.service.list_products()
        self.view.list_products(products)

    def _handle_view(self):
        try:
            product_id_str = self.view.input_prompt("Enter product ID: ").strip()
            product_id = int(product_id_str)
            product = self.service.get_product(product_id)
            self.view.show_product(product)
        except ValueError:
            self.view.show_error("Invalid product ID.")
        except ProductNotFoundError as pnfe:
            self.view.show_error(str(pnfe))
        except Exception as e:
            self.view.show_error(f"An unexpected error occurred: {str(e)}")

    def _handle_update(self):
        try:
            product_id = int(self.view.input_prompt("Enter product id to update: ").strip())
            p = self.service.get_product(product_id) 
            self.view.show_message(f"Current name: {p.name}")
            new_name = self.view.input_prompt("New name (leave blank to keep): ").strip()
            self.view.show_message(f"Current price: {p.price}")
            new_price_raw = self.view.input_prompt("New price (leave blank to keep): ").strip()
            new_price = None
            if new_price_raw:
                new_price = float(new_price_raw)
            self.view.show_message(f"Current description: {p.description}")
            new_desc = self.view.input_prompt("New description (leave blank to keep): ").strip()
            updated = self.service.update_product(product_id,
                                                  name=new_name if new_name else None,
                                                  price=new_price,
                                                  description=new_desc if new_desc else None)
            self.view.show_message(f"Updated product: {updated}")
        except ValueError as e:
            self.view.show_error(e)
        except ProductNotFoundError as e:
            self.view.show_error(e)

    def _handle_delete(self):
        try:
            product_id = int(self.view.input_prompt("Enter product id to delete: ").strip())
            confirm = self.view.input_prompt(f"Are you sure you want to delete product {product_id}? (y/N): ").strip().lower()
            if confirm == "y":
                self.service.delete_product(product_id)
                self.view.show_message("Deleted.")
            else:
                self.view.show_message("Cancelled.")
        except ValueError:
            self.view.show_error("Please input a valid integer id.")
        except ProductNotFoundError as e:
            self.view.show_error(e)
