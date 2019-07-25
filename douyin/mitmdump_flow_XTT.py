# _*_ coding: utf-8 _*_
__author__ = "吴飞鸿"
__date__ = "2019/7/25 17:01"

import json
import re

import pymongo
from pymongo.collection import Collection


def response(flow):
    """
        截获处理数据流。
        # 进入python 环境
        # mitmdump -s <.py> -p <端口> 运行截获需要的response
    """

    if 'ixigua.com/' in flow.request.url:
        file_name = re.match('.*ixigua\.com/([a-z0-9]+)/.*', flow.request.url).group(1)
        with open('douyin_videos_XTT/{0}.mp4'.format(file_name), 'wb') as f:
            f.write(flow.response.content)
        print('OK!!!!!!!!!')