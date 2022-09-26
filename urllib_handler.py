import urllib.request
import urllib.parse

data = {
    "wd": "ip",
}

# url = "https://www.baidu.com/s?" + urllib.parse.urlencode(data)

url = "https://2022.ip138.com/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
}

# 因为参数顺序问题不能直接写url，headers，中间还有data，所以用关键字传参
request = urllib.request.Request(url=url, headers=headers)

proxies = {
    'https': '117.157.197.18:3128'
}
handler = urllib.request.ProxyHandler(proxies=proxies)

opener = urllib.request.build_opener(handler)

response = opener.open(request)

content = response.read().decode("utf-8")

print(content)
with open("text.html", "w", encoding="utf-8") as fp:
    fp.write(content)
