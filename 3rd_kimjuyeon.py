from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from time import sleep

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(5)
driver.get('https://www.naver.com/')

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

driver.find_element(By.ID, 'query').click()
driver.find_element(By.ID, 'query').send_keys("삼쩜삼" + Keys.ENTER)
driver.find_element(By.LINK_TEXT, '뉴스').click()
sleep(5)