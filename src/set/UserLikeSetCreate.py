import mongo.Connect as connect
import mongo.FuncColle as fcc
import myutils.c_user as cua
import hashlib
import random
import uuid
import time as t


class UserLikeSetCreate(object):
    min = 1
    max = 678

    def __init__(self) -> None:
        self.count = 100
        # 数据库操作
        self.f = fcc.Colle()
        pass

    # 创建用户喜欢的音乐集合，其中包含了用户的id name song信息 最后是tags信息
    # 获取用户信息，并且只获取用户信息中id 和name ，忽略用户的密码
    # 随机获取歌曲表格中的随机首歌曲，对每个用户生成一个新的diction，
    # 并且生成与用户歌曲tag 列表，（暂定不需要描述tag）
    def makeUserLikeSet(self):
        print("[" + t.asctime(t.localtime()) + "]" +
              "Start make " + "userlike by song and songdetail and user")
        n = 0
        while True:

            # 从user表中获取用户
            docs_user = self.f.findDocument(
                collection_name="user",
                projection={'_id': 1, 'id': 1, 'name': 1}, limit=100, page=n)
            # 翻页
            n += 1
            # print(len(docs_user))
            # 循环每个用户并且随机获取歌曲生成歌曲信息表
            for user in docs_user:
                list_user_song = []
                # 从 songdetail 表中获取用户
                size = random.randint(self.min, self.max)
                query_list = [
                    {
                        '$sample': {
                            "size": size
                        }
                    },
                    {
                        '$lookup': {
                            "from": "song",        # 需要连接的表格（副表）
                            "localField": "id",    # 主表中的字段
                            "foreignField": "id",  # 副表的字段
                            "as": "union"          # 生成的新字段名
                        }

                    },
                    {
                        '$project': {
                            "_id": 0,
                            "id": 1,
                            "name": 1,
                            "union.tags": 1,
                        }
                    }
                ]
                docs_songs = self.f.aggregateDocument(
                    collection_name="songdetail",
                    querys=query_list)
                list_tags = self.changeDocsSongs(docs_songs=docs_songs)
                diction_user_song = {
                    "_id": user['_id'],
                    "id": user['id'],
                    "name": user['name'],
                    "songs": docs_songs,
                    "tags": list_tags,
                }
                list_user_song.append(diction_user_song)
                # 写入数据
                self.f.insertDocument(
                    0, docs=list_user_song, collection_name="like")
            if len(docs_user) <= 0:
                break
        return

    # 处理数据docs_songs
    def changeDocsSongs(self, docs_songs):
        tags = []
        for song in docs_songs:
            tags = list(set(tags+song['union'][0]['tags']))
        return tags
