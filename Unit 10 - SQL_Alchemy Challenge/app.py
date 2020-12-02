# import all the stuff
import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect
from flask import Flask, jsonify

#SQLAlchemy 
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)
Measurement = Base.classes.measurement
Station = Base.classes.station


#Flask 
app = Flask(__name__)


#Define main route
@app.route("/")
def welcome():
    return "Welcome to my Weather Alchemy Page"

#Define precipitation route
@app.route("/api/v1.0/precipitation")
def precipitation():
    return "This is the precipitation for the last year"

#Define main behavior
if __name__ == "__main__":
    app.run(debug=True)
