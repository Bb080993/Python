from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)  
app.secret_key = "I love Cobu"

@app.route('/')            
def user_form():
    return render_template("index.html")

@app.route('/process', methods=["POST"])          
def process_form():
    session['name']=request.form['name']
    session['dojo_location']=request.form['dojo_location']
    session['favorite_language']=request.form['favorite_language']
    session['comments']=request.form['comments']
    return redirect('/result')

@app.route('/result')         
def result():
    return render_template("results.html")

if __name__=="__main__":     
    app.run(debug=True, port=8000)  

