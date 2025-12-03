# EW 7th Flask Notes

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        return redirect(url_for("user", name=request.form["name"]))
    return render_template("index.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/<name>")
def user(name):
    return f"<h1>Hello {name}!</h1>"

if __name__ == "__main__":
    app.run(debug=True)

# What does Flask do?
    # We are accessing the flask library that allows us to develop multi page websites.
# What are the steps to setting up a Flask project?
    # You have to set up a folder and a python file in the folder. You import and name the app and then do some defs.
# How can you reference subpages on your Flask project? (Meaning the difference between the home page and a personal profile)
    # Home just has a slash and the other parts have a / and something else
# What are templates?
    # They are outside html that you can import into tutorial.py that will then show up on your webpage. They are the cookie cutters you can create.