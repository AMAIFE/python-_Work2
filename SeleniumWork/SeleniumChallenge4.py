# Navigate to https://www.bbc.com/ and print out the top 10 latest news from the homepage

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.bbc.com/")
    news_one = driver.find_element(By.XPATH, '//*[@id="page"]/section[3]/div/ul/li[1]/div/a')
    print("News One : ", news_one.text)
    news_two = driver.find_element(By.XPATH, '//*[@id="page"]/section[3]/div/ul/li[3]')
    print("News Two : ", news_two.text)
    news_three = driver.find_element(By.XPATH, '//*[@id="page"]/section[3]/div/ul/li[3]')
    print("News Three : ", news_three.text)
    news_four = driver.find_element(By.XPATH, '//*[@id="page"]/section[3]/div/ul/li[4]')
    print("News Four : ", news_four.text)
    news_five = driver.find_element(By.XPATH, '//*[@id="page"]/section[3]/div/ul/li[5]')
    print("News Five: ", news_five.text)
    news_six = driver.find_element(By.XPATH, '//*[@id="page"]/section[4]/div/div/div[2]/div/section[2]/div/ul/li[1]/div/a')
    print("News Six : ", news_six.text)
    news_seven = driver.find_element(By.XPATH, '//*[@id="page"]/section[4]/div/div/div[2]/div/section[2]/div/ul/li[2]')
    print(" News Seven : ", news_seven.text)
    news_eight = driver.find_element(By.XPATH, '//*[@id="page"]/section[4]/div/div/div[2]/div/section[2]/div/ul/li[3]')
    print("News Eight : ", news_eight.text)
    news_nine = driver.find_element(By.XPATH, '//*[@id="page"]/section[6]/div/ul/li[1]/div/a')
    print("News Nine : ", news_nine.text)
    news_ten = driver.find_element(By.XPATH, '//*[@id="page"]/section[6]/div/ul/li[2]')
    print("News Ten : ", news_ten.text)


if __name__ == '__main__':
    main()