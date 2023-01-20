import time as t

import controller.FuncGetJson as fgJ
import domain.PlayList as pl
import domain.Song as s
import mongo.FuncColle as funccol
import service.Parse as parse


class PL(object):
    def __init__(self) -> None:
        self.pl = pl.PlayList()
        self.pld = pl.PlayListDetail()
        self.s = s.Song()
        self.sa = s.SongAble()
        self.f = fgJ.GetJson()
        self.fc = funccol.Colle()
        self.p = parse.Parse()

    # 写 playlists
    def writePLtoMongo(self):
        print("[" + t.asctime(t.localtime()) + "]" +
              "Start get " + "playlist")
        for n in range(30):
            print("playlists ：", n)
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

    # 写 playlistdetail
    def writePLDtoMongo(self):
        # 按量获取playlist 的 id
        # 限制为每50一组 通过self.pl.getL()获取
        # 第一步 获取数据
        print("[" + t.asctime(t.localtime()) + "]" +
              "Start get " + "playlistdetail")
        n = 0
        while (True):
            docs = self.fc.findDocument(
                collection_name="playlists",
                limit=self.pl.getL(),
                page=n)
            print("pld:", n, "length:", len(list(docs)))
            n += 1
            # print(len(list(docs)))
            if len(list(docs)) == 0:
                break
            # 将每个playlistdetail存放到playlistdetail
            num = 0
            for i in docs:
                print(num, "pld:", i['id'])
                # 根据id 获取playlistdetail数据
                self.pld.setId(i['id'])
                # print(self.pld.getUrl())
                context = []
                context.append(self.f.getJsonFromUrl(
                    self.pld, "playlistsdetail")['playlist'])
                self.f.writeJsonToDataBase(
                    context=context, col_name="playlistdetail")
                # self.fc.findDocument("playlistdetail")
                num += 1
                t.sleep(3)
        return "playlist detail"

    # 写 song
    def writeSongtoMongo(self):
        print("[" + t.asctime(t.localtime()) + "]" +
              "Start get " + "song and songdetail")
        # 首先获取trackIds
        n = 0
        while (True):
            docs = self.fc.findDocument(
                collection_name="playlistdetail",
                limit=self.pl.getL(),
                page=n)
            print("songs:", n, "length:", len(list(docs)))
            n += 1
            songIds = []
            num = 0
            for i in docs:
                print(num, "song:", i['id'])
                # print(type(i), i['trackIds'])
                songIds.extend(i['trackIds'])
            # songIds = list(docs['trackIds'])
            print(len(songIds))
            # print(len(list(docs)))
            context = []
            if len(list(docs)) == 0:
                break
            for i in songIds:
                # 根据id 获取song和songAble数据
                # 设置一首哥的数据
                self.s.setId(i['id'])
                self.sa.setId(i['id'])
                contextS = self.f.getJsonFromUrl(
                    self.s, "song")['songs'][0]
                contextSA = self.f.getJsonFromUrl(
                    self.sa, "songable"
                )['data'][0]
                diction = {
                    "id": i['id'],
                    "song": contextS,
                    "song_able": contextSA
                }
                context.append(diction)
                # self.fc.findDocument("playlistdetail")
                num += 1
                t.sleep(1)
            self.f.writeJsonToDataBase(
                context=context, col_name="song")
        return "song"
