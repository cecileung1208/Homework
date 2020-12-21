#!/usr/bin/env python
# coding: utf-8

# # Mission to Mars

# ### Import Dependencies


# Import dependencies
from bs4 import BeautifulSoup
import requests
import pandas as pd
import pymongo
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import time


# ### NASA Mars News

# Use Splinter to Run URL to extract news headlines and paragraph text
def init_browser():
    executable_path = {'executable_path': 'chromedriver'} #ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    return browser


def scrape_info():
    browser = init_browser()
    # URL of page to be scraped
    url = 'https://mars.nasa.gov/news/'

    # Visit through chrome browser 
    browser.visit(url)

    # create html to extract news information
    html = browser.html

    # Create BeautifulSoup object; parse with 'html.parser'
    soup = BeautifulSoup(html,'html.parser')

    # Get html code of latest news
    results = soup.find('li', class_='slide')


    # Extract the latest news and its paragraph text
    news_title = results.find('div', class_='content_title').text
    news_text = results.find('div', class_='article_teaser_body').text


    time.sleep(2)

    ### JPL Mars Space Images - Featured Image
    # URL to visit
    jpl_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'

    # Visit through chrome browser 
    browser.visit(jpl_url)

    # Create html to extract news information
    html_jpl = browser.html

    # Create BeautifulSoup object; parse with 'html.parser'
    soup_jpl = BeautifulSoup(html_jpl,'html.parser')


    # Extract the link for the featured image
    image = soup_jpl.find('div', class_='carousel_items').a['data-fancybox-href']


    #Link main URL to image link to get the full URL of the image in JPL website
    main_url = 'https://www.jpl.nasa.gov'
    featured_image_url= main_url + image


    time.sleep(2)

    ### Mars Facts

    #Mars Facts URL
    url_mars_facts= 'https://space-facts.com/mars/'


    # Use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
    table_mars= pd.read_html(url_mars_facts)


    # The above output parses all tables from the URL.  We only need the first table.
    mars_df = table_mars[0]


    #Format the table by changing column names
    column_names = {mars_df.columns[0]: 'Description', mars_df.columns[1]: 'Value'}
    mars_df.rename(columns = column_names)


    # Use Pandas to convert the data to a HTML table string.
    mars_facts_html = mars_df.to_html()
    time.sleep(2)

    # Mars Hemisphere

    # URL of page to be scraped
    url_mars_hemisphere = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

    # Visit through chrome browser 
    browser.visit(url_mars_hemisphere)

    # create html to extract news information
    html_astropedia = browser.html


    # Create BeautifulSoup object; parse with 'html.parser'
    soup_mars_hemisphere = BeautifulSoup(html_astropedia,'html.parser')


    hemi_img_urls = []

    h3links= browser.find_by_tag("h3")


    for items in range(len(h3links)):
        hemidict = {}
    
        browser.find_by_css('h3')[items].click()
    
        ## titles
        hemidict['title']=browser.find_by_css('h2.title').text
    
        ## images
        image_url= browser.links.find_by_text('Sample').first
        hemidict['img_url'] = image_url['href']
        hemi_img_urls.append(hemidict)
        browser.back()
    
    time.sleep(2)

    # create dictionary to hold all mars info scraped

    mars_data = {
            "news_title": news_title,
            "news_text": news_text,
            "featured_image_url": featured_image_url,
            "html_table": mars_facts_html,
            "hemisphere_img_urls": hemi_img_urls
    }



  # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_data