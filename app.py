from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/registrants")
def registrants():
  name = request.argv.get(name, "Whoever your name is")
  surname = request.argv.get(surname, "Whoever your surname is")
  
  return render_template("registrants.html", name=name, surname=surname)
