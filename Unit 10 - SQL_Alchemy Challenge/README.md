# SQLAlchemy Challenge - Surfs Up!

After settling in my career as a Data Analyst, I have decided to treat myself to a long holiday vacation in Honolulu, Hawaii! To help with my trip planning, I need to do some climate analysis on the area.

## **1. - Climate Analysis and Exploration**

Python and SQLAlchemy have been used to conduct climate anlysis and data exploration by connecting to the SQLite Database. 

The analysis is completed in the [Climate Starter Notebook](https://github.com/cecileung1208/Homework/blob/master/Unit%2010%20-%20SQL_Alchemy%20Challenge/climate_starter.ipynb) and [Hawaii SQLite Dabtabse](https://github.com/cecileung1208/Homework/blob/master/Unit%2010%20-%20SQL_Alchemy%20Challenge/Resources/hawaii.sqlite) have been used to obtain the climate results using SQLAlchemy ORM queries, Pandas, and Matplotlib methods.


### **Precipitation Analysis**

Before planning any activities, I want to know if the weather is good!  Otherwise, it would be disappointing if I had to cancel any activities because of rain.

A query have been designed to collect the past 12 months of precipitation data to determine which time of the year have the most rain.

![Image](https://github.com/cecileung1208/Homework/blob/master/Unit%2010%20-%20SQL_Alchemy%20Challenge/Output%20Files/Annual%20Precipitation.png)

### **Station Analysis**

To ensure that my analysis is accurate, weather information have been gathered from various stations.  

A query have been designed to determine the total number of stations, most active station with the highest number of observations, and to retrieve the last 12 months temperature observation data (TOBS).


![Image](https://github.com/cecileung1208/Homework/blob/master/Unit%2010%20-%20SQL_Alchemy%20Challenge/Output%20Files/Annual%20Temperature.png)


## **2. - Climate App**

Upon the completion of my initial analysis, a [Flask API file](https://github.com/cecileung1208/Homework/blob/master/Unit%2010%20-%20SQL_Alchemy%20Challenge/app.py) have been designed for the queries I have developed.

The Flask API have been have the following routes:


* **Home page (/)**

* **Precipitation (/api/v1.0/precipitation)** 
    Return a JSON list of all precipitation information.
    
* **Stations (/api/v1.0/stations)** 
  Return a JSON list of stations from the dataset.
  
* **TOBS (/api/v1.0/tobs)**
  Return a JSON list of temperature observations (TOBS) for the previous year.
  
* **Temperature Statistics for Start Date (/api/v1.0/startdate)** 
    Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start date of your choice to the last day of the database.
  
* **Temperature Statistics for Start Date and End Date (/api/v1.0/startdate/enddate)** 
  Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start date and last date of your choice. 
  
  Note:  Dates should be entered in the format YYYY-MM-DD.
         Example 1 (/api/v1.0/2017-05-01)
         Example 2 (/api/v1.0/2017-05-01/2017-05-08)
