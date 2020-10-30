# Matplotlib-Challenge - Pymaceuticals

As a Senior Data Analyst at Pymaceuticals, I have generated tables and figures from the given information on the results of 10 different drug treatments for squamous cell carcinoma (SCC), a commonly occuring form of skin scancer.  248 mice identified with SCC tumor were evenly tested across different drug regimens in a course of 45 days to determine if the tumor size have decreasd.

## **The Summary of Results have the following outputs:**

### **Pymaceuticals - Jupyter Notebook**

This [file](https://github.com/cecileung1208/Homework/blob/master/Unit%205%20-%20MatplotLib%20Challenge/Pymaceuticals/Pymaceuticals.ipynb) provides program codes that output various graphs and tables that determine the results of the cancer treatments across different drug regimen for 248 mice.  

**The output are as follows:**
*    Observations and Insights

**Summary Statistics of Tumor Volume by Drug Regimen**

The mean, median, variance, standard deviation, and standard error from mean (sem) of the tumor volume will be calculated across the 10 drug regimen by the :
*    Groupby Method
*    Aggregate Method

**Bar Graph of Unique Mice by Drug Regimen**
*   Dataframe Panda Method
*   Pyplot Method

**Pie Chart of Mice Gender Distribution**
*    Dataframe Panda Method
*    Pyplot Method

**Quartiles, Interquartiles and Boxplot of Most Promising Drug Regimen**

The 4 drug regimens are: Capomulin, Ceftamin, Infubinol, Ramicane
*    Quartiles and Interquartiles Results of the 4 Most Promising Drug Regimen
*    Outliers of the 4 Most Promising Drug Regimen
*    Boxplot of the 4 Most Promising Drug Regimen

**Line Graph of Tumor Size vs Timepoint**
*    Results for a Specific Mouse under the Capomulin Drug Regimen

**Scatter Plot of Average Tumor Size vs Weight**
*    Results under the  Capomulin Drug Regimen

**Coeeficient Correlation and Linear Regression Model of Average Tumor Size vs Weight** 
*    Results of Coefficient Correlation and Linear Regression under the Capomulin Scatter Plot

### **2.  Pymaceuticals Data Source**

The data frame is extracted from the following CSV Files in the [data directory](https://github.com/cecileung1208/Homework/tree/master/Unit%205%20-%20MatplotLib%20Challenge/Pymaceuticals/data):
*    [Mouse Metadata](https://github.com/cecileung1208/Homework/blob/master/Unit%205%20-%20MatplotLib%20Challenge/Pymaceuticals/data/Mouse_metadata.csv)
*    [Study Results](https://github.com/cecileung1208/Homework/blob/master/Unit%205%20-%20MatplotLib%20Challenge/Pymaceuticals/data/Study_results.csv)
