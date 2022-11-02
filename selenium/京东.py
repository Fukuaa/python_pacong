from selenium import webdriver
path = "chromedriver.exe"
browser = webdriver.Chrome(path)
url = "https://www.jd.com/"
browser.get(url)
content = browser.page_source
print(content)