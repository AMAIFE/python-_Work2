# Navigate any browser to https://weather.com/ get the current  temperature  and  print  it  out  in  the  terminal.
# Then print out the temperature for Morning, Afternoon, Evening,and Overnight.


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.weather.com/")
    time.sleep(6)
    current_temp = driver.find_element(By.XPATH, '//*[@id="WxuCurrentConditions-main-b3094163-ef75-4558-8d9a-e35e6b9b1034"]/div/section/div/div[2]/div[1]/div[1]/span')
    print('Current Temperature: ', current_temp.text)
    morning_temp = driver.find_element(By.XPATH, '//*[@id="WxuTodayWeatherCard-main-486ce56c-74e0-4152-bd76-7aea8e98520a"]/section/div/ul/li[1]/a/div[1]/span')
    print('Morning Temperature: ', morning_temp.text)
    afternoon_temp = driver.find_element(By.XPATH, '//*[@id="WxuTodayWeatherCard-main-486ce56c-74e0-4152-bd76-7aea8e98520a"]/section/div/ul/li[2]/a/div[1]/span')
    print('Afternoon Temperature: ', afternoon_temp.text)
    evening_temp = driver.find_element(By.XPATH, '//*[@id="WxuTodayWeatherCard-main-486ce56c-74e0-4152-bd76-7aea8e98520a"]/section/div/ul/li[3]/a/div[1]/span')
    print('Evening Temperature: ', evening_temp.text)
    overnight_temp = driver.find_element(By.XPATH, '//*[@id="WxuTodayWeatherCard-main-486ce56c-74e0-4152-bd76-7aea8e98520a"]/section/div/ul/li[4]/a/div[1]/span')
    print('Overnight Temperature: ', overnight_temp.text)

    time.sleep(3)


if __name__ == '__main__':
    main()