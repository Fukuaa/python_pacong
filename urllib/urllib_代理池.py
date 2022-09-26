import urllib.request
import urllib.parse
import random
data = {
    "wd": "本机ip地址查询",
}
url = "https://www.baidu.com/s?" + urllib.parse.urlencode(data)
#url = "https://2022.ip138.com/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 "
                  "Safari/537.36 "
}

# 因为参数顺序问题不能直接写url，headers，中间还有data，所以用关键字传参

proxiepool = [
    {'http': '121.13.252.61:41564'},
    {'http': '114.67.104.36:18888'},
    {'http': '14.187.165.54:19132'},
    {'http': '117.54.114.101:80'},
    {'http': '117.54.114.99:80'}
]
for i in range(1,5):
    request = urllib.request.Request(url=url, headers=headers)
    proxies = random.choice(proxiepool)
    handler = urllib.request.ProxyHandler(proxies=proxies)
    opener = urllib.request.build_opener(handler)
    response = opener.open(request)
    content = response.read().decode("utf-8")
    print(content)
    with open(str(i)+"text.html", "w", encoding="utf-8") as fp:
        fp.write(content)
