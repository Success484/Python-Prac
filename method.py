# product.py
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

# cart.py
class Cart:
    def __init__(self):
        self.items = []

    def add_product(self, product):
        self.items.append(product)

    def remove_product(self, product_name):
        self.items = [item for item in self.items if item.name != product_name]

    def view_cart(self):
        for item in self.items:
            print(f'{item.name}: ${item.price}')

    def calculate_total(self):
        return sum(item.price for item in self.items)

# main.py
# from product import Product
# from cart import Cart

def main():
    cart = Cart()
    products = []

    while True:
        print("\n1. Add Product\n2. Update Product\n3. Delete Product\n4. View Products\n5. Add to Cart\n6. View Cart\n7. Calculate Total\n8. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            products.append(Product(name, price))
        elif choice == '2':
            # Implement update functionality
            pass
        elif choice == '3':
            name = input("Enter product name to delete: ")
            products = [p for p in products if p.name != name]
        elif choice == '4':
            for product in products:
                print(f'{product.name}: ${product.price}')
        elif choice == '5':
            name = input("Enter product name to add to cart: ")
            for product in products:
                if product.name == name:
                    cart.add_product(product)
                    break
        elif choice == '6':
            cart.view_cart()
        elif choice == '7':
            total = cart.calculate_total()
            print(f'Total: ${total}')
        elif choice == '8':
            break

if __name__ == "__main__":
    main()
