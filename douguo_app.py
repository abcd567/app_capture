# _*_ coding:utf-8 _*_

__author__ = "吴飞鸿"
__date__ = "2019/7/14 20:12"

import requests
import json
import time
from multiprocessing import Queue


queue_list = Queue()

# 处理请求
def handle_request(url, data):
    # 伪装请求头
    header = {
        "client":"4",
        "version":"6942.6",
        "device":"SM-G955F",
        "sdk":"25,7.1.2",
        "imei":"355757010762041",
        "channel":"oppo",
        # "mac":"4C:CC:6A:8E:FB:64",
        "resolution":"1280*720",
        "dpi":"1.5",
        # "android-id":"4ccc6a8efb647084",
        # "pseudo-id":"a8efb6470844ccc6",
        "brand":"samsung",
        "scale":"1.5",
        "timezone":"28800",
        "language":"zh",
        "cns":"3",
        "carrier":"CHINA+MOBILE",
        # "imsi":"460077620410614",
        "User-Agent":"Mozilla/5.0 (Linux; Android 7.1.2; SM-G955F Build/JLS36C; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.100 Mobile Safari/537.36",
        "act-code":"8f3b1bf1206314031aed282785356aca",
        "act-timestamp":"1563100093",
        "uuid":"6ebb1f88-bd1e-4aba-928c-3672d62deb8b",
        "newbie":"1",
        "reach":"10000",
        "Content-Type":"application/x-www-form-urlencoded; charset=utf-8",
        "Accept-Encoding":"gzip, deflate",
        "Connection":"Keep-Alive",
        # "Cookie":"duid=60470696",
        "Host":"api.douguo.net",
        # "Content-Length":"68"
    }
    # 发起请求,并返回结果
    response = requests.post(url=url, data=data, headers=header)
    return response


def handle_index():
    url = 'http://api.douguo.net/recipe/flatcatalogs'
    data = {
        "client":",",
        # "_session":"563100941637355757010762041",
        "v":"503650468,",
        "_vs":"305"
    }
    response = handle_request(url, data)
    index_dict = json.loads(response.content.decode("unicode_escape"))
    for index_item in index_dict['result']['cs']:
        for index_item_1 in index_item['cs']:
            for index_item_2 in index_item_1['cs']:
                data_2 = {
                    "client": "4",
                    # "_session": "563100941637355757010762041",
                    "keyword": index_item_2["name"],
                    "order": "3",
                    "_vs": "400",
                    "type": "0"
                }
                # # 测试
                # url_api = "http://api.douguo.net/recipe/v2/search/0/20"
                # response = handle_request(url=url_api, data=data_2)
                # time.sleep(2)
                # print(response.content.decode("unicode_escape"))
                # print()
                queue_list.put(data_2)


def handle_menu_list(data):
    print("当前处理食材：", data["keyword"])
    # 前20条数据api
    url = "http://api.douguo.net/recipe/v2/search/0/20"
    menus_response = handle_request(url=url, data=data)
    # print(menus_response.content.decode("unicode_escape"))
    menus_dict = json.loads(menus_response.text)
    for menu_dict in menus_dict["result"]["list"]:
        menu_info = {}
        menu_info["食材"] = data["keyword"]
        if menu_dict["type"] == 13:
            menu_info["author_name"] = menu_dict['r']['an']
            menu_info["id"] = menu_dict['r']['id']
            # 菜式描述，可能为空
            menu_info["story"] = menu_dict['r']['cookstory'].replace(" ", "")
            menu_info["name"] = menu_dict['r']['n']
            # 主料
            menu_info["major"] = menu_dict['r']['major']
            # 多少人做过
            menu_info["recommendation_tag"] = menu_dict['r']['recommendation_tag']
            print(menu_info)
        else:
            continue

if __name__ == '__main__':
    handle_index()
    print(queue_list.qsize())
    handle_menu_list(queue_list.get())