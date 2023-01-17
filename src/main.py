import time as t

import controller.FuncGetJson as fgJ
import domain.PlayList as pl
import mongo.FuncColle as funccol
import service.Parse as parse

# 首先获取playlist，并存储到数据库中
# 然后根据playlist的id 获取 playlist_detail
# 在play_detail的tracks 获取 songs_id
# 同时应该存储每首歌的歌曲是否可以听取的信息
# 新建对象
pp = pl.PlayList()
# 新建方法对象
f = fgJ.GetJson()
fc = funccol.Colle()
p = parse.Parse()
# 该过程保证playlist 的 输入
for n in range(50):
    # 获取内容
    # print(pp.getUrl())
    # print(n, pp.getOffset(), pp.getL())
    pp.setOffset(pp.getOffset() + pp.getL())
    context = f.getJsonFromUrl(pp, "playlist")
    f.writeJsonToDataBase(
        context=context['playlists'], col_name="playlist")
    fc.findDocument("playlist")
    t.sleep(8)
# context = f.getJsonFromUrl(pp, "playlist")
# f.writeJsonToDataBase(context=context['playlists'], col_name="playlist")
# fc.findDocument("playlist")
# f.writeJson(context, file_name="pl")
# plist = p.readPlayList()
# p.songIds(plist[0]['songs'])
# p.cleanSong(30612793)
# test mongo 连接collection
# col = funccol.Colle()
# col.createCollection("playlist")
