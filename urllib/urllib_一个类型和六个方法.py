import urllib.request

url = "https://img2.baidu.com/it/u=3744598050,4191464688&fm=253&fmt=auto&app=138&f=JPEG?w=800&h=500";
urllib.request.urlretrieve(url, "text.jpg")
