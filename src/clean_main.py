#!/usr/bin/python3
import mongo.FuncColle as funccol  # 这个是用来和数据库连接的
import mongo.Connect as connect
# 本程序只需要完成对音乐信息的更新即可，不要过多更改音乐表的信息，保证数据格式的不变，避免和java程序产生冲突，造成项目的大修改以致于崩溃


# 1 写一个循环，按次序获取音乐的id，连接mongo程序

size = 100
pageInde = 0
connect = funccol.Colle()
# 连接数据库
# condb = connect.con.getDB()
# 连接对应的数据表
# 首先连接基础表
cols = connect.condb["song"]
docs = cols.find({}, {}).limit(100).skip(1*100)
# 循环体内部代码较多，提取出来，保证程序代码的整体平衡
for item in docs:
    print(item)

# 获得数据，根据数据中的数据进行三件事，更新数据，查找对应的护具信息，生成新的数据信息
# songDict = {
#     "id":
#     "name":
#     "songAble":
#     "songUrl":
#     "similaritySongs":}
# songDetailDict = {
#     "id":
#     "name":
#     "song": }
