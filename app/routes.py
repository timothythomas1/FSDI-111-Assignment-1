from flask import Flask, render_template     # from the flask "module" import the Flask class

app = Flask(__name__)       # Instantiate the Flask class 

# @app.get("/")
# def index():
#     return "<h1>Hello, World!!!</h1>"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    me = {
        "first_name": "Tim",
        "last_name": "Tom",
        "hobbies": "DIY stuff",
        "bio": "My name is Tim Tom, and I am  student"
    }
    return render_template("about.html", about_dict = me)

@app.route("/objects")
def objects():
    return render_template("objects.html")