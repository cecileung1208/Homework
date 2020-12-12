# Web Design Challenge - Web Visualization Dashboard (Latitude) 

Data is more powerful when we share it with others! Let's take what we've learned about HTML and CSS to create a dashboard showing off the analysis we've done.


## Latitude - Latitude Analysis Dashboard with Attitude

Visualization dashboard website will be created  with plotting [weather data](https://github.com/cecileung1208/Homework/blob/master/Unit%2011%20-%20Web%20Design%20Challenge/Resources/cities.csv).<br>

In building this dashboard, we'll create individual pages for each plot and a means by which we can navigate between them. These pages will contain the visualizations and their corresponding explanations. We'll also have a landing page, a page where we can see a comparison of all of the plots, and another page where we can view the data used to build them.

### Website Requirements
For reference, see the [Screenshots](#screenshots) section below.

The website must consist of 7 html pages and 1 style page in total, including:

**1. A [Landing page](#landing-page) containing:**

  - An explanation of the project.
  - Links to each visualizations page. There should be a sidebar containing preview images of each plot, and clicking an image should take the user to that visualization.
  - See the [index.html file](https://github.com/cecileung1208/Homework/blob/master/Unit%2011%20-%20Web%20Design%20Challenge/index.html) for the html codes.

**2. Four [Visualization pages](#visualizations-page), each with:**

  - A descriptive title and heading tag.
  - The plot/visualization itself for the selected comparison.
  - A paragraph describing the plot and its significance.
  - See the [max_temp.html file](https://github.com/cecileung1208/Homework/blob/master/Unit%2011%20-%20Web%20Design%20Challenge/max_temp.html), [humidity.html file](https://github.com/cecileung1208/Homework/blob/master/Unit%2011%20-%20Web%20Design%20Challenge/humidity.html), [cloudiness.html file](https://github.com/cecileung1208/Homework/blob/master/Unit%2011%20-%20Web%20Design%20Challenge/cloudiness.html), and [wind_speed.html file](https://github.com/cecileung1208/Homework/blob/master/Unit%2011%20-%20Web%20Design%20Challenge/wind_speed.html) for the html codes.


**3. A [Comparisons page](#comparisons-page) that:**

  - Contains all of the visualizations on the same page so we can easily visually compare them.
  - Uses a Bootstrap grid for the visualizations.
  - The grid must be two visualizations across on screens medium and larger, and 1 across on extra-small and small screens.
  - See the [comparisons.html file](https://github.com/cecileung1208/Homework/blob/master/Unit%2011%20-%20Web%20Design%20Challenge/comparisons.html) for the html codes.


**4. A [Data page](#data-page) that:**

  - Displays a responsive table containing the data used in the visualizations.
  - The table must be a bootstrap table component. 
  - The data must come from exporting the [.csv file](https://github.com/cecileung1208/Homework/blob/master/Unit%2011%20-%20Web%20Design%20Challenge/Resources/cities.csv) as HTML, or converting it to HTML. Try using a tool you already know, pandas. Pandas has a nifty method approprately called [to_html](https://github.com/cecileung1208/Homework/blob/master/Unit%2011%20-%20Web%20Design%20Challenge/Resources/Cities%20Table%20HTML%20Coversion.ipynb) that allows you to generate a HTML table from a pandas dataframe.
  - See the [data.html file](https://github.com/cecileung1208/Homework/blob/master/Unit%2011%20-%20Web%20Design%20Challenge/data.html)
 
**5. Style Sheet**

  - This is to store default settings for the html files.  
  - Settings include fonts, padding, background colour, formats for resizing the browser etc for the header and paragraph text, navigation bar, containers, column sizes, footer.
  - Details are in the [style.css file](https://github.com/cecileung1208/Homework/blob/master/Unit%2011%20-%20Web%20Design%20Challenge/style.css)
### Screenshots

#### Landing Page

Large Screen

![Image](https://github.com/cecileung1208/Homework/blob/master/Unit%2011%20-%20Web%20Design%20Challenge/Visualizations/Dashboard%20-%20Big%20Screen.png)

Small Screen

![Image](https://github.com/cecileung1208/Homework/blob/master/Unit%2011%20-%20Web%20Design%20Challenge/Visualizations/Dashboard%20-%20Small%20Screen.png)


#### Visualizations Page

Large Screen 

![Image](https://github.com/cecileung1208/Homework/blob/master/Unit%2011%20-%20Web%20Design%20Challenge/Visualizations/Visualization%20-%20Big%20Screen.png)

Small Screen 

![Image](https://github.com/cecileung1208/Homework/blob/master/Unit%2011%20-%20Web%20Design%20Challenge/Visualizations/Visualization%20-%20Small%20Screen.png)

#### Comparisons Page

Large Screen

![Image](https://github.com/cecileung1208/Homework/blob/master/Unit%2011%20-%20Web%20Design%20Challenge/Visualizations/Comparison-%20Big%20Screen.png)

Small Screen

![Image](https://github.com/cecileung1208/Homework/blob/master/Unit%2011%20-%20Web%20Design%20Challenge/Visualizations/Comparison-%20Small%20Screen.png)

#### Data Page

Large Screen

![Image](https://github.com/cecileung1208/Homework/blob/master/Unit%2011%20-%20Web%20Design%20Challenge/Visualizations/Data%20-%20Big%20Screen.png)

Small Screen

![Image](https://github.com/cecileung1208/Homework/blob/master/Unit%2011%20-%20Web%20Design%20Challenge/Visualizations/Data%20-%20Small%20Screen.png)

#### Navigation Bar

Large Screen 

![Image](https://github.com/cecileung1208/Homework/blob/master/Unit%2011%20-%20Web%20Design%20Challenge/Visualizations/Navigation%20Bar%20-%20Big%20Screen.png)

Small Screen

![Image](https://github.com/cecileung1208/Homework/blob/master/Unit%2011%20-%20Web%20Design%20Challenge/Visualizations/Navigation%20Bar%20-%20Small%20Screen.png)

## Folders and Directories

The below folders have the following files:

| Folder Name    | File Name |
| ------------- | ------------- |
| Unit 11 - Web Design Challenge  | [README.md](https://github.com/cecileung1208/Homework/blob/master/Unit%2011%20-%20Web%20Design%20Challenge/README.md)|
|                                  | [index.html](https://github.com/cecileung1208/Homework/blob/master/Unit%2011%20-%20Web%20Design%20Challenge/index.html)|
|                                  | [max_temp.html](https://github.com/cecileung1208/Homework/blob/master/Unit%2011%20-%20Web%20Design%20Challenge/max_temp.html)|
|                                  | [humidity.html](https://github.com/cecileung1208/Homework/blob/master/Unit%2011%20-%20Web%20Design%20Challenge/humidity.html)|
|                                  | [cloudiness.html](https://github.com/cecileung1208/Homework/blob/master/Unit%2011%20-%20Web%20Design%20Challenge/cloudiness.html)|
|                                  | [wind_speed.html](https://github.com/cecileung1208/Homework/blob/master/Unit%2011%20-%20Web%20Design%20Challenge/wind_speed.html)|
|                                  | [comparisons.html](https://github.com/cecileung1208/Homework/blob/master/Unit%2011%20-%20Web%20Design%20Challenge/comparisons.html)|
|                                  | [data.html](https://github.com/cecileung1208/Homework/blob/master/Unit%2011%20-%20Web%20Design%20Challenge/data.html)|
|                                  | [style.css](https://github.com/cecileung1208/Homework/blob/master/Unit%2011%20-%20Web%20Design%20Challenge/style.css)|


Inside the Web Challenge Folder, there are the Assets, Resources, and Visualization folders that store the following files:

| Folder Name    | File Name |
| ------------- | ------------- |
| Assets        | [Latitude_MaxTemp.png](https://github.com/cecileung1208/Homework/blob/master/Unit%2011%20-%20Web%20Design%20Challenge/Assets/Latitude_MaxTemp.png)|
|               | [Latitude_Humidity.png](https://github.com/cecileung1208/Homework/blob/master/Unit%2011%20-%20Web%20Design%20Challenge/Assets/Latitude_Humidity.png)|
|               | [Latitude_Cloudiness.png](https://github.com/cecileung1208/Homework/blob/master/Unit%2011%20-%20Web%20Design%20Challenge/Assets/Latitude_Cloudiness.png)|
|               | [Latitude_WindSpeed.png](https://github.com/cecileung1208/Homework/blob/master/Unit%2011%20-%20Web%20Design%20Challenge/Assets/Latitude_WindSpeed.png)|
| Resources   | [Cities Table HTML Coversion](https://github.com/cecileung1208/Homework/blob/master/Unit%2011%20-%20Web%20Design%20Challenge/Resources/Cities%20Table%20HTML%20Coversion.ipynb)|
|             | [cities.csv](https://github.com/cecileung1208/Homework/blob/master/Unit%2011%20-%20Web%20Design%20Challenge/Resources/cities.csv)|
| Visualizations   | [Dashboard- Big Screen.png](https://github.com/cecileung1208/Homework/blob/master/Unit%2011%20-%20Web%20Design%20Challenge/Visualizations/Dashboard%20-%20Big%20Screen.png)|
|                 | [Dashboard- Small Screen.png](https://github.com/cecileung1208/Homework/blob/master/Unit%2011%20-%20Web%20Design%20Challenge/Visualizations/Dashboard%20-%20Small%20Screen.png)|
|                 | [Visualization- Big Screen.png](https://github.com/cecileung1208/Homework/blob/master/Unit%2011%20-%20Web%20Design%20Challenge/Visualizations/Visualization%20-%20Big%20Screen.png)|
|                 | [Visualization- Small Screen.png](https://github.com/cecileung1208/Homework/blob/master/Unit%2011%20-%20Web%20Design%20Challenge/Visualizations/Visualization%20-%20Small%20Screen.png)|
|                 | [Comparison- Big Screen.png](https://github.com/cecileung1208/Homework/blob/master/Unit%2011%20-%20Web%20Design%20Challenge/Visualizations/Comparison-%20Big%20Screen.png)|
|                 | [Comparison- Small Screen.png](https://github.com/cecileung1208/Homework/blob/master/Unit%2011%20-%20Web%20Design%20Challenge/Visualizations/Comparison-%20Small%20Screen.png)|
|                 | [Data- Big Screen.png](https://github.com/cecileung1208/Homework/blob/master/Unit%2011%20-%20Web%20Design%20Challenge/Visualizations/Data%20-%20Big%20Screen.png)|
|                 | [Data- Small Screen.png](https://github.com/cecileung1208/Homework/blob/master/Unit%2011%20-%20Web%20Design%20Challenge/Visualizations/Data%20-%20Small%20Screen.png)|
|                 | [Navigation Bar- Big Screen.png](https://github.com/cecileung1208/Homework/blob/master/Unit%2011%20-%20Web%20Design%20Challenge/Visualizations/Navigation%20Bar%20-%20Big%20Screen.png)|
|                 | [Navigation Bar- Small Screen.png](https://github.com/cecileung1208/Homework/blob/master/Unit%2011%20-%20Web%20Design%20Challenge/Visualizations/Navigation%20Bar%20-%20Small%20Screen.png)|

