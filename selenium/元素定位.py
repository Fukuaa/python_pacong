from selenium import webdriver
from selenium.webdriver.common.by import By

path = "chromedriver.exe"
browser = webdriver.Chrome(path)
url = "https://www.baidu.com/"
browser.get(url)
button = browser.find_element(by=By.ID, value='su')
print(button)
