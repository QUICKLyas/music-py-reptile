from pymongo import MongoClient

import myutils.c_user as cu


class Conn (object):
    def __init__(self) -> None:
        self.client = MongoClient(
            cu.user['IP'], int(cu.user['port']))  # Host以及port
        print(self.client)
        self.db = self.client['nobody']
        print(self.db)
        self.client.authenticate(
            cu.user['mongoDB']['username'],
            cu.user['mongoDB']['password'])
        collection = self.db.test   # myset集合，同上解释
        collection.insert({"name": "zhangsan", "age": 18})
        collection.delete_one({"name": "zhangsan"})

    def getClient(self):
        return self.client

    def getDB(self):
        return self.db
