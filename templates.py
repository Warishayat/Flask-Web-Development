from flask import Flask,redirect,url_for,render_template

app = Flask("__name__")

@app.route("/")
@app.route("/home")

def home():
    return render_template("index.html",title="HomePage")   #how to render custom templates/PlaceHolder

@app.route("/about")
def about():
    return render_template("index.html",title="ABOUTpAGE")  #how to render custom templates/PlaceHolder

if __name__ == "__main__":
    app.run(debug=True)

