from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


def locate_by_link_text(driver):
    explore_courses_link = driver.find_element, (By.LINK_TEXT, "EXPLORE COURSES")
    print("EXPLORE COURSES link:", explore_courses_link)


def locate_by_partial_link_text(driver):
    subscribe_to_receive_link = driver.find_element, (By.PARTIAL_LINK_TEXT, "Subscribe_to_receive")
    print("Subscribe_to_receive_training_updates_from_testify link|Partial:", subscribe_to_receive_link)


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://academy.testifyltd.com/")
    locate_by_link_text(driver)
    locate_by_partial_link_text(driver)


if __name__ == "__main__":
    main()
