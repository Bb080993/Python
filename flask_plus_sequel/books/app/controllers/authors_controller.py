from app import app
from flask import Flask, render_template, redirect, request,session
from app.models import book_model, author_model#PUT WHATEVER THE MODELS ARE. Do not put class names; will create circular import in many to many relationships


@app.route('/authors')          
def add_author():
    all_authors=author_model.Author.get_all_authors()

    return render_template("authors.html", all_authors=all_authors)

@app.route('/add_author', methods=['POST'])
def author_form():
    data=request.form
    author_model.Author.insert_author(data)
    return redirect("/authors")

@app.route('/author/<int:id>')
def one_author(id):
    data={
        "id":id
    }
    one_author=author_model.Author.get_one_author(data)
    all_books=book_model.Book.get_all_books()
    return render_template ("one_author.html", one_author=one_author, all_books=all_books)

@app.route('/add_book_favorite', methods=["POST"])
def add_authors_favorite_book():
   print("!!!!!!!", request.form)
   data={
       "author_id":request.form["author_id"],
       "book_id":request.form["book_id"]
   }
   author_model.Author.add_to_favorites(data)
    
   return redirect(f'/author/request.form["author_id"]')


#Example routes

# @app.route('/dojos')          
# def get_all_dojos():
#     dojos=Dojo.get_all_users()
#     #print (dojos)
#     return render_template("show_all_dojos.html", dojos=dojos )

# @app.route('/add_dojo', methods=['POST'])
# def add_dojo():
#     data=request.form
#     Dojo.save(data)
#     return redirect("/dojos")

# @app.route('/dojo/<int:id>')
# def dojo_ninjas(id):
#     data={
#         "id":id
#     }
#     one_dojo=Dojo.get_ninjas_from_dojo(data)
#     print("!!!!!!", one_dojo.id)
#     session['id']=one_dojo.id
#     print('?????', session['id'])
#     return render_template("dojo_show.html", one_dojo=one_dojo)

# @app.route('/ninja/delete/<int:id>')
# def delete_ninja(id):
#     data={
#         "id":id
#     }
#     Dojo.delete_ninja(data)
#     return redirect(f'/dojo/{session["id"]}')

