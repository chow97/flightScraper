from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

url = 'https://www.kayak.com/flights/KUL-SEA/2021-02-01?sort=bestflight_a&fs=airlines=~NH'

driver.get(url)

