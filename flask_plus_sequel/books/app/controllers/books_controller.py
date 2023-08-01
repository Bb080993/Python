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