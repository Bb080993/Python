from app.config.mysqlconnection import connectToMySQL
from app.models import author_model


class Book:
    DB = "books_schema"
    def __init__(self, data):
        self.id= data['id']
        self.title = data['title']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.been_favorited_by_author=[]
    @classmethod
    def insert_book(cls, data):
        query = "INSERT INTO books (title, num_of_pages) VALUES (%(title)s, %(num_of_pages)s);"    
        return connectToMySQL(cls.DB).query_db(query, data)
    @classmethod
    def get_all_books(cls):
        query="""SELECT * FROM books"""
        results= connectToMySQL(cls.DB).query_db(query)
        print(results)
        book_list=[]
        for book in results:
            book_list.append(cls(book))
        return book_list
    @classmethod
    def get_one_book(cls, data):
        query="""
                SELECT * FROM books
                LEFT JOIN favorites ON favorites.book_id=books.id
                LEFT JOIN authors ON authors.id=favorites.author_id
                WHERE books.id=%(id)s
            """
        results=connectToMySQL(cls.DB).query_db(query, data)
        print(results)
        one_book=cls(results[0])
        for row in results:
            print(row)
            author_data= {"id":row ["authors.id"],
                "name" :row ["name"],
                "created_at": row ["authors.created_at"],
                "updated_at" :row ["authors.updated_at"] }
            one_book.been_favorited_by_author.append(author_model.Author(author_data))
        return one_book
    @classmethod
    def add_to_author_favorites(cls, data):
        query="""
                INSERT INTO favorites (author_id, book_id)
                VALUES (%(author_id)s, %(book_id)s);
            """
        results=connectToMySQL(cls.DB).query_db(query, data)
        return results
