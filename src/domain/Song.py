import config.c_ua as cua
import config.c_urls as curls


class Song(object):

    def __init__(self, id=curls.urls['song_detail']['ids']):
        self.id = id
        self.url = curls.urls['song_detail']['head'] + \
            str(id)
        self.head = {
            'User-Agent': cua.ua
        }

    def getId(self):
        return self.id

    def getUrl(self):
        return self.url

    def getHead(self):
        return self.head
