import time
import json
import datetime
from module import *
from bs4 import BeautifulSoup

# Initialize the WebDriver
#ake sure to specify the correct WebDriver for your browser

# Open the Zomato URL
url = "https://results.eci.gov.in/PcResultGenJune2024/index.htm"  # Replace with the actual URL
driver.get(url)
time.sleep(5)
# Find the table
table = driver.find_element(By.TAG_NAME, "table")

# Extract headers
headers = [header.text.strip() for header in table.find_elements(By.TAG_NAME, "th")]

# Extract rows
data = []
rows = table.find_elements(By.TAG_NAME, "tr")[1:-1]  # Skip the header and footer rows

for row in rows:
    cols = row.find_elements(By.TAG_NAME, "td")
    if len(cols) == 0:  # Skip empty rows
        continue
    row_data = {headers[i]: cols[i].text.strip() for i in range(len(cols))}
    data.append(row_data)

# Save to JSON
with open('election_results.json', 'w') as f:
    json.dump(data, f, indent=4)

print("Data has been saved to election_results.json")

# Close the browser
driver.quit()