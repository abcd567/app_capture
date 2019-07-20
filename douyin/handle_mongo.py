import pymongo
from pymongo.collection import Collection


client = pymongo.MongoClient(host='127.0.0.1', port=27017)
db = client['douyin']


# def handle_init_task():
#     task_id_collection = Collection(db, "task_id")
#     with open("douyin_hot_id", r) as f_share:
#         for f_share_task in f_share.readline():
#             init_task = {}
#             init_task["share_id"] = f_share_task.replace("\n", "")
#             task_id_collection.insert(init_task)
#
#
# def handle_get_task():
#     task_id_collection = Collection(db, "task_id")
#     return task_id_collection.find_one_and_delete({})


def send_task():
    with open('douyin_hot_id.txt', 'r') as f:
        f_read = f.readlines()
        for i in f_read:
            task_info = {}
            task_info['share_id'] = i.replace('\n', '')
            task_info['task_type'] = 'share_id'
            print('当前保存的task为%s:' % task_info)
            # 保存到数据库
            save_task(task_info)


def save_task(task):
    """
        更新，不存在则插入
    """
    task_collections = Collection(db, 'douyin_task')
    task_collections.update({'share_id': task['share_id']}, task, True)


def get_task(task_type):
    """
        从数据库取一条并删除
    """
    task_collections = Collection(db, 'douyin_task')
    task = task_collections.find_one_and_delete({'task_type': task_type})
    return task


def delete_task(task):
    pass


def save_data(item):
    """
        原始插入数据， 已被save_task()代替
    """
    data_collections = Collection(db, 'douyin_data')
    data_collections.insert(item)
