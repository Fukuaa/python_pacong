import urllib.request
import urllib.parse
from lxml import etree

# https://dianying.taobao.com/cityAction.json?activityId&_ksTS=1665210577667_108&jsoncallback=jsonp109&action=cityAction&n_s=new&event_submit_doGetAllRegion=true
url = "https://dianying.taobao.com/cityAction.json?activityId&_ksTS=1665210577667_108&jsoncallback=jsonp109&action" \
      "=cityAction&n_s=new&event_submit_doGetAllRegion=true "
headers = {
    'content-encoding': 'gzip',
    'content-language': 'zh-CN',
    'content-type': 'text/html;charset=UTF-8',
    'date': 'Sat, 08 Oct 2022 06:29:37 GMT',
    'eagleeye-traceid': '212b9cb916652105776665097edb37',
    's': 'STATUS_NOT_EXISTED',
    'server': 'Tengine/Aserver',
    'strict-transport-security': 'max-age=31536000',
    'timing-allow-origin': '*',
    'vary': 'Accept-Encoding',
    # ':authority': 'dianying.taobao.com',
    # ':method': 'GET',
    # ':path': '/cityAction.json?activityId&_ksTS=1665210577667_108&jsoncallback=jsonp109&action=cityAction&n_s=new'
    #         '&event_submit_doGetAllRegion=true',
    # ':scheme': 'https',
    'accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, '
              '*/*; q=0.01',
    # 'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'bx-v': '2.2.3',
    'cookie': 't=c8ecd4dd99312397d405fd59ba30266c; cna=gMdOGwYiWHgCAXF2u8ruAEW2; '
              'cookie2=12ab1c055f7bdf76fe903815ff7eb377; v=0; _tb_token_=ee5535e76a35f; xlly_s=1; '
              'tfstk=cY1dBRYtzlq3hBZk_BeM4x1EyXacZ3uyVzxxw_0FyD94xhcRigCcM2FqEE-2vPC..; '
              'l=eBPZ0NAnT_l2xTQNBOfZnurza77T_IRAguPzaNbMiOCP9gCH5a0AW6PbCJLMCnGVhsfWR3rp2umHBeYBqn4jjqj4axom4qDmn; '
              'isg=BHp6krrQzbS4zkGrxESIvXyfy6CcK_4FYScmpYRzPI3YdxqxbLuJFceBxwOrZ3ad',
    'referer': 'https://dianying.taobao.com/',
    'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/106.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest'
}
request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode("utf-8")
content = content.split("(")[1].split(")")[0]
with open("淘票票.json", "w", encoding="utf-8") as fp:
    fp.write(content)
import json
import jsonpath

obj = json.load(open("淘票票.json", "r", encoding="utf-8"))
city_list = jsonpath.jsonpath(obj, "$..regionName")
print(city_list)
