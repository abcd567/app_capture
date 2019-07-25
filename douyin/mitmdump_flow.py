# _*_ coding: utf-8 _*_
__author__ = "吴飞鸿"
__date__ = "2019/7/21 20:43"

import json

import pymongo
from pymongo.collection import Collection

# from .handle_mongo import save_task


def response(flow):
    """
        截获处理数据流。
        # 进入python 环境
        # mitmdump -s <.py> -p <端口> 运行截获需要的response
    """
    # if 'aweme/v1/user/following/list/' in flow.request.url:
        # with open('user.txt', 'w') as f:
            # f.write(flow.response.test)

    if 'aweme/v1/user/follower/list/' in flow.request.url:
        client = pymongo.MongoClient(host='127.0.0.1', port=27017)
        db = client['douyin']
        task_collections = Collection(db, 'douyin_task')
        for user in json.loads(flow.response.text)['followers']:
            user_info = {}
            user_info['douyin_id'] = user['unique_id']
            user_info['uid'] = user['uid']
            user_info['nickname'] = user['nickname']
            print(user_info)
            task_collections.update_one({'uid': user_info['uid']}, {"$set": user_info}, True)
        print('OK!!!!!!!!!')
