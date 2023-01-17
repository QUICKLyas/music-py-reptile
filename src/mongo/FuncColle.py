import mongo.Connect as connect


class Colle (object):
    def __init__(self) -> None:
        self.con = connect.Conn()
        self.condb = self.con.getDB()
        self.collist = self.condb. list_collection_names(session=None)
        pass

    def isCollectionExist(self, collection_name="test"):
        if collection_name in self.collist:
            print("The collection:" + collection_name + " exists")
            return True
        else:
            False

    def createCollection(self, collection_name):
        # 判断是否存在collection，若不存在创建，若存在需要连接
        if self.isCollectionExist(collection_name):
            print(collection_name + "exists!")
        cols = self.condb[collection_name]
        cols.insert_one({"name": "playlist"})
        cols.delete_one({"name": "playlist"})
        return

    def insertDocument(self, doc, collection_name):
        # 确保该collection是存在的
        self.createCollection(collection_name)
        cols = self.condb[collection_name]
        for i in doc:
            # 将数据存入
            cols.insert_one(i)
            break
        return
