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

#Define the Query Dates
session = Session(engine)

# Calculate the date 1 year ago from the last data point in the database
year_ago = dt.date(2017,8,23) - dt.timedelta(days=365)


session.close()


#Flask 
app = Flask(__name__)


#Define main route
@app.route("/")
def welcome():
    return (
        f"Welcome to the Hawaii Weather Alchemy Page!!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/start/end<br/>"
    )


        
#Define precipitation route
@app.route("/api/v1.0/precipitation")
def precipitation():

    # Define Session & Query Precipitation Results
    session = Session(engine)
    prcp_results = session.query(Measurement.date, Measurement.prcp).all()
    session.close()
    
    # Create a dictionary as date the key and prcp as the value
    precipitation = []
    for value in prcp_results:
        prcp_dict = {}
        prcp_dict["Date"] = value[0]
        prcp_dict["Precipitation"] = value[1]
        precipitation.append(prcp_dict)

    return jsonify(precipitation)

#Define stations route
@app.route("/api/v1.0/stations")
def stations():

    # Define Session & Query Station Results
    session = Session(engine)
    station_names= session.query(Station.station, Station.name).all()
    session.close()
    

    # Create a dictionary as station id as the key and station name as the value
    stations = []
    for value in station_names:
        stations_dict = {}
        stations_dict["Station ID"] = value[0]
        stations_dict["Station Name"] = value[1]
        stations.append(stations_dict)

    return jsonify(stations)


#Define tobs route
@app.route("/api/v1.0/tobs")

# Define Session & Query Station Results
def tobs():
    session = Session(engine)
    tobs_results = session.query(Measurement.date, Measurement.tobs).filter(Measurement.date > year_ago).filter(Measurement.station == 'USC00519281').all()
    session.close()

    # Create a dictionary to query dates and temperature for the most active station in the past year.
    tobs_list = []
    for value in tobs_results:
        tob_dict = {}
        tob_dict["Date"] = value[0]
        tob_dict["Temperature"] = value[1]
        tobs_list.append(tob_dict)
    return jsonify(tobs_list)

#Define start date
@app.route('/api/v1.0/<startdate>/')
# Define Session & Query for temperature min, avg, max on start date till the latest date in the datset
def start(startdate):
    session = Session(engine)
    temp_results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
                   filter(Measurement.date >= startdate).all()
    
    # Create a dictionary to store the values 
    temp = []
    for value in temp_results:
        temp_dict = {}
        temp_dict["Temp Min"] = value [0]
        temp_dict["Temp Avg"] = value [1]
        temp_dict["Temp Max"] = value [2]
        temp.append(temp_dict)
    return jsonify(temp)

#Define start date and end date
@app.route('/api/v1.0/<startdate>/<enddate>')
# Define Session & Query for temperature min, avg, max on start date and end date of your choice

def startend(startdate,enddate):
    session = Session(engine)
    temp_startend_results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
                            filter(Measurement.date >= startdate, Measurement.date <= enddate).all()
    # Create a dictionary to query dates and temperature for the most active station in the past year.
    temp_daterange = []
    for value in temp_startend_results:
        temp_startend_dict = {}
        temp_startend_dict["Temp Min"] = value [0]
        temp_startend_dict["Temp Avg"] = value [1]
        temp_startend_dict["Temp Max"] = value [2]
        temp_daterange.append(temp_startend_dict)
    return jsonify(temp_daterange)

#Define main behavior
if __name__ == "__main__":
    app.run(debug=True)
