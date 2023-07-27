from app import app
from flask import Flask, render_template, redirect, request
from app.models.example_model import #PUT WHATEVER THE CLASS NAME IS HERE!




@app.route('/')          
def user_form():
    return render_template("index.html")



