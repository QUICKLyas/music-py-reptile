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
            # 判断是否存在该数据，不存在，将数据插入
            if self.isDocExtists(i, collection_name) != True:
                cols.insert_one(i)
                print("new: ", n, " : ", i['name'])
                n += 1
            # 当处理的是song表时，判断存在该数据，如果存在，那么就要做更新
            if collection_name == "song" and self.isDocExtists(i, collection_name) == True:
                n += 1
                myquery = {"id": i['id']}
                newvalues = {"$set": {"tags": i['tags']}}
                cols.update_one(myquery, newvalues)
                print("update:", n, " : ", i['name'])
        # 输出信息显示当前写入数据库的数据个数
        # print("The number of object that have been wrote is ", n)
        # 假设我们处理的playlists，就返回playlists的最后一个单元的updateTime
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
        # print(length,doc['id'])
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
