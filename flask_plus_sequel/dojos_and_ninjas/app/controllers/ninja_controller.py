from app import app
from flask import Flask, render_template, redirect, request
from app.models.dojo_model import Dojo
from app.models.ninja_model import Ninja


@app.route('/ninjas')          
def form_page():
     dojos=Dojo.get_all_users()
     return render_template("add_ninja.html", dojos=dojos)

@app.route('/ninja_form', methods=['POST'])
def add_ninja():
     data=request.form
     Ninja.add_ninja(data)
     #return redirect('/dojos')
     return redirect(f'/dojo/{request.form["dojo_id"]}')



