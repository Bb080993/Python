from app import app
from flask import Flask, render_template, redirect, request, session, flash
from app.models import order_model


@app.route('/cookies')          
def all_orders():
    all_orders=order_model.Order.get_all_orders()
    return render_template("cookie_orders.html", all_orders=all_orders)

@app.route('/cookies/new')
def new_order():
    return render_template("new_order.html")

@app.route('/add/order', methods=['POST'])
def add_order():
    if not order_model.Order.validate_form(request.form):
        return redirect('/cookies/new')
    data={
        "customer_name":request.form["customer_name"],
        "cookie_type":request.form["cookie_type"],
        "num_of_boxes":request.form["num_of_boxes"]
    }
    order_model.Order.insert_order(data)
    return redirect ('/cookies')

@app.route('/edit/<int:id>')
def order_page(id):
    data={
        'id':id
    }
    order=order_model.Order.get_one_order(data)
    return render_template ("edit_order.html", order=order)

@app.route('/edit/order', methods=["POST"])
def edit_order():
    if not order_model.Order.validate_form(request.form):
        return redirect(f'/edit/{request.form["id"]}')
    data={
        "id":request.form['id'],
        "customer_name":request.form["customer_name"],
        "cookie_type":request.form["cookie_type"],
        "num_of_boxes":request.form["num_of_boxes"]
    }
    order_model.Order.update_order(data)
    return redirect('/cookies')


