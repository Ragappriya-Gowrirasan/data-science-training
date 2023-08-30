# import library packages
# http request library_requests
import requests
from bs4 import BeautifulSoup

# open url link of website
url = "https://www.webmd.com/search/search_results/default.aspx?query=atorvastatin"
response = requests.get(url).content
#text read using beatufulsoup
b = BeautifulSoup(response,"html.parser") 
table =b.find_all("div",{"class":"main-container main-container-2"})
print(table)