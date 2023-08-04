from app import app
from flask import Flask, render_template, redirect, request,session
from app.models import author_model#PUT WHATEVER THE MODELS ARE. Do not put class names; will create circular import in many to many relationships
from app.models import book_model

@app.route("/books")
def get_all_books():
    all_books=book_model.Book.get_all_books()
    return render_template("books.html", all_books=all_books)
    
@app.route('/add_book', methods=['POST'])
def add_book():
    data=request.form
    book_model.Book.insert_book(data)
    return redirect('/books')

@app.route("/one_book/<int:id>")
def find_one_book(id):
    data={
        'id': id
    }
    one_book=book_model.Book.get_one_book(data)
    all_authors=author_model.Author.get_all_authors()
    return render_template("one_book.html", one_book=one_book, all_authors=all_authors)

@app.route('/add_author_favorite', methods=["POST"])
def add_books_favorite_author():
   print("!!!!!!!", request.form)
   data={
       "author_id":request.form["author_id"],
       "book_id":request.form["book_id"]
   }
   book_model.Book.add_to_author_favorites(data)
    
   return redirect(f'/one_book/{request.form["book_id"]}')