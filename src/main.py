'''
Author: QUICKLyas 2298930148@qq.com
Date: 2023-01-20 08:52:25
LastEditors: QUICKLyas 2298930148@qq.com
LastEditTime: 2023-01-20 16:14:51
FilePath: /reptile/src/main.py
# Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
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
fcPL = fcpl.PL()
# fcPL.writePLtoMongo()
# fcPL.writePLDtoMongo()
fcPL.writeSongDetailtoMongo()
fcPL.writeSongtoMongo()
