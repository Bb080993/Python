from app import app
from flask import Flask, render_template, redirect, request, flash
from app.models.users_model import User




@app.route('/')          
def user_form():
    return render_template("create.html")

@app.route('/creating_user', methods=['POST'])
def create_form():
    data={
        "first_name":request.form["first_name"],
        "last_name":request.form["last_name"],
        "email":request.form["email"]
    }
    if not User.validate_user(data):
        return redirect('/')
    new_user=User.save(data)
    print("This is our new user line 17", new_user)
    return redirect(f"/one_user/{new_user}") 

@app.route('/all_users')
def see_all_users():
    all_users=User.get_all_users()
    return render_template("read_all.html", all_users=all_users)

@app.route('/one_user/<int:id>')
def get_one_user(id):
    data={
        "id": id
    }
    user=User.get_one_user(data)
    return render_template("read_one.html", user=user)

@app.route('/edit/<int:id>')
def get_current_info(id):
    data={
        "id": id,
        # "first_name":request.form["first_name"],
        # "last_name":request.form["last_name"],
        # "email":request.form["email"]
    }
    return render_template ('edit.html', user=User.get_one_user(data))

@app.route('/update_form', methods=['POST'])
def update_user_info():
    data={
        "id":request.form["id"],
        "first_name":request.form["first_name"],
        "last_name":request.form["last_name"],
        "email":request.form["email"]
    }
    updated_user=User.update_user_info(data)
    
    return redirect(f"/one_user/{data['id']}" )

@app.route('/delete/<int:id>')
def delete_user(id):
    data={
        "id":id
    }
    User.delete_user(data)
    return redirect("/all_users")


