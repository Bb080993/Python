from flask import Flask, render_template, request, redirect
from flask_app.models.friend import Friend


app = Flask(__name__)

@app.route('/')
def index():
    friends = Friend.get_all()
    print(friends)
    return render_template("index.html", all_friends = friends)

@app.route('/create_friend', methods=["POST"])
def create_friend():
    data = {
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "occ": request.form["occ"]
    }
    Friend.save(data)
    return redirect('/')

@app.route('/friends/create', methods=['POST'])
def create():
    Friend.save(request.form)
    return redirect('/')
"""
@app.route('/friend/show/<int:friend_id>')
def show(friend_id):
    # calling the get_one method and supplying it with the id of the friend we want to get
    friend=Friend.get_one(friend_id)
    return render_template("show_friend.html", friend=friend)"""

            
if __name__ == "__main__":
    app.run(debug=True, port=8000)

