from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

browser = webdriver.Chrome("D:/Setup/chromedriver_win32/chromedriver.exe")
browser.get(START_URL)

time.sleep(18)

scraped_data = []
stars_data = []

def scrape():
    soup = BeautifulSoup(browser.page_source, "html.parser")
    
    bright_star_table = soup.find("table")

    table_body = bright_star_table.find("tbody")
    table_rows = table_body.find_all("tr")

    for row in table_rows:
        table_cols = row.find_all("td")
        #print(table_cols)

        temp_list = []

        for col_data in table_cols:
            #print(col_data.text)
            data = col_data.text.strip()
            #print(data)

            temp_list.append(data)
        scraped_data.append(temp_list)
    #print(scraped_data)


    for i in range(0,len(scraped_data)):
        Star_names = scraped_data[i][1]
        Distance = scraped_data[i][3]
        Mass = scraped_data[i][5]
        Radius = scraped_data[i][6]

        required_data = [Star_names, Radius, Mass, Distance]
        stars_data.append(required_data)
    #print(stars_data)

scrape()

headers = ["Star_names", "Radius", "Mass", "Distance"]

star_df_1 = pd.DataFrame(stars_data, columns= headers)

star_df_1.to_csv("scraped_data.csv", index= True, index_label= "id")

