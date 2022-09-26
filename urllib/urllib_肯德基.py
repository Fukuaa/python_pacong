#   http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname
import urllib.request
import urllib.parse


def create_request(page):
    data = {
        'cname': '深圳',
        'pid': '',
        'pageIndex': page,
        'pageSize': '10'
    }
    data = urllib.parse.urlencode(data).encode("utf-8")
    url = "http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/105.0.0.0 Safari/537.36 "
    }
    print(url)
    # 因为参数顺序问题不能直接写url，headers，中间还有data，所以用关键字传参
    request = urllib.request.Request(url=url, headers=headers,data=data)
    return request


def get_content(request):
    # 模拟浏览器发送请求
    response = urllib.request.urlopen(request)
    content = response.read().decode("utf-8")
    return content


def down_load(page, content):
    with open("肯德基地址" + str(page) + ".json", "w", encoding="utf-8") as fp:
        fp.write(content)


start_page = int(input("请输入起始页"))
end_page = int(input("请输入结束页"))
for page in range(start_page, end_page + 1):
    down_load(page, get_content(create_request(page)))
    # create_request(page)
