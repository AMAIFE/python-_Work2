# Using the firefox browser navigate to https //www.google.com / # enter the text Python in the search box, then send the Enter key. # Get the Text from the Wikipedia brief on the right side and print the value in the console. import time from selenium import webdriver from selenium.webdriver im…
# Using the firefox browser navigate to https //www.google.com /# enter the text Python in the search box, then send the Enter key.

# Get the Text from the Wikipedia brief on the right side and print the value in the console.

import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


def send_keys_to_element(element, keys):
    element.send_keys(keys)


def main():
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    driver.get("https://www.google.com/")
    send_keys_to_element(driver.find_element(By.TAG_NAME, "input"), "python")
    send_keys_to_element(driver.find_element(By.TAG_NAME, "input"), Keys.ENTER)
    time.sleep(5)
    python_text = driver.find_element(By.XPATH, '//div[@data-attrid="description"]')
    print(python_text.text)


if __name__ == '__main__':
    main()