import math
import time as t

import myutils.c_ua as cua
import myutils.c_urls as curls


class PlayList(object):

    def __init__(self, before=curls.urls['playlist']['before']):
        self.before = before
        self.limit = 100
        self.url = curls.urls['playlist']['head'] + \
            str(self.before)
        self.head = {
            'User-Agent': cua.ua
        }

    def getL(self):
        return self.limit

    def getBefore(self):
        return self.before

    def setBefore(self, before):
        self.before = before
        self.setUrl("")

    def getUrl(self):
        return self.url

    def setUrl(self, url):
        if(url == ""):
            self.url = curls.urls['playlist']['head'] + \
                str(self.before)
        else:
            self.url = url

    def getHead(self):
        return self.head

    def setHead(self, head):
        self.iheadd = head


class PlayListDetail(object):
    # timestamp=math.trunc(t.time())
    def __init__(self, id=curls.urls['playlist_detail']['id'], s=0) -> None:
        # math.trunc(t.time())
        self.id = id
        # 最近收藏这个id的用户
        self.s = curls.urls['playlist_detail']['s']+str(s)
        self.url = curls.urls['playlist_detail']['head'] + \
            str(self.id) + \
            self.s
        self.head = {
            'User-Agent': cua.ua
        }

    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id
        self.setUrl("")

    def getS(self):
        return self.s

    def setS(self, s):
        self.s = s

    def getUrl(self):
        return self.url

    def setUrl(self, url):
        if(url == ""):
            self.url = curls.urls['playlist_detail']['head'] + \
                str(self.id) + \
                self.s
        else:
            self.url = url

    def getHead(self):
        return self.head

    def setHead(self, head):
        self.iheadd = head
