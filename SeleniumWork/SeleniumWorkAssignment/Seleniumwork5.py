import time
from POMTask4 import TestAutomation
from POMTask5 import SwitchToSoftware
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    test_automation_simplified = TestAutomation(driver)
    print(test_automation_simplified.title.text)
    switch_to_software = SwitchToSoftware(driver)
    print(switch_to_software.title.text)
    
    
if __name__ == "__main__":
    main()