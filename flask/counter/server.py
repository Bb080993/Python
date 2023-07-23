from flask import Flask, render_template,request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def counter():
    if not "count" in session:
        session["count"]=0
    session["count"]+=1
    return render_template("index.html")

@app.route('/add_two', methods=['POST'])
def add_two():
    session['count']+=1
    return redirect('/') 

@app.route('/reset', methods=['POST'])
def reset():
    return redirect('/destroy_session') 

@app.route('/add_count', methods=['POST'])
def add_number():
    session['count']+= (int(request.form['add'])-1)
    return redirect('/')

@app.route('/destroy_session')
def clear_session():
    session.clear()
    return redirect ('/')

if __name__ == "__main__":
    app.run(debug=True, port=8000)