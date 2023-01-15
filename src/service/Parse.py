
import controller.FuncGetJson as fgJ
import domain.PlayList as pl
import myutils.t_file as tf


class Parse(object):

    def __init__(self) -> None:
        self.pl = pl.PlayListDetail()
        self.f = fgJ.GetJson()
        pass

    def readPlayList(self):
        context = tf.readJson(file_name="pl")
        cList = context['playlists']
        for c in cList:
            # first 7821742772
            print(c['id'])
            # 设置 id
            self.pl.setId(c['id'])
            print(self.pl.getUrl())
            context = self.f.getJsonFromUrl(self.pl, "playlist detail")
            print(context)
            break
        # https: // yesplaymusic.yunyuwu.cn/api/playlist/detail?id = &1673792457664 & realIP = 211.161.244.70
        # https: // yesplaymusic.yunyuwu.cn/api/playlist/detail?id = 7821742772 & timestamp = 1673792457664 & realIP = 211.161.244.70
        return
