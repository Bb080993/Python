from app.config.mysqlconnection import connectToMySQL
from app.models.post_model import Post


class Comment:
    DB = "coding_dojo_wall"
    def __init__(self, data):
        self.id= data['id']
        self.comment_text= data["comment_text"]
        self.post_id= data["post_id"]
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.post= None

    @classmethod
    def add_comment(cls, data):
        query=  """
                INSERT INTO comments (comment_text, post_id) VALUES (%(comment_text)s, %(post_id)s)
                """
        results=connectToMySQL(cls.DB).query_db(query, data)
        print("this is the add comment data", results)
        return results
    @classmethod
    def get_all_comments_with_post(cls):
        query=  """
                SELECT * FROM comments
                JOIN users ON comments.post_id=posts.id
                """
        results=connectToMySQL(cls.DB).query_db(query)
        all_comments=[]
        for row in results:
            one_comment=cls(row)
            one_comment_post_info= {
                "id":row["posts.id"],
                "content_text": row["content_text"],
                "created_at": row["posts.created_at"],
                "updated_at": row["posts.updated_at"]
            }
            author=Post(one_comment_post_info)
            one_comment.post=author

            all_comments.append(one_comment)
        return all_comments
    @classmethod
    def delete_one_comment(cls, data):
        query=  """
                DELETE FROM comments WHERE id=%(id)s;
                """
        results=connectToMySQL(cls.DB).query_db(query, data)
        return results
    @staticmethod
    def validate_comment(data):
        is_valid=True

        if len(data["comment_text"])<1:
            flash("Must write something before posting")
            is_valid=False
            
        return is_valid