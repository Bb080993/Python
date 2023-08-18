
from app.config.mysqlconnection import connectToMySQL
#THIS PAGE CONTAINS AN EXAMPLE MODEL OF OOP AND EXAMPLES OF EACH CRUD METHOD
# from flask import flash
# import re

# EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

# class User:
#     DB = "users_schema"
#     def __init__(self, data):
#         self.id= data['id']
#         self.first_name = data['first_name']
#         self.last_name = data['last_name']
#         self.email = data['email']
#         self.created_at = data['created_at']
#         self.updated_at = data['updated_at']
#         #self.anything that is a many relationship to connect to=[]
#         #self.if this is the many that needs to be equal eventually to one= None
#     #Insert into database
#     @classmethod
#     def insert_user(cls, data):
#         query = "INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s);"    
#         return connectToMySQL(cls.DB).query_db(query, data)
#     #Get all from table in database
#     @classmethod
#     def get_all_users(cls):
#         query="""SELECT * FROM users"""
#         results= connectToMySQL(cls.DB).query_db(query)
#         print(results)
#         user_list=[]
#         for user in results:
#             user_list.append(cls(user))
#         return user_list
#     #Get one from table in database
#     @classmethod
#     def get_one_user(cls, id):
#         query= """SELECT * FROM users WHERE id=%(id)s """
#         results= connectToMySQL(cls.DB).query_db(query, id)[0]
#         print(results)
#         return results
#     #Update one from table in database
#     @classmethod
#     def update_user_info(cls, data):
#         query= """UPDATE users SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s 
#                     WHERE id=%(id)s"""
#         results=connectToMySQL(cls.DB).query_db(query, data)
#         print(results)
#         return results
#     #Delete from database on specific id
#     @classmethod
#     def delete_user(cls, data):
#         query="""DELETE FROM users WHERE id=%(id)s"""
#         results=connectToMySQL(cls.DB).query_db(query, data)
#         return results

# #Find user by email for login
#     @classmethod
#     def find_user_by_email(cls, email):
#         query="""SELECT * FROM users WHERE email=%(email)s"""
#         response=connectToMySQL(cls.DB).query_db(query, email)
#         print(response)

#         if len(response)<1:
#             return False
#         return cls(response[0])
#     #Get user by id
#     @classmethod
#     def get_user_by_id(cls, id):
#         query= """SELECT * FROM users WHERE id=%(id)s """
#         results= connectToMySQL(cls.DB).query_db(query, id)[0]
#         print("!!!!!!!!!!!", results)
#         return results



#     #JOIN 2 tables. Get the one with its many
#     @classmethod
#     def get_ninjas_from_dojo(cls, data):
        
#         query="""SELECT * FROM dojos
#         LEFT JOIN ninjas ON ninjas.dojo_id=dojos.id
#         WHERE dojos.id=%(id)s;"""
#         results=connectToMySQL(cls.DB).query_db(query, data)
#        # print("Get_ninjas_from_dojo results", results)
#         dojo=cls(results[0])
#         #print("!!!!!!!", dojo)
#         for row in results:
#             ninja_data= {"id":row ["ninjas.id"],
#                 "first_name" :row ["first_name"],
#                 "last_name": row ["last_name"],
#                 "age": row ["age"],
#                 "created_at": row ["ninjas.created_at"],
#                 "updated_at" :row ["ninjas.updated_at"],
#                 "dojo_id":row ["dojo_id"] }
#             dojo.ninjas.append(ninja_model.Ninja(ninja_data))
#         return dojo
# #Get all of the many with their one
#    @classmethod
#     def get_all_recipes_with_user(cls):
#         query="""
#                 SELECT * FROM recipes
#                 LEFT JOIN users ON users.id=recipes.user_id
#             """
#         results=connectToMySQL(cls.DB).query_db(query)
#         all_recipes=[]
#         for row in results:
#             one_recipe=cls(row)
#             one_recipe_user_info={
#                 "id":row["users.id"],
#                 "first_name":row["first_name"],
#                 "last_name":row["last_name"],
#                 "email":row["email"],
#                 "password":row["password"],
#                 "created_at":row["users.created_at"],
#                 "updated_at": row["users.updated_at"]
#             }
#             user=user_model.User(one_recipe_user_info)
#             one_recipe.created_by=user
#             print(one_recipe.__dict__)
#             all_recipes.append(one_recipe)
#         print("ALL recipes with user", all_recipes)
#         return all_recipes

# #Get one from the many, with its one
    
