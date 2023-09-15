import requests
from bs4 import BeautifulSoup

# Define the URL pattern
base_url = "https://reviews.webmd.com/drugs/drugreview-841-atorvastatin-oral?conditionid=&sortval=1&page={}&next_page=true"

# Number of pages to scrape (change as needed)
num_pages_to_scrape = 5

# Loop through the specified number of pages
for page_num in range(1, num_pages_to_scrape + 1):
    # Construct the URL for the current page
    url = base_url.format(page_num)

    # Send a GET request to the current page
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract and print the review details (you can modify this part to store the data)
        review_details = soup.find_all('div', class_='review-details')
        for detail in review_details:
            print(detail.get_text())

    else:
        print(f"Failed to retrieve page {page_num}")

    # You can add a delay here to be polite to the website (e.g., time.sleep(seconds))

# End of the loop
files = pd.DataFrame(file)
files.to_csv('drug.csv')
print(files)
