import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


def print_element_attributes(element):
    print("Class", element.get_attribute("class"))
    print("ID", element.get_attribute("Id"))
    print("Style", element.get_attribute("style"))
    print("Inner Test", element.get_attribute("InnerText"))
    print("Inner HTML", element.get_attribute("InnerHTML"))


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://academy.testifyltd.com/")
    testify_limited_link: WebElement = driver.find_element(By.LINK_TEXT, "Testify")
    print_element_attributes(testify_limited_link)


if __name__ == "__main__":
    main()
