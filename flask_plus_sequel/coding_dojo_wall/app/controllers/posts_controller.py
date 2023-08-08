from app import app
from flask import Flask, render_template, redirect, request,session
from app.models.post_model import Post

@app.route('/post', methods=["POST"])
def post_content():
    data={
        "user_id": request.form["user_id"],
        "content_text": request.form["content_text"]
    }
    if not Post.validate_post(data):
        return redirect (f"/wall/{request.form['user_id']}")
    Post.add_post(data)
    return redirect (f"/wall/{request.form['user_id']}")

@app.route("/delete/<int:id>")
def delete_post(id):
    data={
        "id":id
    }
    Post.delete_one_post(data)
    return redirect(f"/wall/{session['user_id']}")


