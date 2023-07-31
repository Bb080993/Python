from app import app
from flask import Flask, render_template, redirect, request, session
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

@app.route('/edit/ninja/<int:id>')
def grab_one_ninja(id):
     data={
          'id':id
     }
     ninja=Ninja.get_one_ninja(data)
     #print(ninja)
     session["ninja_dojo_id"]=ninja["dojo_id"]
     #print(session["ninja_dojo_id"])
     return render_template("edit_ninja.html", ninja=ninja)

@app.route('/apply/edit', methods=["POST"])
def edit_ninja():
     
     one_ninja=Ninja.update_ninja(request.form)
     print("This is one ninja", one_ninja)
     return redirect(f'/dojo/{session["ninja_dojo_id"]}')







