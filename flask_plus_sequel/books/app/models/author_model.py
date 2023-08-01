
from app.config.mysqlconnection import connectToMySQL
#THIS PAGE CONTAINS AN EXAMPLE MODEL OF OOP AND EXAMPLES OF EACH CRUD METHOD

class Author:
    DB = "books_schema"
    def __init__(self, data):
        self.id= data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.book_favorites=[]
        #self.anything that is a many relationship to connect to=[]
        #self.if this is the many that needs to be equal eventually to one= None
    @classmethod
    def insert_author(cls, data):
        query = "INSERT INTO authors (name) VALUES (%(name)s);"    
        return connectToMySQL(cls.DB).query_db(query, data)
    @classmethod
    def get_all_authors(cls):
        query="""SELECT * FROM authors"""
        results= connectToMySQL(cls.DB).query_db(query)
        print(results)
        author_list=[]
        for author in results:
            author_list.append(cls(author))
        return author_list


    
    #Insert into database
    # @classmethod
    # def insert_user(cls, data):
    #     query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, NOW(), NOW());"    
    #     return connectToMySQL(cls.DB).query_db(query, data)
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