import time
import json
import datetime
from module import *
from bs4 import BeautifulSoup

# Initialize the WebDriver
#ake sure to specify the correct WebDriver for your browser

# Open the URL
url = "https://results.eci.gov.in/"  # Replace with the actual URL
driver.get(url)
time.sleep(5)
data = []

# Extract data from the first state item
parliamentary = driver.find_element(By.CSS_SELECTOR, ".state-item.blue-bg")
parliamentary_data = {
    "title": parliamentary.find_element(By.TAG_NAME, "h2").text,
    "count": parliamentary.find_element(By.TAG_NAME, "h1").text,
    "link": parliamentary.find_element(By.TAG_NAME, "a").get_attribute("href")
}
data.append(parliamentary_data)

# Extract data from the assembly constituencies
assembly_items = driver.find_elements(By.CSS_SELECTOR, ".state-item.olive-bg, .state-item.pine-bg, .state-item.gry-bg")

for item in assembly_items:
    item_data = {
        "state": item.find_element(By.TAG_NAME, "h2").text,
        "count": item.find_element(By.TAG_NAME, "h1").text,
        "type": item.find_element(By.TAG_NAME, "h5").text,
        "link": item.find_element(By.TAG_NAME, "a").get_attribute("href")
    }
    data.append(item_data)

# Extract data from the bottom links
bottom_links = driver.find_elements(By.CSS_SELECTOR, ".btn.btn-big.btn-primary")

for link in bottom_links:
    link_data = {
        "state": link.text,
        "link": link.get_attribute("href")
    }
    data.append(link_data)

# Save to JSON
with open('election_data_page1.json', 'w') as f:
    json.dump(data, f, indent=4)

print("Data has been saved to election_data.json")

# Close the browser
driver.quit()