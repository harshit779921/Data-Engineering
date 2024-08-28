from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

# Query and URL for Amazon search
query = "laptop"
file = 0

# Ensure the 'data' directory exists
if not os.path.exists("data"):
    os.makedirs("data")

# Loop to iterate over multiple pages
for i in range(1, 20):
    driver.get(f"https://www.amazon.in/s?k={query}&page={i}")

    # Use find_elements to get a list of all matching elements
    elems = driver.find_elements(By.CLASS_NAME, "puis-card-container")

    # Print the number of items found
    print(f"{len(elems)} items found")

    # Iterate over each element and save its HTML content to a file
    for elem in elems:
        outer_html = elem.get_attribute("outerHTML")
        with open(f"data/{query}_{file}.html", "w", encoding="utf-8") as f:
            f.write(outer_html)
        file += 1

    # Introduce a delay before going to the next page
    time.sleep(2)

# Close the browser after the loop is complete
driver.close()
