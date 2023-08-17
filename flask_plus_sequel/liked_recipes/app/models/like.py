from app.config.mysqlconnection import connectToMySQL
from flask import flash

class Like:
    DB = "liked_recipes"
    def __init__(self, data):
        self.id= data['id']
        self.user_id= data['user_id']
        self.recipe_id=data['recipe_id']