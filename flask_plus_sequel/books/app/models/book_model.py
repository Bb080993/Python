from app.config.mysqlconnection import connectToMySQL


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