# import necessary libraries
from flask import Flask, render_template
import pymongo

# setup mongo connection
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)


# create instance of Flask app
app = Flask(__name__)


# create route that renders index.html template
@app.route("/scrape")
def scrape():
    return render_template("index.html")

@app.route("/")
def main():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
