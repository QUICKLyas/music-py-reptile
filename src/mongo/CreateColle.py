import mongo.Connect as connect


class CreateColle (object):
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
        cols.delete_many({"name": "playlist"})
        return