#     @classmethod
#     def one_recipe_with_user(cls,data):
#         query="""
#                 SELECT * FROM recipes
#                 LEFT JOIN users ON users.id=recipes.user_id
#                 WHERE recipes.id=%(id)s
#             """
#         results=connectToMySQL(cls.DB).query_db(query, data)
#         one_recipe_with_user=cls(results[0])
#         for row in results:
#             one_recipe_user_info={
#                 "id":row["users.id"],
#                 "first_name":row["first_name"],
#                 "last_name":row["last_name"],
#                 "email":row["email"],
#                 "password":row["password"],
#                 "created_at":row["users.created_at"],
#                 "updated_at": row["users.updated_at"]
#             }
#             user=user_model.User(one_recipe_user_info)
#             one_recipe_with_user.created_by=user
#         print("!ONE RECIPE WITH USER!",one_recipe_with_user)
#         return one_recipe_with_user

    #Join query all with like count
    #    @classmethod
    # def get_all_recipes_with_user(cls):
    #     query="""
    #             SELECT *, (SELECT (COUNT(*)) FROM likes WHERE recipes.id=recipe_id)
    #              AS num_of_likes FROM recipes
    #             LEFT JOIN users ON users.id=recipes.user_id
    #         """
    #     results=connectToMySQL(cls.DB).query_db(query)
    #     all_recipes=[]
    #     for row in results:
    #         one_recipe=cls(row)
    #         one_recipe_user_info={
    #             "id":row["users.id"],
    #             "first_name":row["first_name"],
    #             "last_name":row["last_name"],
    #             "email":row["email"],
    #             "password":row["password"],
    #             "created_at":row["users.created_at"],
    #             "updated_at": row["users.updated_at"]
    #         }
    #         user=user_model.User(one_recipe_user_info)
    #         one_recipe.created_by=user
    #         print(one_recipe.__dict__)
    #         all_recipes.append(one_recipe)
    #     print("ALL recipes with user", all_recipes)
    #     return all_recipes
    

    #Join query many to one with like count
    # @classmethod
    # def one_recipe_with_user(cls,data):
    #     query="""
    #             SELECT *, (SELECT (COUNT(*)) fROM likes WHERE recipe_id=%(id)s) AS num_of_likes FROM recipes
    #             LEFT JOIN likes on likes.recipe_id=recipes.id
    #             LEFT JOIN users ON users.id=recipes.user_id
    #             WHERE recipes.id=%(id)s
    #         """
    #     results=connectToMySQL(cls.DB).query_db(query, data)
    #     one_recipe_with_user=cls(results[0])
    #     for row in results:
    #         one_recipe_user_info={
    #             "id":row["users.id"],
    #             "first_name":row["first_name"],
    #             "last_name":row["last_name"],
    #             "email":row["email"],
    #             "password":row["password"],
    #             "created_at":row["users.created_at"],
    #             "updated_at": row["users.updated_at"]
    #         }

    #         user=user_model.User(one_recipe_user_info)
    #         one_recipe_with_user.created_by=user
    #         one_recipe_with_user.likes2.append(row['likes.user_id'])
    #     print("LIKES 2", one_recipe_with_user.likes)
    #     return one_recipe_with_user

    #Add like
    # @classmethod
    # def like_recipe(cls, data):
    #     query= """
    #             INSERT INTO likes (user_id, recipe_id)
    #             VALUES (%(user_id)s, %(recipe_id)s)
    #             """
    #     results=connectToMySQL(cls.DB).query_db(query, data)
    #     return results
    
    #Unlike
    # @classmethod
    # def unlike_recipe(cls, data):
    #     query= """
    #             DELETE FROM likes
    #             WHERE user_id=%(user_id)s
    #             AND recipe_id=%(recipe_id)s
    #             """
    #     results=connectToMySQL(cls.DB).query_db(query, data)
    #     return results

        
    #Validation of login
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
    #     query="""SELECT * FROM users WHERE email=%(email)s"""
    #     response=connectToMySQL(DB).query_db(query, form_data)
    #     print(response)
    #     if len(response)>0:
    #         flash("User already exists", 'register')
    #         is_valid= False
    #     return is_valid

    #Validation of form

    # @staticmethod
    # def validate_new_recipe(data):
    #     is_valid=True

    #     if len(data["name"])<3:
    #         flash("Name must be at least 3 characters.",'recipe')
    #         is_valid=False
    #     if len(data["description"])<3:
    #         flash("Description must be at least 3 characters.", 'recipe')
    #         is_valid=False
    #     if len(data["instructions"])<3:
    #         flash("Instructions must be at least 3 characters.", 'recipe')
    #         is_valid=False
    #     if not data["date_cooked"]:
    #         flash("Date cooked required", 'recipe')
    #         is_valid=False
    #     if "less_than_30" not in data:
    #         flash("Does your recipe take less than 30 minutes?", 'recipe')
    #         is_valid=False
    #     return is_valid
    