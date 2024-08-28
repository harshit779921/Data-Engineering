from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

# Query and URL for Amazon search
query = "laptop"

for i in range(1, 20):
    driver.get(f"https://www.amazon.in/s?k={query}&page={i}")

    # Use find_elements to get a list of all matching elements
    elems = driver.find_elements(By.CLASS_NAME, "puis-card-container")

    # Print the number of items found
    print(f"{len(elems)} items found")

    # Iterate over each element and print its text content
    for elem in elems:
        print(elem.text)

    # Introduce a delay before closing the browser
    time.sleep(2)

    # Close the browser
    driver.close()
