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
        self.sd = s.SongDetail()

    # 写 playlists
    def writePLtoMongo(self):
        print("[" + t.asctime(t.localtime()) + "]" +
              "Start get " + "playlist")
        n = 0
        before = 0
        while(True):
            print("playlists : ", n)
            # 获取内容
            # print(pp.getUrl())
            # print(n, pp.getOffset(), pp.getL())

            context = self.f.getJsonFromUrl(self.pl, "playlists")

            if len(list(context['playlists'])) == 0 or n > 100:
                print(context['playlists'])
                break
            before = self.f.writeJsonToDataBase(
                len(list(context['playlists']))-1,
                context=context['playlists'], col_name="playlists")
            self.fc.findDocument("playlists")
            # print(before)
            self.pl.setBefore(str(before))
            n += 1
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
            print("pl_docs_page:", n, " pl_docs_length:", len(list(docs)))
            n += 1
            # print(len(list(docs)))
            if len(list(docs)) == 0:
                break
            # 将每个playlistdetail存放到playlistdetail
            num = 1

            for i in docs:
                context = []
                print(num, " pl_id :", i['id'], " pl_name :", i['name'])
                # 根据id 获取playlistdetail数据
                self.pld.setId(i['id'])
                # print(self.pld.getUrl())
                context.append(self.f.getJsonFromUrl(
                    self.pld,  "playlistsdetail")['playlist'])
                num += 1
                t.sleep(3)
                self.f.writeJsonToDataBase(
                    0, context=context, col_name="playlistdetail")
            # self.fc.findDocument("playlistdetail")
        return "playlist detail"

    # 写 song
    def writeSongtoMongo(self):
        print("[" + t.asctime(t.localtime()) + "]" +
              "Start get " + "song and songable")
        # 首先获取trackIds
        n = 0
        while (True):
            tags = []
            docs = self.fc.findDocument(
                collection_name="playlistdetail",
                limit=1,
                page=n)

            if(len(docs[0]['trackIds']) < 1):
                break
            else:
                tags = docs[0]['tags']
                docs = docs[0]['trackIds']
            print("pld_docs_page:", n, " pld_docs_length:", len(docs))

            n += 1
            if len(list(docs)) == 0:
                break
            num = 1
            for i in docs:
                context = []
                # 根据id 获取song和songAble数据
                # 设置一首哥的数据
                print(num, "song_id:", i['id'])
                self.s.setId(i['id'])
                self.sa.setId(i['id'])
                contextS = self.f.getJsonFromUrl(
                    self.s, "song")['data'][0]
                contextSA = self.f.getJsonFromUrl(
                    self.sa, "songable"
                )
                diction = {
                    "id": i['id'],
                    "name": i['id'],
                    "song_url": contextS,
                    "song_able": contextSA,
                    "tags": tags
                }
                context.append(diction)
                # self.fc.findDocument("playlistdetail")
                num += 1
                t.sleep(2)
                self.f.writeJsonToDataBase(
                    0, context=context, col_name="song")
        return "song"

    def writeSongDetailtoMongo(self):
        print("[" + t.asctime(t.localtime()) + "]" +
              "Start get " + "songdetail")
        n = 0
        while (True):
            docs = self.fc.findDocument(
                collection_name="song",
                limit=self.pl.getL(),
                page=n)
            if len(list(docs)) == 0:
                break
            num = 1
            context = []
            for i in docs:
                print(num, "song_id:", i['id'])
                self.sd.setId(i['id'])
                contextSD = self.f.getJsonFromUrl(
                    self.sd, "songdetail")['songs'][0]
                # print(contextSD)
                diction = {
                    "id": i['id'],
                    "name": contextSD['al']['name'],
                    "song": contextSD
                }
                context.append(diction)
                num += 1
                t.sleep(2)
            self.f.writeJsonToDataBase(
                0, context=context, col_name="songdetail")
        return "song detail"
