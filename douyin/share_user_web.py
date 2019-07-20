# _*_ coding: utf-8 _*_
__author__ = "吴飞鸿"
__date__ = "2019/7/20 21:04"

import re

import requests
from lxml import etree


def handle_decode(input_data):
    # 抖音数字破解
    regex_list = [
        {"name": [" &#xe603; ", " &#xe60d; ", " &#xe616; "], "value": 0},
        {"name": [" &#xe602; ", " &#xe60e; ", " &#xe618; "], "value": 1},
        {"name": [" &#xe605; ", " &#xe610; ", " &#xe617; "], "value": 2},
        {"name": [" &#xe604; ", " &#xe611; ", " &#xe61a; "], "value": 3},
        {"name": [" &#xe606; ", " &#xe60c; ", " &#xe619; "], "value": 4},
        {"name": [" &#xe607; ", " &#xe60f; ", " &#xe61b; "], "value": 5},
        {"name": [" &#xe608; ", " &#xe612; ", " &#xe61f; "], "value": 6},
        {"name": [" &#xe60a; ", " &#xe613; ", " &#xe61c; "], "value": 7},
        {"name": [" &#xe60b; ", " &#xe614; ", " &#xe61d; "], "value": 8},
        {"name": [" &#xe609; ", " &#xe615; ", " &#xe61e; "], "value": 9},
    ]
    # 替换密文成明文
    for i in regex_list:
        for j in i["name"]:
            input_data = re.sub(j, str(i["value"]), input_data)

    response_html = etree.HTML(input_data)
    user_info = {}
    user_info["nickname"] = response_html.xpath("//p[@class='nickname']/text()")[0]
    douyin_id_abc = response_html.xpath("//p[@class='shortid']/text()")[0].replace("抖音ID：", "").replace(" ", "")
    douyin_id_123 = "".join(response_html.xpath("//p[@class='shortid']/i/text()"))
    user_info["douyin_id"] = douyin_id_abc + douyin_id_123

    user_info["signature"] = response_html.xpath("//p[@class='signature']/text()")
    user_info["focus"] = "".join(response_html.xpath("//p[@class='follow-info']/span[1]/span[@class='num']/i/text()"))
    # 粉丝数量
    user_info["follower"] = "".join(response_html.xpath("//p[@class='follow-info']/span[2]/span[@class='num']/i/text()"))
    if 'w ' in response_html.xpath("//p[@class='follow-info']/span[2]/span[@class='num']/text()"):
        user_info["follower"] = str(int(user_info["follower"]) / 10) + "w"
    # 获得赞数量
    user_info["liked"] = "".join(response_html.xpath("//p[@class='follow-info']/span[3]/span[@class='num']/i/text()"))
    if 'w ' in response_html.xpath("//p[@class='follow-info']/span[3]/span[@class='num']/text()"):
        user_info["liked"] = str(int(user_info["liked"]) / 10) + 'w'
    print(user_info)

def handle_share_user_web():
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
    }
    url = "https://www.iesdouyin.com/share/user/51483050122"

    response = requests.get(url=url, headers=headers)
    # print(response.text)
    handle_decode(response.text)

if __name__ == '__main__':
    handle_share_user_web()
