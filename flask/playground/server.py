"""from flask import Flask, render_template
app= Flask(__name__)
@app.route('/')
def welcome():
    return render_template("index.html")

@app.route('/play')
def play():
    num=3
    color="rgb(158,197,248)"
    return render_template("index.html", num=num, color=color)

@app.route('/play/<int:num>')
def play_num(num):
    return render_template("index.html", num=num)

@app.route('/play/<int:num>/<string:color>')
def num_color(num, color):
    return render_template("index.html", num=num, color=color)

if __name__=="__main__":     
    app.run(debug=True, port=8000)"""
from flask import Flask, render_template
app= Flask(__name__)

@app.route('/',defaults={"num":1, "color":"rgb(158,197,248)"})
@app.route('/play',defaults={"num":1, "color":"rgb(158,197,248)"})
@app.route('/play/<int:num>', defaults={"color":"rgb(158,197,248)"})
@app.route('/play/<int:num>/<string:color>')
def num_color(num, color):
    return render_template("index.html", num=num, color=color)


if __name__=="__main__":     
    app.run(debug=True, port=8000)