#!/usr/bin/python3
import mongo.FuncColle as funccol  # 这个是用来和数据库连接的
import mongo.Connect as connect
import domain.Song as s
import controller.FuncGetJson as fGJson
# 本程序只需要完成对音乐信息的更新即可，不要过多更改音乐表的信息，保证数据格式的不变，避免和java程序产生冲突，造成项目的大修改以致于崩溃


# 1 写一个循环，按次序获取音乐的id，连接mongo程序

size = 100
pageInde = 0
connect = funccol.Colle()
f = fGJson.GetJson()
# 连接数据库
# condb = connect.con.getDB()
# 连接对应的数据表
# 首先连接基础表
cols = connect.condb["song"]
colsd = connect.condb["songdetail"]
docs = cols.find({}, {}).limit(100).skip(1*100)
# 循环体内部代码较多，提取出来，保证程序代码的整体平衡
for item in docs:
    # 获取id，根据id获取song和songdetail的信息，保存tag信息
    id = item['id']
    print(id)
    # 获取歌曲信息
    song = s.Song(id=id)
    songDetail = s.SongDetail(ids=id)
    songAble = s.SongAble(id=id)
    # input()
    context = f.getJsonFromUrl(song,  "song")
    contextDetail = f.getJsonFromUrl(songDetail, "songdetail")
    # check/music?id=可能出现问题，无法使用，延用之前保留的音乐权限记录
    # contextAble = f.getCookieFromUrl(songAble, "songAble")
    # print(song.getUrl())
    # print("song:", context, "\n")
    # print(songDetail.getUrl())
    # print("songDetail:", contextDetail, "\n")
    songs = contextDetail['songs'][0]
    data = context['data'][0]
    # print("songAble:",  contextAble, "\n")
    print("id", item['id'], "\n")
    # 更新
    query = {"id": id}
    new_values = {"$set": {
        "songUrl": data['url'], "name": songs['name'], "mark": songs["mark"], "data": data}}
    print(query, new_values)
    # 对应于songDetail的信息更新程序
    new_values_sd = {"$set": {
        "name": songs["name"], "songs": songs}, "$unset": {"song": ""}}
    print(query, new_values_sd)
    pass
    result = cols.update_one(query, new_values)
    result_sd = colsd.update_one(query, new_values_sd)
    # print(result.modified_count, result_sd.modified_count)
    if(result.modified_count == 1 and result_sd.modified_count == 1):
        print(result.modified_count, "complete", item['id'])
    else:
        print("no complete")


# 更新数据到原表中，保证只改变需要改变的数据
# 显示需要的数据项，并与数据库中的数据进行比较和替换

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
