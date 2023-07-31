from app.config.mysqlconnection import connectToMySQL


class Ninja:
    DB = "dojos_and_ninjas_2_schema"
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id=data['dojo_id']
        self.dojo=None
    @classmethod
    def add_ninja(cls, data):
        query="""INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s)"""
        results=connectToMySQL(cls.DB).query_db(query, data)
        return results
    # @classmethod
    # def get_ninja_w_dojo(cls, data):
           
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