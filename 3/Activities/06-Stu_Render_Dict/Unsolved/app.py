# import necessary libraries
from flask import Flask, render_template

# @TODO: Initialize your Flask app here
# CODE GOES HERE
app = Flask(__name__)
# @TODO: Create a list of dictionaries
# CODE GOES HERE
d_list=[{"ID":1,"Item":"Basketball"},{"ID":2,"Item":"Soccerball"},{"ID":3,"Item":"Tennis ball"}]
# @TODO:  Create a route and view function that takes in a dictionary and renders index.html template
# CODE GOES HERE
@app.route('/')
def main():
    return render_template('index.html',list=d_list)

if __name__ == "__main__":
    app.run(debug=True)
