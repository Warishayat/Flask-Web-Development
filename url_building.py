from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1> Hello from welcome page </h1>"

@app.route("/score/<name>/<int:num>")
def score(name, num):
    if num < 33:
        # Redirect to the fail function/page.
        return redirect(url_for("fail", sname=name, marks=num))
    else:
        # Redirect to the success function/page.
        return redirect(url_for("success", sname=name, marks=num))
       
@app.route("/success/<sname>/<int:marks>")
def success(sname, marks):
    return f"<h1> Congrats {sname.title()} you have passed with {marks} </h1>"

@app.route("/fail/<sname>/<int:marks>")
def fail(sname, marks):
    return f"<h1> Alas! {sname.title()} you have failed with {marks}</h1>"

if __name__ == "__main__":
    app.run(debug=True)
