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
col = crecol.CreateColle()
col.createCollection("playlist")
