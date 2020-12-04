# SQLAlchemy Challenge - Surfs Up!

After settling in my career as a Data Analyst, I have decided to treat myself to a long holiday vacation in Honolulu, Hawaii! To help with my trip planning, I need to do some climate analysis on the area.

## **1. - Climate Analysis and Exploration**

Python and SQLAlchemy have been used to conduct climate anlysis and data exploration by connecting to the SQLite Database. 

The analysis is completed by using the [Climate Starter Notebook](https://github.com/cecileung1208/Homework/blob/master/Unit%2010%20-%20SQL_Alchemy%20Challenge/climate_starter.ipynb) and [Hawaii SQLite Database](https://github.com/cecileung1208/Homework/blob/master/Unit%2010%20-%20SQL_Alchemy%20Challenge/Resources/hawaii.sqlite) to obtain climate results using the SQLAlchemy ORM queries, Pandas, and Matplotlib.


### **Precipitation Analysis**

Before planning any activities, I want to know if the weather is good!  Otherwise, it would be disappointing if I had to cancel any activities because of rain.

A query have been designed to collect the past 12 months of precipitation data to determine which time of the year have the most rain.

![Image](https://github.com/cecileung1208/Homework/blob/master/Unit%2010%20-%20SQL_Alchemy%20Challenge/Output%20Files/Annual%20Precipitation.png)

### **Station Analysis**

To ensure that my analysis is accurate, weather information have been gathered from various stations.  

A query have been designed to determine the total number of stations and the most active station with the highest number of observations. 

| Station ID    | Station Name | Total Counts |
| ------------- | ------------- | ------------- |
|USC00519281 | WAIHEE 837.5, HI US | 2772|
|USC00519397 | WAIKIKI 717.2, HI US | 2724|
|USC00513117 | KANEOHE 838.1, HI US | 2709|
|USC00519523 | WAIMANALO EXPERIMENTAL FARM, HI US | 2669|
|USC00516128 | MANOA LYON ARBO 785.2, HI US | 2612|
|USC00514830 | KUALOA RANCH HEADQUARTERS 886.9, HI US | 2202|
|USC00511918 | HONOLULU OBSERVATORY 702.2, HI US | 1979|
|USC00517948 | PEARL CITY, HI US | 1372|
|USC00518838 | UPPER WAHIAWA 874.3, HI US | 511|




and to retrieve the last 12 months temperature observation data (TOBS).

The below histogram shows the frequency of the range of temperature in Hawaii form the most active station.

![Image](https://github.com/cecileung1208/Homework/blob/master/Unit%2010%20-%20SQL_Alchemy%20Challenge/Output%20Files/Annual%20Temperature.png)


## **2. - Climate App**

Upon the completion of my initial analysis, a [Flask API file](https://github.com/cecileung1208/Homework/blob/master/Unit%2010%20-%20SQL_Alchemy%20Challenge/app.py) have been designed for the queries I have developed.

The Flask API have the following routes:


* **Home page (/)**

* **Precipitation (/api/v1.0/precipitation)**<br/> - Return a JSON list of all precipitation information.
    
* **Stations (/api/v1.0/stations)**<br/> - Return a JSON list of stations from the dataset.
  
* **TOBS (/api/v1.0/tobs)** <br/> - Return a JSON list of temperature observations (TOBS) for the previous year.
  
* **Temperature Statistics for Start Date (/api/v1.0/startdate)**<br/> - Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start date of your choice to the last day on the database.
  
* **Temperature Statistics for Start Date and End Date (/api/v1.0/startdate/enddate)**<br/> - Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start date and last date of your choice. 
  
  **Note:**  Dates should be entered in the format YYYY-MM-DD.<br/>
         Example 1 (/api/v1.0/2017-05-01)<br/>
         Example 2 (/api/v1.0/2017-05-01/2017-05-08)<br/>
         
  
## **3. - Other Useful Analysis**

I have conducted additonal analysis to make the most out of my trip in the [Climate Starter Notebook](https://github.com/cecileung1208/Homework/blob/master/Unit%2010%20-%20SQL_Alchemy%20Challenge/climate_starter.ipynb).

### **Temperature Analysis I**

Analysis have been conducted by determining the averages of June an December for all stations across all available years in the dataset. 

A T-Test has been conducted to determine to test the difference of the mean with the following hypothesis.

Null Hypothesis: Mean Difference = 0<br/>
Alternative Hypothesis: Mean Difference > 0<br/>

P-value = 0.00036573

Since the p-value is almost 0.0004 , there is a difference in the mean temperatures in June and December.  Paired t-tests are considered more powerful than unpaired t-tests because using the same samples eliminiate variation between the samples that could be caused by anything other than what’s being tested.

Details of the analysis is in the [Climate Starter Notebook](https://github.com/cecileung1208/Homework/blob/master/Unit%2010%20-%20SQL_Alchemy%20Challenge/climate_starter.ipynb)

### **Temperature Analysis II**

My manager have approved my vacation days!  I am off to Hawaii from August 2 to August 10 and will be having lots of fun in the sun!!

The calc_temps function have been created to calculate the min, avg, and max temperatures for my trip.  The below graph shows the range of temperature during August 2 to August 10.

![Image](https://github.com/cecileung1208/Homework/blob/master/Unit%2010%20-%20SQL_Alchemy%20Challenge/Output%20Files/Trip%20Average%20Temperature.png)

### **Daily Rainfall Analysis**

Calculating the the total rainfall per weather station using the previous year's matching dates for my trip.

| Station ID    | Station Name | Latitude | Longitude | Elevation | Total Rainfall |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| USC00516128    | MANOA LYON ARBO 785.2, HI US | 21.33310 | -157.80250| 152.4 | 0.92 |
| USC00514830    | KUALOA RANCH HEADQUARTERS 886.9, HI US | 21.52130 | -157.83740 | 7.0 | 0.2 |
| USC00519281    | USC00519281	WAIHEE 837.5, HI US | 21.45167 | -157.84889 | 32.9 | 0.06 |
| USC00519397    | WAIKIKI 717.2, HI US | 21.27160 | -157.81680 | 3.0 | 0.02 |
| USC00519523    | WAIMANALO EXPERIMENTAL FARM, HI US | 21.33556 | -157.71139 | 19.5 | 0.00 |


### **Daily Normals**

The daily_normal function was used to calculate the averages for the min, avg, and max temperatures for my trip.  This date string will be in the format %m-%d that will use all historic TOBS that match that date string.

![Image](https://github.com/cecileung1208/Homework/blob/master/Unit%2010%20-%20SQL_Alchemy%20Challenge/Output%20Files/Daily%20Normals.png)


## **4.  Folders and Directories**

The below folders have the following files:

| Folder Name    | File Name |
| ------------- | ------------- |
| Unit 10 - SQL_Alchemy Challenge  | [README.md](https://github.com/cecileung1208/Homework/blob/master/Unit%2010%20-%20SQL_Alchemy%20Challenge/README.md)  |
|                                  | [app.py](https://github.com/cecileung1208/Homework/blob/master/Unit%2010%20-%20SQL_Alchemy%20Challenge/app.py) |
|                                  | [climate_starter.ipynb](https://github.com/cecileung1208/Homework/blob/master/Unit%2010%20-%20SQL_Alchemy%20Challenge/climate_starter.ipynb)|

Inside the Employee SQL_Alchemy Challenge Folder, there are the Ouput and Resources folders that stores the following files:

| Folder Name    | File Name |
| ------------- | ------------- |
| Output        | [Annual Precipitation.png](https://github.com/cecileung1208/Homework/blob/master/Unit%2010%20-%20SQL_Alchemy%20Challenge/Output%20Files/Annual%20Precipitation.png)|
|               | [Annual Temperature.png](https://github.com/cecileung1208/Homework/blob/master/Unit%2010%20-%20SQL_Alchemy%20Challenge/Output%20Files/Annual%20Temperature.png)|
|               | [Daily Normals.png](https://github.com/cecileung1208/Homework/blob/master/Unit%2010%20-%20SQL_Alchemy%20Challenge/Output%20Files/Daily%20Normals.png)  |
|               | [Trip Average Temperature.png](https://github.com/cecileung1208/Homework/blob/master/Unit%2010%20-%20SQL_Alchemy%20Challenge/Output%20Files/Trip%20Average%20Temperature.png)  |
| Resources   | [hawaii.sqlite](https://github.com/cecileung1208/Homework/blob/master/Unit%2010%20-%20SQL_Alchemy%20Challenge/Resources/hawaii.sqlite)  |
|             | [hawaii_meaurements.csv](https://github.com/cecileung1208/Homework/blob/master/Unit%2010%20-%20SQL_Alchemy%20Challenge/Resources/hawaii_measurements.csv)  |
|             | [hawaii_stations.csv](https://github.com/cecileung1208/Homework/blob/master/Unit%2010%20-%20SQL_Alchemy%20Challenge/Resources/hawaii_stations.csv)  |
