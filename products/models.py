#mock db
from decorators.decorators import log_call, timer, delay

mock_products = {
    "espresso": {"name": "Espresso", "price": 2.50},
    "cappuccino": {"name": "Cappuccino", "price": 3.50},
    "latte": {"name": "Latte", "price": 4.00},
    "mocha": {"name": "Mocha", "price": 4.50},
    "americano": {"name": "Americano", "price": 3.00},
    "flat_white": {"name": "Flat White", "price": 3.80},
}

@log_call
@timer
@delay(rate=1)
def get_product_by_name(product_name):
    return mock_products[product_name]

@log_call
@timer
@delay(rate=1)
def is_product_exists(product_name):
    return product_name in mock_products.keys()

@log_call
@timer
@delay(rate=1)
def add_new_product(name, cost):
    new_product = {"name": name, "cost": cost}
    mock_products[name] = new_product
    return new_product