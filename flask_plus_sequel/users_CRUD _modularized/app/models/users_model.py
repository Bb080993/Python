
from app.config.mysqlconnection import connectToMySQL


class User:
    DB = "users_schema"
    def __init__(self, data):
        self.idusers = data['idusers']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, NOW(), NOW());"    
        return connectToMySQL(cls.DB).query_db(query, data)
    @classmethod
    def get_all_users(cls):
        query="""SELECT * FROM users"""
        results= connectToMySQL(cls.DB).query_db(query)
        print(results)
        user_list=[]
        for user in results:
            user_list.append(cls(user))
        return user_list
    @classmethod
    def get_one_user(cls, id):
        query= """SELECT * FROM users WHERE idusers=%(id)s """
        results= connectToMySQL(cls.DB).query_db(query, id)[0]
        print(results)
        return results
    @classmethod
    def update_user_info(cls, data):
        query= """UPDATE users SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s 
                    WHERE idusers=%(id)s"""
        results=connectToMySQL(cls.DB).query_db(query, data)
        print(results)
        return results
    @classmethod
    def delete_user(cls, data):
        query="""DELETE FROM users WHERE idusers=%(id)s"""
        results=connectToMySQL(cls.DB).query_db(query, data)
        return results