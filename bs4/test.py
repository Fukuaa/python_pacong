from bs4 import BeautifulSoup
import urllib.request
import urllib.parse

# //ul[@class="grid padded-3 product"]//strong/text()
url = "https://www.starbucks.com.cn/menu/"
response = urllib.request.urlopen(url)
content = response.read().decode("utf-8")
soup = BeautifulSoup(content, "lxml")
name_list = soup.select('ul[class="grid padded-3 product"] strong')
for name in name_list:
    print(name.get_text())
