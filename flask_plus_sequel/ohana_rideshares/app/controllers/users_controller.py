from app import app
from flask import Flask, render_template, redirect, request, session, flash
from app.models.user_model import User
from app.models.ride_model import Ride
from flask_bcrypt import Bcrypt
bcrypt=Bcrypt(app)



@app.route('/')          
def user_form():
    return render_template("login_registration.html")

@app.route("/register", methods=["POST"])
def register_user():
    
    form_data={
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "password": request.form["password"],
        "confirm_password": request.form["confirm_password"]
    }
    if not User.validate_user(form_data):
        return redirect('/')
    hash_pw= bcrypt.generate_password_hash(request.form['password'])
    data= {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "password": hash_pw
    }
    user=User.insert_user(data)
    session["user_id"]=user
    return redirect ("/dashboard")

@app.route('/login', methods=["POST"])
def login_user():
    data={
        "email":request.form["email"]
    }
    user_in_db=User.find_user_by_email(data)
    if not user_in_db:
        flash("Invalid email/password", "login")
        return redirect('/')
    if not bcrypt.check_password_hash(user_in_db.password, request.form["password"]):
        flash("Invalid email/password", "login")
        return redirect('/')

    session["user_id"]=user_in_db.id

    return redirect("/dashboard")

@app.route('/dashboard')
def dashboard_page():
    if not "user_id" in session:
        return redirect("/")

    data={
        "id":session["user_id"]
    }
    user=User.get_user_by_id(data)
    all_requests=Ride.get_all_ride_requests_w_rider_info()
    all_booked=Ride.get_all_booked_requests()

    return render_template("dashboard.html", user=user, all_requests=all_requests, all_booked=all_booked)

@app.route('/logout')
def logout():
    session.clear()
    return redirect ("/")

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

