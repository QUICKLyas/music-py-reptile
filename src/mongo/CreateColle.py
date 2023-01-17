import mongo.Connect as connect


class CreateColle (object):
    def __init__(self) -> None:
        self.con = connect.Conn()
        self.condb = self.con.getDB()
        # print(self.condb)
        print(self.condb.list_collection_names())
        # self.collist = self.condb.list_collection_names()
        pass

    def createPlayList(self):
        # print(self.collist)
        # if "playlist" not in self.collist:
            # print("The collection not  exists.")
        return
