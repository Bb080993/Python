
from app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    DB = "coding_dojo_wall"
    def __init__(self, data):
        self.id= data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password= data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.posts= []
        #self.anything that is a many relationship to connect to=[]
        #self.if this is the many that needs to be equal eventually to one= None
    #Insert into database
    @classmethod
    def insert_user(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"    
        return connectToMySQL(cls.DB).query_db(query, data)
    @classmethod
    def check_for_email(cls, email):
        query="""SELECT * FROM users WHERE email=%(email)s"""
        response=connectToMySQL(cls.DB).query_db(query, email)
        print("!!!!!!!!!!!", response)


        if response==False:
            return False
        return cls(response[0])
    @classmethod
    def find_user_by_email(cls, email):
        query="""SELECT * FROM users WHERE email=%(email)s"""
        response=connectToMySQL(cls.DB).query_db(query, email)
        print("!!!!!!!!!!!", response)

        if len(response)<1:
            return False
        return cls(response[0])
    @classmethod
    def get_one_user(cls, id):
        query=  """
                SELECT * FROM users WHERE id=%(id)s;
                """
        results=connectToMySQL(cls.DB).query_db(query, id)
        print("model results get one", results)
        return results[0]
    @staticmethod
    def validate_registration(data):
        is_valid=True
        if len(data['first_name'])<2:
            flash("First Name Required", "register")
            is_valid=False
        if len(data['last_name'])<2:
            flash("Last Name Required", "register")
            is_valid=False
        if len(data['email'])<1:
            flash("Email Required", "register")
            is_valid=False
        if not EMAIL_REGEX.match(data['email']):
            flash("Invalid Email", "register")
            is_valid=False
        if len(data['password'])<1:
            flash("Password Required", "register")
            is_valid=False
        if len(data['confirm_password'])<1:
            flash("Confirm password Required", "register")
            is_valid=False
        if data["password"]!=data["confirm_password"]:
            flash("Passwords do not match!", "register")
            is_valid=False
        return is_valid

        

    # #Get all from table in database
    # @classmethod
    # def get_all_users(cls):
    #     query="""SELECT * FROM users"""
    #     results= connectToMySQL(cls.DB).query_db(query)
    #     print(results)
    #     user_list=[]
    #     for user in results:
    #         user_list.append(cls(user))
    #     return user_list
    # #Get one from table in database
    # @classmethod
    # def get_one_user(cls, id):
    #     query= """SELECT * FROM users WHERE id=%(id)s """
    #     results= connectToMySQL(cls.DB).query_db(query, id)[0]
    #     print(results)
    #     return results
    # #Update one from table in database
    # @classmethod
    # def update_user_info(cls, data):
    #     query= """UPDATE users SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s 
    #                 WHERE id=%(id)s"""
    #     results=connectToMySQL(cls.DB).query_db(query, data)
    #     print(results)
    #     return results
    # #Delete from database on specific id
    # @classmethod
    # def delete_user(cls, data):
    #     query="""DELETE FROM users WHERE id=%(id)s"""
    #     results=connectToMySQL(cls.DB).query_db(query, data)
    #     return results
    # #JOIN 2 tables
    # @classmethod
    # def get_ninjas_from_dojo(cls, data):
        
    #     query="""SELECT * FROM dojos
    #     LEFT JOIN ninjas ON ninjas.dojo_id=dojos.id
    #     WHERE dojos.id=%(id)s;"""
    #     results=connectToMySQL(cls.DB).query_db(query, data)
    #    # print("Get_ninjas_from_dojo results", results)
    #     dojo=cls(results[0])
    #     #print("!!!!!!!", dojo)
    #     for row in results:
    #         ninja_data= {"id":row ["ninjas.id"],
    #             "first_name" :row ["first_name"],
    #             "last_name": row ["last_name"],
    #             "age": row ["age"],
    #             "created_at": row ["ninjas.created_at"],
    #             "updated_at" :row ["ninjas.updated_at"],
    #             "dojo_id":row ["dojo_id"] }
    #         dojo.ninjas.append(ninja_model.Ninja(ninja_data))
    #     return dojo
    #Validation
    # @staticmethod
    # def validate_user(user):
        
    #     is_valid=True
    #     if len(user['first_name'])<1:
    #         flash("First Name Required")
    #         is_valid=False
    #     if len(user['last_name'])<1:
    #         flash("Last Name Required")
    #         is_valid=False
    #     if len(user['email'])<1:
    #         flash("Email Required")
    #         is_valid=False
    #     if not EMAIL_REGEX.match(user['email']):
    #         flash("Invalid Email")
    #         is_valid=False
    #     return is_valid