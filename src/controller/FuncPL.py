import time as t

import controller.FuncGetJson as fgJ
import domain.PlayList as pl
import mongo.FuncColle as funccol
import service.Parse as parse


class PL(object):
    def __init__(self) -> None:
        self.pl = pl.PlayList()
        self.pld = pl.PlayListDetail()
        self.f = fgJ.GetJson()
        self.fc = funccol.Colle()
        self.p = parse.Parse()

    def writePLtoMongo(self):
        for n in range(50):
            # 获取内容
            # print(pp.getUrl())
            # print(n, pp.getOffset(), pp.getL())
            self.pl.setOffset(self.pl.getOffset() + self.pl.getL())
            context = self.f.getJsonFromUrl(self.pl, "playlist")
            self.f.writeJsonToDataBase(
                context=context['playlists'], col_name="playlist")
            self.fc.findDocument("playlist")
            t.sleep(8)
        return "playlist"

    def writePLDtoMongo(self):
        # 
        return "playlist detail"
