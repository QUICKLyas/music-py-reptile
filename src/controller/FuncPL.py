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

    # 写 playlists
    def writePLtoMongo(self):
        for n in range(50):
            # 获取内容
            # print(pp.getUrl())
            # print(n, pp.getOffset(), pp.getL())
            self.pl.setOffset(self.pl.getOffset() + self.pl.getL())
            context = self.f.getJsonFromUrl(self.pl, "playlists")
            self.f.writeJsonToDataBase(
                context=context['playlists'], col_name="playlists")
            self.fc.findDocument("playlists")
            t.sleep(8)
        return "playlists"

    def writePLDtoMongo(self):
        # 按量获取playlist 的 id
        # 限制为每50一组 通过self.pl.getL()获取
        # 第一步 获取数据
        n = 0
        while (True):
            docs = self.fc.findDocument(
                collection_name="playlists",
                limit=self.pl.getL(),
                page=n)
            if len(list(docs)) == 0:
                break
            for i in docs:
                print(i['id'])
        return "playlist detail"
