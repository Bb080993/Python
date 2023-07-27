from flask import Flask, render_template, redirect, request
app = Flask(__name__)    
from users_model import User

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
    User.save(data)
    return redirect('/all_users')

@app.route('/all_users')
def see_all_users():
    all_users=User.get_all_users()
    return render_template("read_all.html", all_users=all_users)

if __name__=="__main__":   
    app.run(debug=True, port=8000)