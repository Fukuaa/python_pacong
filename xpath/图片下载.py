import urllib.request
import urllib.parse
from lxml import etree


def create_request(page):
    if page == 1:
        url = "https://sc.chinaz.com/tupian/caoyuantupian.html"
    else:
        url = "https://sc.chinaz.com/tupian/caoyuantupian_" + str(page) + ".html"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/105.0.0.0 Safari/537.36 "
    }
    print(url)
    # 因为参数顺序问题不能直接写url，headers，中间还有data，所以用关键字传参
    request = urllib.request.Request(url=url, headers=headers)
    return request


def get_content(request):
    # 模拟浏览器发送请求
    response = urllib.request.urlopen(request)
    content = response.read().decode("utf-8")
    return content


def down_load(content):
    tree = etree.HTML(content)
    name_list = tree.xpath('//a[@class="name"]/text()')
    # //img[@class="lazy"]/@src
    # //div[@class="item masonry-brick"]/img/@data-original
    img_list = tree.xpath('//img[@class="lazy"]/@data-original')
    # print(name_list)
    # print(img_list)
    # print(len(img_list))
    for i in range(len(name_list)):
        name = name_list[i]
        src = "https:" + img_list[i]
        # print(src)
        # print(name)
        urllib.request.urlretrieve(url=src, filename='E:\\img/' + name + '.jpg')


start_page = int(input("请输入起始页"))
end_page = int(input("请输入结束页"))
for page in range(start_page, end_page + 1):
    down_load(get_content(create_request(page)))
