#!/usr/bin/env python
# coding: utf-8

# In[138]:


# Dependencies
from splinter import Browser
from bs4 import BeautifulSoup
import requests
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager


# In[139]:


executable_path = {"executable_path": ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[140]:


url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
browser.visit(url)


# In[141]:


html = browser.html
# Parse HTML with Beautiful Soup
soup = BeautifulSoup(html, 'html.parser')


# In[142]:


print(soup.prettify())


# In[143]:


slide_soup = soup.find("li", class_="slide")
news_title = slide_soup.find('div', class_="content_title").a.text


# In[144]:


news_title


# In[145]:


paraphraph = slide_soup.find('div', class_="article_teaser_body").text


# In[146]:


paraphraph


# In[147]:


url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)


# In[148]:


browser.click_link_by_partial_text('FULL IMAGE')


# In[149]:


browser.click_link_by_partial_text('more info')


# In[150]:


html = browser.html
soup = BeautifulSoup(html, 'html.parser')


# In[151]:


images = soup.find('figure', class_= 'lede').a['href']


# In[152]:


images


# In[153]:


feature_image_url = f"https://www.jpl.nasa.gov/{images}"


# In[154]:


feature_image_url


# In[155]:


import pandas as pd


# In[156]:


url = 'https://space-facts.com/mars/'


# In[157]:


tables = pd.read_html(url)[0]
tables.columns= ["description", "data"]
tables.set_index("description", inplace=True)


# In[173]:


tables


# In[175]:


html_table = tables.to_html()
html_table


# In[176]:


html_table.replace('\n', '')


# In[159]:


#Mars Hemispheres
#Visit the USGS Astrogeology site here to obtain high resolution images for each of Mar's hemispheres.
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)


# In[160]:


html = browser.html
# Parse HTML with Beautiful Soup
soup = BeautifulSoup(html, 'html.parser')


# In[161]:


print(soup.prettify())


# In[162]:


lists = soup.find_all('div', class_='description')
lists


# In[163]:


img = lists[0]
img.a['href']


# In[164]:


images_url = []
base_url = "https://astrogeology.usgs.gov"
for page in lists:
    link = page.a['href']
    image_url = f"{base_url}+{link}"
    images_url.append(image_url)
print(images_url)


# In[177]:


#Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name.
hemisphere_image_urls = []
for url in images_url:
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    image_url = soup.find('div', class_='downloads').find('ul').find('li').find('a')['href']
    title = soup.find('h2', class_='title')
    dict = {"title": title, "image_url": image_url}
    print(title)
    print(image_url)
print(hemisphere_image_urls)


# In[ ]:




