import urllib.request
import urllib.parse
import json

data = {
    "from": "zh",
    "to": "en",
    "query": "测试",
    "simple_means_flag": "3",
    "sign": "706553.926920",
    "token": "ccabd3bfecbb49d2a6d2deaa8a9012e4",
    "domain": "common"
}
url = "https://fanyi.baidu.com/v2transapi?from=en&to=zh?"
headers = {
    'Accept': '*/*',
    #'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Acs-Token': '1663830232305_1663834964513_cy9zHscQaXJY6OzESuNbQXoaBtUlxb6CT1Ts8j0TXsigi7WNpKE6/kEWevj8ngPgcWmuON0tMLbxaVGagpSwZCrKOrpBXB+9Ui29UsW4yjA5Q8akuAP35lOk/H530D5TTFSt5jQi071RmCq8rpHXDihzdNuXwTH1w02/UrxZBtmqbtxbwkHIQc//a6WJ4zIqHZiMXk8x2M3750OKDRkSkDEhPACwxvwIh+NImeyIxY0TfPaxIfefHgrSjfKAT0KYXHA1WNdNqFKQrRuu5zOE5acN+uQG0QIMLBRRmk8ggdWjuBLdoOpz/K6Xw1iaQ3CE5Otxaz0wiazo21MhRkaHQFdI+OdrjkICGeIGVeCHqu8=',
    'Connection': 'keep-alive',
    'Content-Length': '130',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'BIDUPSID=488DDADED467BC564BE0D58C966BFEB5; PSTM=1632976872; __yjs_duid=1_44642cca51cbae6e9c0ca9d0f071743d1632976944133; BAIDUID=44FEFBD5F24D4908C2222B0A1E79856C:FG=1; APPGUIDE_10_0_2=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; SOUND_SPD_SWITCH=1; HISTORY_SWITCH=1; SOUND_PREFER_SWITCH=1; BDUSS=mhiaFlyc3lVYWJsbll6dzM0MWQtUDZrdzJ5dUJxWGw0bmhtLXEwbkY5UlVHRFJqSVFBQUFBJCQAAAAAAAAAAAEAAADJxgtfYb34u~e1xERPVEEyAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFSLDGNUiwxjS; BDUSS_BFESS=mhiaFlyc3lVYWJsbll6dzM0MWQtUDZrdzJ5dUJxWGw0bmhtLXEwbkY5UlVHRFJqSVFBQUFBJCQAAAAAAAAAAAEAAADJxgtfYb34u~e1xERPVEEyAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFSLDGNUiwxjS; ZFY=hFT6BaA6cNWciNbw7CQXSHDeq5z:BD1IaXDLIsMNQCRM:C; BAIDUID_BFESS=44FEFBD5F24D4908C2222B0A1E79856C:FG=1; RT="sl=0&ss=l8a0iv5j&tt=0&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&z=1&dm=baidu.com&si=5g88fx7jdv6&ul=8au9&hd=8avr"; BA_HECTOR=0l842k202400a50l258kpi5d1hilnlt19; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1662692895,1662708794,1663121187,1663834938; ab_sr=1.0.1_MDUwMTM1MWEyNTZhOTkyYjc2MjllZTVjMTFiNmJhYTAyYTdmYmI4ZjZhYjkzODk1ZjFmZjI4NDJlOWEwN2MxN2RlMjBkZmVhZTVhMDNkMzEyNDY0MGUzOTlmMDlhMWI2MTAyYzU4Y2RlMjgyM2I0ZWNhNmI3OGJhYTg5YjgxOGJhNjNkYzQ0ZTE4OGNhNTQyODI2NTBkZDg2ZDZkYjBkNWNiNjhjM2E5MjU0Nzk3YzExY2Q4NjgzNGIzZGVkYTkz; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1663834964',
    'Host': 'fanyi.baidu.com',
    'Origin': 'https://fanyi.baidu.com',
    'Referer': 'https://fanyi.baidu.com/?aldtype=16047',
    'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
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
