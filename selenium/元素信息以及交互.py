from selenium import webdriver
from selenium.webdriver.common.by import By
import time

path = "chromedriver.exe"
browser = webdriver.Chrome(path)
url = "https://www.baidu.com/"
browser.get(url)
input = browser.find_element(by=By.ID, value='kw')
input.send_keys('周杰伦')
time.sleep(2)
button = browser.find_element(by=By.ID, value='su')
button.click()
time.sleep(2)
js_bottom = 'document.documentElement.scrollTop=10000'
browser.execute_script(js_bottom)
time.sleep(2)
next = browser.find_element(by=By.XPATH, value='//a[@class="n"]')
next.click()
time.sleep(2)
browser.back()
time.sleep(2)
browser.forward()
time.sleep(2)
browser.quit()
