from app import app
from flask import Flask, render_template, redirect, request, session, flash
from app.models.user_model import  User
from flask_bcrypt import Bcrypt
bcrypt=Bcrypt(app)

@app.route('/')          
def user_form():
    return render_template("login_registration.html")

@app.route('/register', methods=["POST"])
def register():
    if User.find_user(request.form):
        flash("Account already exists")
        return redirect ('/')
    #check if email is unique/not in database yet
 
    
    if not User.validate_user(request.form):
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    confirm_hash= bcrypt.generate_password_hash(request.form['confirm_password'])
    data={
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "password": pw_hash,
        "confirm_password": confirm_hash
    }
    user=User.insert_user(data)
    print("!!!!!!!!!", user)
    session["user_id"]=user
    return redirect(f'/dashboard/{session["user_id"]}')

@app.route('/login', methods=["POST"])
def login():
    hashed_pw=request.form['password']
    data={
        "email":request.form["email"]
    }
    user_in_db=User.find_user(data)
    if not user_in_db:
        flash("Invalid Email/password", "login")
        return re   `direct ('/')
    if not bcrypt.check_password_hash(user_in_db.password, hashed_pw):
        flash("Invalid Email/password", "login")
        return redirect ('/')
    session["user_id"]=user_in_db.id
    return redirect(f'/dashboard/{session["user_id"]}')

@app.route('/dashboard/<int:id>')
def dashboard_page(id):
    data={
        'id':id
    }
    one_user=User.get_one_user(data)
    print(one_user)
    session["first_name"]=one_user['first_name']
    return render_template ("welcome_dashboard.html")

@app.route('/logout')
def logout():
    session.clear()
    return redirect ("/")



