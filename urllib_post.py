import urllib.request
import urllib.parse
import json

data = {
    "kw": "test"
}
url = "https://fanyi.baidu.com/sug?"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 "
                  "Safari/537.36 "
}
# data = urllib.parse.urlencode(data).encode("utf-8")
# 因为参数顺序问题不能直接写url，headers，中间还有data，所以用关键字传参  post请求参数必须编码
request = urllib.request.Request(url=url, data=urllib.parse.urlencode(data).encode("utf-8"), headers=headers)
# 模拟浏览器发送请求
response = urllib.request.urlopen(request)

content = response.read().decode("utf-8")
content = json.loads(content)
print(content)

# post请求参数必须编码

