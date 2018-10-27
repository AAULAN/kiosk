from flask import Blueprint, jsonify
from __init__ import make_public_category

category_blueprint = Blueprint('category', __name__, url_prefix='/kiosk/api/v1.0/categories')


@category_blueprint.route('', methods=['GET'])
def get_categories():
    return jsonify({'categories': [make_public_category(category) for category in list_categories()]})
