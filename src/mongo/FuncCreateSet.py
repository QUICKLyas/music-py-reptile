import mongo.Connect as connect


class CreateSet(object):
    def __init__(self) -> None:
        self.con = connect.Conn()
        self.condb = self.con.getDB()
        # 数据库中存在的表格名
        self.conlist = self.condb.list_collection_names()
        pass

    def WriteUsertoMongo():
        return
