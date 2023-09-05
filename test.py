#HTTP request 
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

#Send an HTTP request and get the page content
url = "https://reviews.webmd.com/drugs/drugreview-841-atorvastatin-oral"
response = requests.get(url)

soup = bs(response.content , 'html.parser')
# 01 div box
l1 = soup.find("div", class_="review-details")
l2= l1.find("strong" , class_="condition.name")
print(l2)
# 02 div box
l3 = soup.find("div" , class_="review-details")
l4 =l3.find("div" , class_="condition")
print(l4)
#03 div box
l5 = soup.find("div", class_="review-details")
l6 = l5.find("strong", class_="condition")

# 04 div box
l7 = soup.find("div", class_="review-details")
l8 = l7.find("strong", class_="condition")

for test in soup.find_all("div" , class_="shared-reviews-container"):
    test1 = test.find("div" , class_="review-details")
    if test1:
        test2.append(test1.text.script())  

# add list 
# lists = []
# lists.append(l2)
# lists.append(l4)
# lists.append(l6)
# lists.append(l8)
#print(lists)
# list1 = pd.DataFrame(lists)
# list1.to_csv("drug")
