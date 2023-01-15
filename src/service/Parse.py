
import controller.FuncGetJson as fgJ
import domain.PlayList as pl
import domain.Song as s
import myutils.t_file as tf


class Parse(object):

    def __init__(self) -> None:
        self.pl = pl.PlayListDetail()
        self.f = fgJ.GetJson()
        self.s = s.Song()
        self.sa = s.SongAble()
        pass

    # 该段程序输出的是一个list
    # 结构
    # [
    #   {
    #       "id": 7821742772,
    #       "songs": context
    #   },
    #   ...
    # ]
    def readPlayList(self):
        context = tf.readJson(file_name="pl")
        cList = context['playlists']
        plist = []
        for c in cList:
            # 第一个歌单的id = 7821742772
            # 设置 id
            self.pl.setId(c['id'])
            print(self.pl.getUrl())
            # 获取这个报文
            context = self.f.getJsonFromUrl(self.pl, "playlist detail")
            # 构造字典表示该歌单中歌曲
            pldict = {
                "id": c['id'],
                "songs": context
            }
            # 添加报文到plist后，
            plist.append(pldict)
            break
        return plist

    # 构建歌曲id 的 list
    def songIds(self, songs):
        # 查看每首歌的的Detail
        sList = []
        for s in songs['playlist']['trackIds']:
            # 设置歌曲Id
            self.s.setId(s['id'])
            context = self.f.getJsonFromUrl(self.s, "song detail")
            # 构建一个歌曲列表
            # 如果 是 版本歌曲 跳过 如果不是版本歌曲，不跳过
            if (self.cleanSong(self.s.getId())):
                continue
            sList.append(context)
            break
        # print(sList)
        return sList

    # 判断每首是否能够获取播放权限，排除无法播放的歌曲
    # 如果无权收听，返回True 表示 是 版权歌曲
    # 如果可以收听，返回False 表示 不需要 版本
    def cleanSong(self, id):
        self.sa.setId(id)
        context = self.f.getJsonFromUrl(self.sa, "could this song be listened")
        # 判断是否为None ，如果是 返回 False 不是 返回 True
        if(context['data'][0]['freeTrialPrivilege']['cannotListenReason'] == None):
            return False
        else:
            return True
        return
