#pip install msedge-selenium-tools selenium==3.14
# from msedge.selenium_tools import Edge, EdgeOptions

#pip install bs4
from bs4 import BeautifulSoup as bs
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

    review=soup.find_all("span",{"data-hook":"review-body"})   #read review text
    review_rev=[]
    for i in range(0,len(review)):
        review_rev.append(review[i].get_text().replace("\n",''))
    for rev in review_rev:
        print(rev )

#url of the product
url="https://www.amazon.in/LG-24-inch-Monitor-Freesync-Borderless/product-reviews/B08J5Y9ZSV/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews"
search(url)

