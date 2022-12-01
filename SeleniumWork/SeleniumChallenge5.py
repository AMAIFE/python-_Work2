# Using any browser navigate to any youtube video of your choice,
# allow your script to wait for the comments to load then get the first two comments, and print them in the terminal

import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec


def main():
    driver = webdriver.Chrome(service=(Service(ChromeDriverManager().install())))
    driver.get('https://www.youtube.com/watch?v=W38OustZ-Ds')
    time.sleep(5)
    youtube_play_button = driver.find_element(By.XPATH, '//*[@id="movie_player"]/div[28]/div[2]/div[1]/button')
    youtube_play_button.click()
    time.sleep(5)
    first_comment = driver.find_element(By.XPATH, '//*[@id="content-text"]')
    print("First Comment:", first_comment, first_comment.text)
    time.sleep(5)
    second_comment = driver.find_element(By.XPATH, '//*[@id="content-text"]/span[1]')
    print("Second Comment:", second_comment, second_comment.text)
    time.sleep(5)


if __name__ == '__main__':
    main()