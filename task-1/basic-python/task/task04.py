import requests
from bs4 import BeautifulSoup

# access the https request

search = "website"
url = f"https:/www.google.com/search?&q={search}"
response = requests.get(url)
soup = BeautifulSoup(response.text)

 