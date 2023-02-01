'''
Author: QUICKLyas 2298930148@qq.com
Date: 2023-01-18 19:44:58
LastEditors: QUICKLyas 2298930148@qq.com
LastEditTime: 2023-01-20 09:03:45
FilePath: /reptile/src/mongo/FuncColle.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import mongo.Connect as connect


class Colle (object):
    def __init__(self) -> None:
        self.con = connect.Conn()
        self.condb = self.con.getDB()
        self.collist = self.condb.list_collection_names()
        pass

    # 创建collection
    def createCollection(self, collection_name):
        # 判断是否存在collection，若不存在创建，若存在需要连接
        if self.isCollectionExist(collection_name):
            # print(collection_name + " exists!")
            pass
        cols = self.condb[collection_name]
        cols.insert_one({"name": "playlist"})
        cols.delete_one({"name": "playlist"})
        return

    # 插入数据，一次一条
    def insertDocument(self, last, docs, collection_name):
        # 确保该collection是存在的
        self.createCollection(collection_name)
        cols = self.condb[collection_name]
        # 将每段数据存储到数据库中
        # print(cols.estimated_document_count())
        n = 0
        for i in docs:
            # print(i['id'],i['name'])
            # 将数据存入

            if self.isDocExtists(i, collection_name) != True:
                cols.insert_one(i)
                print(n, " : ", i['name'])
                print()
                n += 1

        print("The number of object is ", n)
        if (collection_name == "playlists"):
            updateTime = docs[last]['updateTime']
            return updateTime
        else:
            return
    # 查找数据，设定一些限制保证数据的可用性

    def findDocument(self, collection_name, query={}, projection={}, limit=1, page=0):
        # print(limit, page)
        cols = self.condb[collection_name]
        docs = cols.find(query, projection).limit(limit).skip(page*limit)
        return list(docs)

    # 删除数据
    def deleteDocument(self, collection_name, query, projection):
        cols = self.condb[collection_name]
        cols.delete_many(query, projection)
        return

    # 判断数据在指定的collection是否已经存在，
    # 存在了返回true，
    # 不存在返回false
    def isDocExtists(self, doc, collection_name):
        self.col = self.condb[collection_name]
        docs = self.col.find({'id': doc['id']})
        length = len(list(docs))
        # print(length)
        # for i in docs:
        #     print(i)
        if length != 0:
            return True
        else:
            return False

    # 判断collection 是否存在
    def isCollectionExist(self, collection_name="test"):
        if collection_name in self.collist:
            return True
        else:
            return False
