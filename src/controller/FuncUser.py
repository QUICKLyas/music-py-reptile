import time as t

import domain.User as user
import controller.FuncGetJson as fgJ
import mongo.FuncColle as funccol
import service.Parse as parse


class Users(object):
    def __init__(self) -> None:
        self.u = user.UserLoginCellPhone()
        self.u.setPhone()
        self.u.setPassword()
        self.f = fgJ.GetJson()
        self.fc = funccol.Colle()
        self.p = parse.Parse()
        pass
    # important things: 我们需要注意存入数据库中的数据
    # 必需是有id和name字段的否则无法存储到数据库中
    # 其次才是我们需要的简单信息
    # 如果存储的是密码，应该考虑进行加密，或者权限设置

    def writeUsertoMongo(self):
        print("[" + t.asctime(t.localtime()) + "]" +
              "Start get " + "user by cellphone")
        context = self.f.getCookieFromUrl(self.u, "user")
        print(context)

        return
