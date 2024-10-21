from flask import Flask,redirect,url_for,render_template
from employes import employes_data

app = Flask("__name__")

@app.route("/")
@app.route("/home")

def home():
    return render_template("index.html",title="Home")   #template inheritance same layout.html is use for both endpoints

@app.route("/about")
def about():
    return render_template("about.html",title="About")  #template inheritance same layout.html is use for both endpoints

@app.route("/checknumber/<int:num>")
def checknumber(num):
    return render_template("evaluate.html",title="evaluate",snum=num)


@app.route("/employees")  # Renamed from "/employes" to "/employees"
def show_employees():
    return render_template("employes.html", title="Employees", data=employes_data)


@app.route("/manager")  # Renamed from "/employes" to "/employees"
def manager():
    return render_template("manager.html", title="Manager", data=employes_data)

if __name__ == "__main__":
    app.run(debug=True)

