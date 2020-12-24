# Web Scraping Challenge - Mission to Mars

In this challenge, I will build a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page.

## 1. Scraping

Initial scraping will be done using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.

A Jupyter Notebook file called [mission_to_mars.ipynb](https://github.com/cecileung1208/Homework/blob/master/Unit%2012%20-%20Web%20Scraping%20Challenge/Mission%20to%20Mars/mission_to_mars.ipynb) and use this to complete all of your scraping and analysis tasks. The following outlines what you need to scrape.


### NASA Mars News

* Scrape the [NASA Mars News Site](https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest) and collect the latest News Title and Paragraph Text. Variables have been assigned so it can be referenced later on.
* Output:<br>
  news_title = A Martian Roundtrip: NASA's Perseverance Rover Sample Tubes<br>
  ---------------------------------------------------------------------------------------------------------------------------<br>
  news_p = Marvels of engineering, the rover's sample tubes must be tough enough to safely bring Red Planet samples on the long journey back to Earth in immaculate condition. 
