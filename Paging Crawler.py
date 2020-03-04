#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from selenium import webdriver
import time

from bs4 import BeautifulSoup
from datetime import datetime
import requests
import pandas as pd
import re

#put the object you want to scrape
date_text=[]
content_text=[]
title_text=[]
category_text=[]

def scraper():  
    html=driver.page_source
    soup=BeautifulSoup(html,'html.parser')

    # put the object you want to scrape in this section
    
    dates=soup.select('.date')
    for date in dates:
        date_text.append(date.text)
    date_text.remove('')
    date_text.remove('')

    titles=soup.select('a.ellipsis')
    for title in titles:
        title_text.append(title.text)
        
    contents=soup.select('span.ellip')
    for content in contents:
        content_text.append(content.text)

    categories=soup.select('.topic.ellipsis')
    for category in categories:
        category_text.append(category.text)

        
def crawler():
    #put your Chrmoe driver location here
    #make sure you have Chromedriver on the proper route
    driver=webdriver.Chrome('/YourChromeDriverLocation/chromedriver')
    driver.get("https://www.data.go.kr/useCase/exam/index.do")
    
    max_page=int(input('input the maxpage'))

    #find and apply the x-path pattern of the paging button in this section
    for i in range(1,max_page/10):
        for j in range(3,12):
            scraper()
        
            driver.find_element_by_xpath("""//*[@id="sub-main"]/div[3]/div[2]/div/a["""+str(j)+"""]""").click()

    #This section is for saving result as a excel file   
            
    result={"date":date_text, "category":category_text, "title":title_text, "content":content_text}
    df=pd.DataFrame(result)

    df.to_excel('result.xlsx',sheet_name = 'Sheet1')
    

