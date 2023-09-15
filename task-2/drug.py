#HTTP request 
import requests
from bs4 import BeautifulSoup
# CSV file open import
import pandas as pd

# Send an HTTP request and get the page content
url = "https://reviews.webmd.com/drugs/drugreview-841-atorvastatin-oral"
response = requests.get(url)

if response.status_code == 200:
    page_content = response.text
else:
    print("Failed to retrieve the web page. Status code:", response.status_code)
    exit()

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(page_content, 'html.parser')

# Extract data from the web page
reviews = []
ratings = []

for review in soup.find_all("div", class_="shared-reviews-container"):
    # Extract review text
    review_text = review.find("div", class_="review-details")
    if review_text:
        reviews.append(review_text.text.strip())
    else:
        reviews.append("N/A")

    # Extract rating
    rating = review.find("div", class_="overall-rating.name")
    if rating:
        ratings.append(rating.text.strip())
    else:
        ratings.append("N/A")

# Create a DataFrame
data = {"Review": reviews, "Rating": ratings}
data_f = pd.DataFrame(data)

# Export data to a CSV file
data_f.to_csv("webmd_reviews.csv", index=False)






