#Figure out how to scrape into other pages 
#Dyanmic scraping w selenium
#import urllib.request
#from urllib.request import urlopen
from bs4 import BeautifulSoup
#from selenium import webdriver
#from selenium.webdriver import Chrome
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
import requests
from requests_html import HTMLSession
import pandas as pd
import csv

tag_list=[]
size_list =[]
url_to_scrape = "https://www.kijiji.ca/b-kitchener-waterloo/apartment-rent-in-kitchener/k0l1700212"

'''
driver = webdriver.Chrome()
driver.get(url_to_scrape)
'''
 
session = HTMLSession()
response = session.get(url_to_scrape)
response.html.render()


soup = BeautifulSoup(response.html.html, 'html.parser')
listings = soup.find_all('div', class_ ="info-container")

filename = 'products.csv'
f = open(filename, 'w')
headers = 'Title, Price, Style, Bedrooms, Bathrooms, Size, Air Conditioned, Amenities \n'
f.write(headers)

print("check 1")

for listing in listings:
    print("check 2")
    title = listing.find('div', class_="title").text
    title =title.strip()
    title = title.replace(",","")

    print("check 3")
    price = listing.find('div', class_="price").text
    price = price.strip()
    price = price.replace(",", "")

    link = listing.find("a", href = True)
    weblink = "https://www.kijiji.ca" + link['href']
    print(weblink)

    if weblink.find("v-apartments-condos") > 0:
        
        response = session.get(weblink)
        response.html.render()
        soup = BeautifulSoup(response.html.html, 'html.parser')
        
        for tag in soup.find_all('li', class_='noLabelAttribute-2328647506'):
            tag_list.append(tag)
        style = tag_list[0].text
        bedrooms = tag_list[1].text
        bathrooms = tag_list[2].text
        tag_list.clear()

        for size in soup.find_all('dd', class_='twoLinesValue-2815147826'):
            size_list.append(size)
        if size_list[3].text == "Yes" or size_list[3].text == "No":
            size = size_list[4].text.replace(",","")
        else:
            size = size_list[3].text.replace(",","")
        air_conditioned = size_list[5].text.replace(",","")
        size_list.clear()




        f.write(title +', '+price + ', ' + style + ', ' +bedrooms +', ' +bathrooms +', ' +size + ', ' + air_conditioned +'\n')

    else: 
        pass
    

f.close()






'''
request_page = urlopen(url_to_scrape)
page_html = request_page.read()
request_page.close()
html_soup = BeautifulSoup(page_html, 'html.parser')

listings = driver.find_elements(By.NAME('sc-df900376 gsWCmx'))

for listing in listings:
    title = listing.find_element(By.xpath('.//*[@id="__next"]/div/div/main/div[2]/div[3]/div[3]/div[3]/div[1]/ul/li[1]/section/div[1]/div[2]/div[1]')).text
    price = listing.find_element(By.xpath('.//*[@id="__next"]/div/div/main/div[2]/div[3]/div[3]/div[3]/div[1]/ul/li[1]/section/div[1]/div[2]/div[1]/h3/a')).text
    print(title,price)

driver.quit()
'''
'''
house_title = html_soup.find_all('div', class_ ="sc-df900376 gsWCmx")
print(house_title)
filename = 'products.csv'
f = open(filename, 'w')

headers = 'Title, Price \n'

f.write(headers)

for main in house_title:
    print("hello")
    title = main.find('div', class_="sc-dab8bd1-0 bThYNJ").text
    #price = main.find('h3', attrs={'data-testid': 'listing-title'}).text

    f.write(title)

f.close()
print(page_html)
'''
