# Using the chrome browser navigate to https://www.facebook.com/fill in the email/phone and password text box
# then click the Login Button.


import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def send_key_to_element(element, keys):
    element.send_keys(keys)


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.facebook.com/")
    send_key_to_element(driver.find_element(By.NAME, "email"), "08028379112")
    send_key_to_element(driver.find_element(By.NAME, "pass"), "estherjane")
    driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button').click()
    # driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(10)


if __name__ == '__main__':
    main()
