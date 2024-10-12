from flask import Flask,render_template,Request


app = Flask(__name__)

@app.route("/")
def home():
    return "<h1> Hello from welcome page </h1>"

@app.route("/welcome/<name>")
def welcome_Steve(name):
    return f"welcome {name} to this page"


if __name__ ==  "__main__" :
    app.run(debug=True)