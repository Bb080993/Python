
from flask_app.controllers.mysqlconnection import connectToMySQL
class Friend:
    DB= "first_flask"
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['fname']
        self.last_name = data['lname']
        self.occupation = data['occ']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM friends;"
        results = connectToMySQL('first_flask').query_db(query)
        friends = []
        for friend in results:
            friends.append(cls(friend))
        return friends

    @classmethod
    def save(cls, data):
        query = "INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES (%(fname)s, %(lname)s, %(occ)s, NOW(), NOW());"
        return connectToMySQL(cls.DB).query_db(query, data)
"""    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM friends;"
        results = connectToMySQL(cls.DB).query_db(query)
        friends = []
        for friend in results:
            friends.append(cls(friend))
        return friends"""
    
"""    # the get_one method will be used when we need to retrieve just one specific row of the table
    @classmethod
    def get_one(cls, friend_id):
        query  = "SELECT * FROM friends WHERE id = %(id)s";
        data = {'id': friend_id}
        results = connectToMySQL(cls.DB).query_db(query, data)
        return cls(results[0])"""
            
