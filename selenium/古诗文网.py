import requests
from bs4 import BeautifulSoup
import urllib.request

url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/98.0.4758.102 Safari/537.36 "
}
response = requests.get(url=url, headers=headers)

content = response.text

# print(content)

soup = BeautifulSoup(content, 'lxml')

VIEWSTATE = soup.select('#__VIEWSTATE')[0].attrs.get('value')

VIEWSTATEGENERATOR = soup.select('#__VIEWSTATEGENERATOR')[0].attrs.get('value')

code = soup.select('#imgCode')[0].attrs.get('src')

code_url = 'https://so.gushiwen.cn' + code

# urllib.request.urlretrieve(url=code_url, filename='code.jpg')
session = requests.session()
response_code = session.get(code_url)
content_code = response_code.content
with open('code.jpg', 'wb') as fp:
    fp.write(content_code)
code_name = input('请输入你的验证码')

url_post = 'https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx'

data_post = {
    '__VIEWSTATE': VIEWSTATE,
    '__VIEWSTATEGENERATOR': VIEWSTATEGENERATOR,
    'from': 'http://so.gushiwen.cn/user/collect.aspx',
    'email': '18138424985',
    'pwd': '123456',
    'code': code_name,
    'denglu': '登录',
}
response_post = session.post(url=url_post, headers=headers, data=data_post)
content_post = response_post.text
with open('gushiwegn.html', 'w', encoding='utf-8') as fp:
    fp.write(content_post)
