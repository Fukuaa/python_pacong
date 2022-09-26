import urllib.request

url = "https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=0&limit=20"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 "
                  "Safari/537.36 "
}
# 因为参数顺序问题不能直接写url，headers，中间还有data，所以用关键字传参
request = urllib.request.Request(url=url, headers=headers)
# 模拟浏览器发送请求
response = urllib.request.urlopen(request)

content = response.read().decode("utf-8")

print(content)
fp = open("douban.json", "w", encoding="utf-8")
fp.write(content)
