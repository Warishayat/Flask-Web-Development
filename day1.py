from flask import Flask
from flask import redirect,render_template,request


app = Flask(__name__) #special variable that python assign

@app.route("/") #enpoints
@app.route("/home") #endpoints adres of the web page
def home():
    return " <h1> Welcome to the home page </h1>"


@app.route("/about") #endpoints
def about():
    return "<h1>Welcome to the About page </h1>"

@app.route("/welcome/<name>") #path parameter
def welcome(name):
    return f"hi {name} welcome to this page"


@app.route("/addition/<int:num>/<int:num2>") #passing aprameters
def addition(num,num2):
    return f"{num} + {num2} is = {num+num2}"

if __name__ == "__main__":
    app.run(debug=True)
