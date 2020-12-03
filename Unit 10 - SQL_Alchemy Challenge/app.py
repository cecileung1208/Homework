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
    return "Welcome to Hawaii's Alchemy Page!!<br>"
        
#Define precipitation route
@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)
    last_date= session.query(func.max(Measurement.date)).first()
    latest_date =  list(np.ravel(last_date))
    year = int(latest_date[0][0]+latest_date[0][1]+latest_date[0][2]+latest_date[0][3])
    month =int(latest_date[0][5]+latest_date[0][6])
    date = int(latest_date[0][8]+latest_date[0][9])
    year_ago = dt.date(year, month, date) - dt.timedelta(days=365)
    year_later = dt.date(year,month, date)
    one_year_prcp = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date > year_ago, Measurement.date<= year_later).all()
    session.close()
    return jsonify(one_year_prcp)

#Define stations route
@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    stations= session.query(Station.station, Station.name).all()
    session.close()
    return jsonify(stations)

#Define tobs route
@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)
    last_date= session.query(func.max(Measurement.date)).first()
    latest_date =  list(np.ravel(last_date))
    year = int(latest_date[0][0]+latest_date[0][1]+latest_date[0][2]+latest_date[0][3])
    month =int(latest_date[0][5]+latest_date[0][6])
    date = int(latest_date[0][8]+latest_date[0][9])
    year_ago = dt.date(year, month, date) - dt.timedelta(days=365)
    year_later = dt.date(year,month, date)
    most_active_yearly_temp = session.query(Measurement.date, Measurement.tobs).filter(Measurement.date > year_ago, Measurement.date<= year_later).filter(Measurement.station == 'USC00519281').all()
    session.close()
    return jsonify(most_active_yearly_temp)

@app.route("/api/v1.0/tobs_test")
def tobs_test():
    session = Session(engine)
    results = session.query(Station.name, Measurement.date, Measurement.tobs).\
        filter(Measurement.date >= "2016-08-24", Measurement.date <= "2017-08-23").\
        all()
    tobs_list = []
    for result in results:
        row = {}
        row["Station"] = result[0]
        row["Date"] = result[1]
        row["Temp"] = int(result[2])
        tobs_list.append(row)
    session.close()
    return jsonify(tobs_list)

#Define main behavior
if __name__ == "__main__":
    app.run(debug=True)
