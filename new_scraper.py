from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import pandas as pd
import time

START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

browser = webdriver.Chrome("D:/Setup/chromedriver_win32/chromedriver.exe")
browser.get(START_URL)

time.sleep(18)

scraped_data = []
brown_dwarf = []
def new_scrape(hyperlink):
    
    page = requests.get(hyperlink) 
    soup = BeautifulSoup(page.content, "html.parser") 
    a = 0
    for table in soup.find_all("table", attrs={"class": "wikitable"}):
        a = a+1
        if a == 3:
            table_body = table.find("tbody")
    
    
    table_rows = table_body.find_all("tr")

    for tr_tags in table_rows: 
        td_tags = tr_tags.find_all("td") 
        temp_list = []
        for index, td_tag in enumerate(td_tags):
                try:
                    temp_list.append(td_tag.find_all("a")[0].contents[0])
                except:
                    try:
                        temp_list.append(td_tag.contents[0])
                    except:
                        temp_list.append("")
        scraped_data.append(temp_list)
        
    for i in range(1,len(scraped_data)):
        Star_names = scraped_data[i][0]
        Radius = scraped_data[i][8]
        Mass = scraped_data[i][7]
        Distance = scraped_data[i][5]

        required_data = [Star_names, Radius, Mass, Distance]
        brown_dwarf.append(required_data)

    new_scraped_data = []

    for row in brown_dwarf:
        replaced = []
        ## ADD CODE HERE ##

        for el in row:
            try:
                eln = el.replace("\n","")
                replaced.append(eln)
            except:
                replaced.append(el)
        
        new_scraped_data.append(replaced)
    
    print(new_scraped_data)

new_scrape(START_URL)

headers = ["Star_names", "Radius", "Mass", "Distance"]

brown_dwarf_df_1 = pd.DataFrame(brown_dwarf, columns= headers)

brown_dwarf_df_1.to_csv("new_scraped_data.csv", index= True, index_label= "id")