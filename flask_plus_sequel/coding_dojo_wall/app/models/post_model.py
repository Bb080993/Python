from app.config.mysqlconnection import connectToMySQL
from flask import flash
from app.models import user_model



class Post:
    DB = "coding_dojo_wall"
    def __init__(self, data):
        self.id= data['id']
        self.content_text= data["content_text"]
        self.user_id= data["user_id"]
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user= None

    @classmethod
    def add_post(cls, data):
        query=  """
                INSERT INTO posts (content_text, user_id) VALUES (%(content_text)s, %(user_id)s)
                """
        results=connectToMySQL(cls.DB).query_db(query, data)
        return results
    @classmethod
    def get_all_posts_with_user(cls):
        query=  """
                SELECT * FROM posts
                JOIN users ON posts.user_id=users.id
                """
        results=connectToMySQL(cls.DB).query_db(query)
        all_posts=[]
        for row in results:
            one_post=cls(row)
            one_posts_user_info= {
                "id":row["users.id"],
                "first_name": row["first_name"],
                "last_name": row["last_name"],
                "email": row["email"],
                "password": row["password"],
                "created_at": row["users.created_at"],
                "updated_at": row["users.updated_at"]
            }
            author=user_model.User(one_posts_user_info)
            one_post.user=author

            all_posts.append(one_post)
        return all_posts
    @classmethod
    def delete_one_post(cls, data):
        query=  """
                DELETE FROM posts WHERE id=%(id)s;
                """
        results=connectToMySQL(cls.DB).query_db(query, data)
        return results
    @staticmethod
    def validate_post(data):
        is_valid=True

        if len(data["content_text"])<1:
            flash("Must write something before posting")
            is_valid=False
            
        return is_valid
    