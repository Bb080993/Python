from app import app
from flask import Flask, render_template, redirect, request, session, flash
from app.models import #PUT WHATEVER THE MODELS ARE. Do not put class names; will create circular import in many to many relationships
from flask_bcrypt import Bcrypt
bcrypt=Bcrypt(app)



@app.route('/')          
def user_form():
    return render_template("index.html")

#Example routes

# @app.route('/dojos')          
# def get_all_dojos():
#     dojos=Dojo.get_all_users()
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
#     session['id']=one_dojo.id
#     return render_template("dojo_show.html", one_dojo=one_dojo)

# @app.route('/ninja/delete/<int:id>')
# def delete_ninja(id):
#     data={
#         "id":id
#     }
#     Dojo.delete_ninja(data)
#     return redirect(f'/dojo/{session["id"]}')
#
#validation route
# @app.route('/creating_user', methods=['POST'])
# def create_form():
#     data={
#         "first_name":request.form["first_name"],
#         "last_name":request.form["last_name"],
#         "email":request.form["email"]
#     }
#     if not User.validate_user(data):
#         return redirect('/')
#     new_user=User.save(data)
#     return redirect(f"/one_user/{new_user}") 

# @app.route("/like/<int:id>")
# def add_like(id):
#     data={
#         "user_id": session["user_id"],
#         "recipe_id": id
#     }
   
#     User.like_recipe(data)
#     return redirect(f"/view/recipe/{data['recipe_id']}")

# @app.route("/unlike/<int:id>")
# def delete_like(id):
#     data={
#         "user_id": session["user_id"],
#         "recipe_id": id
#     }
#     User.unlike_recipe(data)

#     return redirect(f"/view/recipe/{data['recipe_id']}")


