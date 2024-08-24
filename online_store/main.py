'''
This is the main program to run
'''

from store.product import Product
from store.user_manager import UserManager
from store.payment import Payment

def main():
    # Initiliaze the bi boss
    user_manager = UserManager()

    # Register a new customer
    customer = user_manager.register_user(1,"Alice","alice@example.com","passwordSecure", "Customer")

    # register a new admin
    admin = user_manager.register_user(2,"boss baby","bossbaby@example.com","cookies","Admin")

    # authenticate the users
    try:
        logged_in_customer = user_manager.authenticate_user("alice@example.com", "passwordSecure")
        print(f"Logged in as {logged_in_customer.display_user_info()}")
    except ValueError as e:
        print(e)
    try:
        logged_in_admin = user_manager.authenticate_user("bossbaby@example.com", "cookies")
        print(f"Logged in as {logged_in_admin.display_user_info()}")
    except ValueError as e:
        print(e)


    # Customer interacts with the store
    product1 = Product(1,"Laptop","A High-perfomance laptop", 999.99, 10)
    product2 = Product(2,"Robuxs","A super elite currency", 1_000_000, 1)

    admin.add_product(product1)
    admin.add_product(product2)

    customer.add_to_cart(product1,1)
    customer.add_to_cart(product2,1)
    print(customer.view_cart())

    # Checkout and create an order
    order = customer.checkout()
    print(order.display_order_info())

    # process payment
    payment = Payment(1,order,order.total_price,"Credit Card")
    payment.process_payment()
    print(payment.display_payment_info())

    # Admin views all orders
    orders = [order]

    print(admin.view_order(orders))

if __name__ == "__main__":
    main()