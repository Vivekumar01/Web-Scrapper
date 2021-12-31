import csv

#pip install msedge-selenium-tools selenium==3.14
# from msedge.selenium_tools import Edge, EdgeOptions

#pip install bs4
from bs4 import BeautifulSoup as bs
#pip install pandas
import pandas as pd
#pip install selenium
from selenium import webdriver;

#path of the webdriver
path="C:\Program Files (x86)\chromedriver.exe"
#set the path driver
driver=webdriver.Chrome(path)

#read the top reviews
def search(search_term):
    #give url to the driver
    driver.get(search_term)
    #parse into html page
    soup= bs(driver.page_source,"html.parser")

    results=soup.find_all("span",class_="a-profile-name")   #read reviewers' name
    date=soup.find_all("span",class_="a-size-base a-color-secondary review-date")   #read posted date 
    review=soup.find_all("div",{"data-hook":"review-collapsed"})   #read review text
    review_rev = []
    cust = []
    date_rev = []
    print(len(date),len(results),len(review))
    if len(date)==len(results)==len(review):
        for i in range(0,len(results)):
            cust.append(results[i].get_text())
            date_rev.append(date[i].get_text().replace("Reviewed in India on ",""))
            review_rev.append(review[i].get_text().replace("\n",''))
    #create a data frame
    df = pd.DataFrame()
    df['reviewer']=cust
    df['posted_date']=date_rev
    df['review_text']=review_rev

    #saving the datafram in a csv format
    #make sure the path for csv file must be correct
    df.to_csv(r'D:\Downloads\Internship\Web Scraper\data.csv',index=False)
    # print(cust,end="\n")
    # print(date_rev,end="\n")
    print(review_rev,end="\n")
#url of the product
url="https://www.amazon.in/LG-24-inch-Monitor-Freesync-Borderless/dp/B08J5Y9ZSV/"
search(url)

