from __init__ import db


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    category = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    active = db.Column(db.Boolean, nullable=False)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category,
            'price': self.price,
            'active': self.active
        }


class Sale(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product = db.Column(db.Integer, nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    payment = db.Column(db.Integer, nullable=False)
    timestamp = db.Column(db.TIMESTAMP, nullable=False)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'product': self.product,
            'amount': self.amount,
            'payment': self.payment,
            'timestamp': self.timestamp
        }


def add_db_products(products):
    if type(products) is dict:
        new_product = Product()
        new_product.category = products['category']
        new_product.name = products['name']
        new_product.price = products['price']
        new_product.active = products['active']
        db.session.add(new_product)
    else:
        for product in products:
            new_product = Product()
            new_product.category = product['category']
            new_product.name = product['name']
            new_product.price = product['price']
            new_product.active = product['active']
            db.session.add(new_product)
    db.session.commit()


def remove_db_products(products):
    if type(products) is list:
        for product in products:
            db.session.delete(product)
    else:
        db.session.delete(products)
    db.session.commit()


def update_db_products(product_id, new_product):
    product = Product.query.filter_by(id=product_id).first()
    product.category = new_product['category']
    product.name = new_product['name']
    product.price = new_product['price']
    product.active = new_product['active']
    db.session.commit()


def get_db_products(product_id=None, category=None):
    if not product_id and not category:
        return Product.query.all()
    else:
        if product_id:
            return Product.query.filter_by(id=product_id).first()
        elif category:
            return Product.query.filter_by(category=category).all()


def get_db_product_categories():
    categories = list()
    for product in get_db_products():
        if product.category not in categories:
            categories.append(product.category)
    return categories


def add_db_sales(sales):
    if type(sales) is dict:
        new_sale = Sale()
        new_sale.product = sales['product']
        new_sale.amount = sales['amount']
        new_sale.payment = sales['payment']
        new_sale.timestamp = sales['timestamp']
        db.session.add(new_sale)
    else:
        for sale in sales:
            new_sale = Sale()
            new_sale.product = sale['product']
            new_sale.amount = sale['amount']
            new_sale.payment = sale['payment']
            new_sale.timestamp = sale['timestamp']
            db.session.add(new_sale)
    db.session.commit()


def get_db_sales(product_id=None):
    if not product_id:
        return Sale.query.all()
    else:
        return Sale.query.filter_by(product=product_id).all()
