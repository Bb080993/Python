
from app.config.mysqlconnection import connectToMySQL
from flask import flash



class Order:
    DB = "cookie_orders"
    def __init__(self, data):
        self.id= data['id']
        self.customer_name = data['customer_name']
        self.cookie_type = data['cookie_type']
        self.num_of_boxes = data['num_of_boxes']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    #Insert into database
    @classmethod
    def insert_order(cls, data):
        query = "INSERT INTO orders (customer_name, cookie_type, num_of_boxes) VALUES (%(customer_name)s, %(cookie_type)s, %(num_of_boxes)s);"    
        return connectToMySQL(cls.DB).query_db(query, data)
    #Get all from table in database
    @classmethod
    def get_all_orders(cls):
        query="""SELECT * FROM orders"""
        results= connectToMySQL(cls.DB).query_db(query)
        print(results)
        order_list=[]
        for order in results:
            order_list.append(cls(order))
        return order_list
    @classmethod
    def get_one_order(cls, data):
        query="""
                SELECT * FROM orders WHERE id=%(id)s;
                """
        results=connectToMySQL(cls.DB).query_db(query, data)[0]
        return results
    @classmethod
    def update_order(cls, data):
        query="""
            UPDATE orders SET customer_name=%(customer_name)s, cookie_type=%(cookie_type)s, num_of_boxes=%(num_of_boxes)s WHERE id=%(id)s;
            """
        results=connectToMySQL(cls.DB).query_db(query, data)
        return results
    @staticmethod
    def validate_form(order):
        is_valid=True
        if len(order['customer_name'])<2:
            flash("Name Required. Must be 2 or more characters.")
            is_valid=False
        if len(order["cookie_type"])<2:
            flash("Cookie Type Required. Must be 2 or more characters.")
            is_valid=False
        if len(order['num_of_boxes'])<1:
            flash("Must choose a number of boxes")
            is_valid=False
        elif int(order['num_of_boxes'])<1:
            flash("Must choose a positive number of boxes")
            is_valid=False
        return is_valid
    

 