import urllib.request

url = "http://www.baidu.com/"
# 模拟浏览器发送请求
response = urllib.request.urlopen(url)

content = response.read().decode("utf-8")

print(content)
