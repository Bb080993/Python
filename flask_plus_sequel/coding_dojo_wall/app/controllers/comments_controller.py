from app import app
from flask import Flask, render_template, redirect, request,session
from app.models.comment_model import Comment


# @app.route('/comment', methods=["POST"])
# def post_content():
#     data={
#         "post_id": request.form["post_id"],
#         "comment_text": request.form["comment_text"]
#     }
#     print("This is the comment data", request.form)
#     if not Comment.validate_comment(data):
#         return redirect (f"/wall/{session['user_id']}")
#     Comment.add_comment(data)
#     return redirect (f"/wall/{session['user_id']}")

# @app.route("/delete/<int:id>")
# def delete_comment(id):
#     data={
#         "id":id
#     }
#     Comment.delete_one_comment(data)
#     return redirect(f"/wall/{session['user_id']}")