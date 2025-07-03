#mock db
mock_products = {
    "espresso": {"name": "Espresso", "price": 2.50},
    "cappuccino": {"name": "Cappuccino", "price": 3.50},
    "latte": {"name": "Latte", "price": 4.00},
    "mocha": {"name": "Mocha", "price": 4.50},
    "americano": {"name": "Americano", "price": 3.00},
    "flat_white": {"name": "Flat White", "price": 3.80},
}


def get_product(product_name):
    return mock_products[product_name]

def is_product_exists(product_name):
    return product_name in mock_products.keys()

def add_product(name, cost):
    new_product = {"name": name, "cost": cost}
    mock_products[name] = new_product
    return new_product