#HTTP request 
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

#Send an HTTP request and get the page content
url = "https://reviews.webmd.com/drugs/drugreview-841-atorvastatin-oral"
response = requests.get(url)


soup = bs(response.content, "lxml")

#list add condition

condition = []
for test in soup.find_all("div" , class_="review-details"):
   tests = test.find("strong" , class_="condition").text.split(':')[1]
   condition.append(tests)

# reviews

reviews = []

for rev in soup.findAll("div" , class_="overall-rating"):
   r = rev.find("strong").text
   re = r.split()[-1]
   reviews.append(re)

lists = {'condition':condition,'rating':reviews}
list1 = pd.DataFrame(lists)
list1.to_csv("drug.csv",index=False)

# connect the next page
max_pages = 10
current_page = 1
while current_page<=max_pages:
    next_page = soup.find("a" ,class_="page-link ")
    page =next_page.get("href")
    next_page_c = "https://reviews.webmd.com"+page
    print(next_page_c)
    url = page
    response = requests.get(url)
    soup = bs(response.content , "lxml")
    break
