from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

url = 'https://www.kayak.com/flights/KUL-SEA/2021-02-01?sort=bestflight_a&fs=airlines=~NH'

#url = 'https://the-internet.herokuapp.com/key_presses'

driver.get(url)
time.sleep(3)

webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
