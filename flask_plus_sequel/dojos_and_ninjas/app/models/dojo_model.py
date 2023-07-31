
from app.config.mysqlconnection import connectToMySQL
from app.models import ninja_model



class Dojo:
    DB = "dojos_and_ninjas_2_schema"
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas=[]
    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"    
        return connectToMySQL(cls.DB).query_db(query, data)
    @classmethod
    def get_all_users(cls):
        query="""SELECT * FROM dojos"""
        results= connectToMySQL(cls.DB).query_db(query)
        #print(results)
        dojo_list=[]
        for dojo in results:
            dojo_list.append(cls(dojo))
        return dojo_list
    @classmethod
    def get_one_dojo(cls, id):
        query= """SELECT * FROM dojos WHERE id=%(id)s """
        results= connectToMySQL(cls.DB).query_db(query, id)[0]
        #print(results)
        return results
    @classmethod
    def get_ninjas_from_dojo(cls, data):
        
        query="""SELECT * FROM dojos
        LEFT JOIN ninjas ON ninjas.dojo_id=dojos.id
        WHERE dojos.id=%(id)s;"""
        results=connectToMySQL(cls.DB).query_db(query, data)
       # print("Get_ninjas_from_dojo results", results)
        dojo=cls(results[0])
        #print("!!!!!!!", dojo)
        for row in results:
            ninja_data= {"id":row ["ninjas.id"],
                "first_name" :row ["first_name"],
                "last_name": row ["last_name"],
                "age": row ["age"],
                "created_at": row ["ninjas.created_at"],
                "updated_at" :row ["ninjas.updated_at"],
                "dojo_id":row ["dojo_id"] }
            dojo.ninjas.append(ninja_model.Ninja(ninja_data))
        return dojo
    @classmethod
    def delete_ninja(cls, data):
        query="""DELETE FROM ninjas WHERE id=%(id)s"""
        results=connectToMySQL(cls.DB).query_db(query, data)
        return results
    
    