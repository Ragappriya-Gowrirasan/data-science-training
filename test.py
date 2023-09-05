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
for test in soup.findAll("div" , class_="review-details"):
   tests = test.find("strong" , class_="condition")
   condition.append(tests)

# reviews

reviews = []

for rev in soup.findAll("div" , class_="overall-rating"):
   print(rev)
   break
   r = rev.find("strong")
   reviews.append(r.text)
   res = r.text

print(reviews)

lists = {'condition':condition,'rating':reviews}
# list1 = pd.DataFrame(lists)
# list1.to_csv("drug.csv")
