import time

import driver as driver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.facebook.com/")
    form = driver.find_element(By.TAG_NAME, "form")
    print("form States:", form.is_displayed(), form.is_enabled())
    submit_button = form.find_element(By.TAG_NAME, "button")
    print("Submit Button Status:", submit_button.is_displayed(), submit_button.is_enabled())


if __name__ == "__main__":
    main()