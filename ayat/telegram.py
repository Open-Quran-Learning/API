from flask import Flask
from ayat import app

@app.route("/")
@app.route("/ex0")
def example0():
    return "Ayat project: TODO"