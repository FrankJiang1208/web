# import necessary libraries
from flask import Flask, render_template

# @TODO: Initialize your Flask app here
# CODE GOES HERE
app=Flask(__name__)
# @TODO:  Create a route and view function that takes in a string and renders index.html template
# CODE GOES HERE
@app.route("/")
def main():
    return render_template("index.html",header="Shan",hobby="I like to play tennis")

@app.route("/bonus.html")
def secret():
    return render_template("bonus.html",header="Shan",a='index.html')


if __name__ == "__main__":
    app.run(debug=True)
