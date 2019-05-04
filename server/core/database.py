from __init__ import db


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    category = db.Column(db.String(80), nullable=False)
    collection = db.Column(db.String(80))
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    active = db.Column(db.Boolean, nullable=False)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category,
            'collection': self.collection,
            'price': self.price,
            'stock': self.stock,
            'active': self.active
        }


class Sale(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product = db.Column(db.Integer, nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    payment = db.Column(db.Float, nullable=False)
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


def add_db_product(products):
    if type(products) is dict:
        new_product = Product()
        new_product.category = products['category']
        new_product.name = products['name']
        new_product.price = products['price']
        new_product.stock = products['stock']
        new_product.active = products['active']
        db.session.add(new_product)
    else:
        for product in products:
            new_product = Product()
            new_product.category = product['category']
            new_product.name = product['name']
            new_product.price = product['price']
            new_product.stock = product['stock']
            new_product.active = product['active']
            db.session.add(new_product)
    db.session.commit()


def delete_db_product(product_id):
    if not product_id:
        db.session.delete(get_db_products())
    else:
        db.session.delete(get_db_products(product_id))
    db.session.commit()


def update_db_product(product_id, new_product):
    product = Product.query.filter_by(id=product_id).first()
    product.category = new_product['category']
    product.collection = new_product['collection']
    product.name = new_product['name']
    product.price = new_product['price']
    product.stock = new_product['stock']
    product.active = new_product['active']
    db.session.commit()


def get_db_products(product_id=None, category=None, collection=None):
    if not product_id and not category and not collection:
        return Product.query.order_by(Product.category.asc(), Product.name.asc()).all()
    else:
        if product_id:
            return Product.query.filter_by(id=product_id).first()
        elif category:
            return Product.query.filter_by(category=category).all()
        elif collection:
            return Product.query.filter_by(collection=collection).all()


def get_db_product_categories():
    categories = list()
    for product in get_db_products():
        if product.category not in categories:
            categories.append(product.category)
    return categories


def get_db_product_collections():
    collections = list()
    for product in get_db_products():
        if product.collection and product.collection not in collections:
            collections.append(product.collection)
    return collections


def get_db_product_collection(product_id):
    product = get_db_products(product_id=product_id)
    return product.collection if product.collection else False


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


def get_db_sales(sale_id=None, product_id=None, timespan=None):
    if sale_id:
        return Sale.query.filter_by(id=sale_id).first()
    if product_id:
        return Sale.query.filter_by(product=product_id).all()
    if timespan:
        return Sale.query.filter(Sale.timestamp.between(timespan['from'], timespan['to'])).order_by(Sale.timestamp.desc())
    else:
        return Sale.query.order_by(Sale.timestamp.desc()).all()


def delete_db_sales(sale_id=None):
    if not sale_id:
        for sale in get_db_sales():
            db.session.delete(sale)
    else:
        db.session.delete(get_db_sales(sale_id))
    db.session.commit()
