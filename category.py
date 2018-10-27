from flask import Blueprint, jsonify
from database import get_db_product_categories

category_blueprint = Blueprint('category', __name__, url_prefix='/kiosk/api/v1.0/categories')


@category_blueprint.route('', methods=['GET'])
def get_categories():
    return jsonify([category for category in get_db_product_categories()])
