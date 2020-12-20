# import necessary libraries
from flask import Flask, render_template
import pymongo

# create instance of Flask app
app = Flask(__name__)


# create route that renders index.html template
@app.route("/scrape")
def scrape():
    movie_list = ["Mighty Ducks", "Space Jam", "Clerks", "Batman", "Avengers"]
    return render_template("index.html", list=movie_list)

@app.route("/")
def main():
    movie_list = ["Mighty Ducks", "Space Jam", "Clerks", "Batman", "Avengers"]
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
