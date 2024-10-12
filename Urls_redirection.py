from flask import Flask,render_template,Request,redirect,url_for


app = Flask(__name__)

@app.route("/")
def home():
    return "<h1> Hello from welcome page </h1>"

@app.route("/score/<name>/<int:num>")
def score(name,num):
    if num >= 33:
        #redirect the pass function/page.
        return redirect(url_for("suceess"))
    else:
        #redirection fail function/page.
        return redirect(url_for("fail"))
    

@app.route("/suceess")
def suceess():
    return "<h1> Congrats you have been pass in exam.</h1>"


@app.route("/fail")
def fail():
    return "<h1> Alas! you have been fail in exam</h1>"


if __name__ ==  "__main__" :
    app.run(debug=True)