import math
import time as t

import myutils.c_ua as cua
import myutils.c_urls as curls


class PlayList(object):

    def __init__(self, offset=curls.urls['playlist']['offset']):
        self.offset = offset
        self.url = curls.urls['playlist']['head'] + \
            str(offset) + \
            curls.urls['playlist']["limit"]
        self.head = {
            'User-Agent': cua.ua
        }

    def getOffset(self):
        return self.offset

    def getUrl(self):
        return self.url

    def getHead(self):
        return self.head


class PlayListDetail(object):
    def __init__(self, id=curls.urls['playlist_detail']['id'], timestamp=math.trunc(t.time())) -> None:
        # math.trunc(t.time())
        self.id = id
        self.timestamp = curls.urls['playlist_detail']["timestamp"] + \
            str(timestamp)
        self.url = curls.urls['playlist_detail']['head'] + \
            str(self.id) + \
            self.timestamp
        self.head = {
            'User-Agent': cua.ua
        }

    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id
        self.setUrl("")

    def getTimestamp(self):
        return self.timestamp

    def setTimestamp(self, timestamp):
        self.timestamp = timestamp

    def getUrl(self):
        return self.url

    def setUrl(self, url):
        if(url == ""):
            self.url = curls.urls['playlist_detail']['head'] + \
                str(self.id) + \
                self.timestamp
        else:
            self.url = url

    def getHead(self):
        return self.head

    def setHead(self, head):
        self.iheadd = head
