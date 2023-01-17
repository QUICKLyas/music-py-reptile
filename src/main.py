import controller.FuncGetJson as fgJ
import domain.PlayList as pl
import mongo.CreateColle as crecol
import service.Parse as parse

# 新建对象
# pp = pl.PlayList()
# 新建方法对象
# f = fgJ.GetJson()
# p = parse.Parse()
# 获取内容
# context = f.getJsonFromUrl(pp, "playlist")
# f.writeJson(context, file_name="pl")
# plist = p.readPlayList()
# p.songIds(plist[0]['songs'])
# p.cleanSong(30612793)
# test mongo 连接collection
from pymongo import MongoClient
# 建立连接
# host="127.0.0.1", port=27017,username="admin",password="12345678"
client = MongoClient(host="139.224.66.83", port=27017,
                     username='PJMVSSM', password='123456')
# 数据库名admin
db = client.nobody
# 认证用户密码
# 创建集合和数据
db.test.insert_one({"name": "this is test"})
col = db.test
# 打印数据输出
print(col)
# for item in col.find():
#     print (item)
# 关闭连接
client.close()
