# Web Scraping Challenge - Mission to Mars

In this challenge, I will build a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page.

## 1. Scraping

Initial scraping will be done using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.

A Jupyter Notebook file called [mission_to_mars.ipynb](https://github.com/cecileung1208/Homework/blob/master/Unit%2012%20-%20Web%20Scraping%20Challenge/Mission%20to%20Mars/mission_to_mars.ipynb) and use this to complete all of your scraping and analysis tasks. The following outlines what you need to scrape.


### NASA Mars News

* Scrape the [NASA Mars News Site](https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest) and collect the latest News Title and Paragraph Text. Variables have been assigned so it can be referenced later on.
* Example:<br><br>
  news_title = A Martian Roundtrip: NASA's Perseverance Rover Sample Tubes<br>
  ---------------------------------------------------------------------------------------------------------------------------<br>
  news_p = Marvels of engineering, the rover's sample tubes must be tough enough to safely bring Red Planet samples on the long journey back to Earth in immaculate condition. 



### JPL Mars Space Images - Featured Image

* Visit the url for [JPL Featured Space Image website](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars).
* Use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called featured_image_url.
* Example:<br><br>
  featured image url = https://www.jpl.nasa.gov/spaceimages/images/mediumsize/PIA00069_ip.jpg
  
### Mars Facts

* Visit the [Mars Facts webpage](https://space-facts.com/mars/) and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
* Use Pandas to convert the data to a HTML table string.

### Mars Hemispheres

* Visit the [USGS Astrogeology site](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) to obtain high resolution images for each of Mar's hemispheres.
* You will need to click each of the links to the hemispheres in order to find the image url to the full resolution image.
* Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Use a Python dictionary to store the data using the keys img_url and title.
* Append the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.
* Example:<br>
[{'title': 'Cerberus Hemisphere Enhanced', 'image_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg'},<br>
{'title': 'Schiaparelli Hemisphere Enhanced', 'image_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg'},<br>
{'title': 'Syrtis Major Hemisphere Enhanced', 'image_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg'},<br>
{'title': 'Valles Marineris Hemisphere Enhanced', 'image_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg'}]

## 2.  MongoDB and Flask Application

* Use MongoDB with Flask template to create a new HTML page that displays all of the information that was scraped from the URLs above.
* The [Jupyter notebook](https://github.com/cecileung1208/Homework/blob/master/Unit%2012%20-%20Web%20Scraping%20Challenge/Mission%20to%20Mars/mission_to_mars.ipynb) into a Python script called [scrape_mars.py](https://github.com/cecileung1208/Homework/blob/master/Unit%2012%20-%20Web%20Scraping%20Challenge/Mission%20to%20Mars/scrape_mars.py) with a function called scrape that will execute all of your scraping code from above and return one Python dictionary containing all of the scraped data.
* Create a file [app.py](https://github.com/cecileung1208/Homework/blob/master/Unit%2012%20-%20Web%20Scraping%20Challenge/Mission%20to%20Mars/app.py)
* Next, create a route called "/scrape" that will import your scrape_mars.py script and call your scrape function.
* Store the return value in Mongo as a Python dictionary.
* Create a root route "/" that will query your Mongo database and pass the mars data into an HTML template to display the data.
* Create a template HTML file called [index.html](https://github.com/cecileung1208/Homework/blob/master/Unit%2012%20-%20Web%20Scraping%20Challenge/Mission%20to%20Mars/templates/index.html) that will take the mars data dictionary and display all of the data in the appropriate HTML elements. Use the following as a guide for what the final product should look like, but feel free to create your own design.
