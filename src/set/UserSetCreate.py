import mongo.Connect as connect
import mongo.FuncColle as fcc
import myutils.c_user as cua
import hashlib
import random
import uuid
import time as t


class UserSetCreate(object):
    def __init__(self) -> None:
        self.count = 100

        # 数据库操作
        self.f = fcc.Colle()
        pass

    def makeUserSet(self, collection_name="user"):
        print("[" + t.asctime(t.localtime()) + "]" +
              "Start make " + "user")
        # 创建一个用户的名字，和密码
        # 用户和密码暂时设定为一致
        # 写入用户数据集
        # 第一步随机生成用户名和用户密码 数据量为100
        # 使用hashlib.md5(bytes(password, encoding="utf-8")).hexdigest() 加密密码
        list_user = [
            {
                "id": uuid.uuid1().hex,
                "name": cua.defaultuser['username'],
                "password": str(hashlib.md5(bytes(cua.defaultuser['password'], encoding="utf-8")).hexdigest())
            }
        ]
        for i in range(self.count):
            self.createUniqueUser(list=list_user)
        self.f.insertDocument(
            0, docs=list_user, collection_name="user")
        return

    # 生成随机的字符串作为用户集的数据知道生成出100组数据
    # 保证用户名的唯一性，不需要其他的唯一性（mongo本省具有唯一objectId）
    # 密码是用户名+123
    def createUniqueUser(self, list):
        '''这是16位的随机字符串'''
        str_set = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        random_str = ""
        for i in range(random.randint(1, 10)):
            index = random.randint(0, len(str_set) - 1)
            random_str += str_set[index]
        diction_user = {
            "id": uuid.uuid1().hex,
            "name": random_str,
            "password": str(hashlib.md5(bytes(random_str+"123", encoding="utf-8")).hexdigest())
        }
        if self.isUniqueUser(diction=diction_user, list=list):
            list.append(diction_user)
        else:
            self.createUniqueUser(list=list)
        return list

    # 判断是否是一个唯一的User
    def isUniqueUser(self, diction, list):
        if not any(user['name'] == diction['name'] for user in list):
            # does not exist
            return True
        else:
            return False
