from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__) 
app.secret_key = "I love Cobu"

@app.route('/')          
def number_game():
    if not "number" in session:
        session["number"]=int(random.randint(1,100))
        color="rgb(41, 169, 238)"
    else:
        if session["guess"]>session["number"]:
            message="Too high"
            color="red"
        elif session["guess"]<session["number"] and session["guess"]>0:
            message="Too low"
            color="red"
        elif session["guess"]==session["number"]:
            message="You got it!"
            color="rgb(11, 194, 11)"
        else:
             message="Pick a number"
             color="lightblue"

    if not "guess" in session:
        session['guess']=0
        message="Pick a number"
        color="lightblue"
    return render_template("index.html", message=message, color=color)

@app.route('/guess', methods=['POST'])          
def guess():
    session["guess"]=int(request.form["guess"])
    return redirect('/')

@app.route('/clear_session')
def clear():
    session.clear()
    return redirect('/')


if __name__=="__main__": 
    app.run(debug=True, port=8000)  
