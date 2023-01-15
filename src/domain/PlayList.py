import config.c_ua as cua
import config.c_urls as curls


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
