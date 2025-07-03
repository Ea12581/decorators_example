from itertools import product

from flask import Blueprint,request,jsonify
import products.models
from decorators.decorators import log_call,delay,timer
from products.models import is_product_exists, get_product, add_product

products_bp = Blueprint('products', __name__)


@products_bp.route('/products')
@log_call
@timer
@delay(rate=1)
def get_product():
    product_name = request.args.get('name')
    if not product_name:
        return jsonify({'error':'product name is required'}), 400
    if not type(product_name) == str:
        return jsonify({'error':'product name must be a string'}), 400
    if not is_product_exists(product_name):
        return jsonify({'error':'product does not exist'}), 400
    current_product = get_product(product_name)
    return jsonify({'data':current_product}), 200

@products_bp.route('/add', methods=['POST'])
@log_call
@timer
@delay(rate=2)
def add_product():
    name = request.json.get('name')
    if not name:
        return jsonify({'error':'product name is required'}), 400
    if is_product_exists(name):
        return jsonify({'error':'product already exists'}), 400
    cost = request.json.get('cost')
    if not cost:
        return jsonify({'error':'email required'}), 400
    if type(cost) != float or type(cost) != int:
        return jsonify({'error':'cost must be numeric'}), 400
    new_product = add_product(name,cost)
    if not new_product:
        return jsonify({'error':'product could not be created'}), 400
    return 200


