from flask_intro import app
from flask_intro import db
from flask import render_template, redirect, request

@app.route('/products')
def list_products():
    query_string = """
        select * from products
    """
    products = db.query(query_string)
    return render_template('list_products.html', products=products)

@app.route('/products', methods=['POST'])
def create_product():
    name = request.form['name']
    price = request.form['price']
    query_string = f"""
        INSERT INTO products (
            name, price
        ) VALUES (
            "{name}", {price}
        )
    """
    db.query(query_string)
    return redirect('/products')

@app.route('/products/new')
def new_product():
    return render_template('new_product.html')
