import time as t

import controller.FuncGetJson as fgJ
import controller.FuncPL as fcpl
import domain.PlayList as pl
import mongo.FuncColle as funccol
import service.Parse as parse

# 首先获取playlist，并存储到数据库中
# 然后根据playlist的id 获取 playlist_detail
# 在play_detail的tracks 获取 songs_id
# 同时应该存储每首歌的歌曲是否可以听取的信息
# 新建对象
print("1")
fcPL = fcpl.PL()
# fcPL.writePLtoMongo()
fcPL.writePLDtoMongo()
