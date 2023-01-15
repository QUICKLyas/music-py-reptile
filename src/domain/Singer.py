import myutils.c_ua as cua
import myutils.c_urls as curls


class Singer(object):

    def __init__(self, id=curls.urls['artist']['id']):
        self.id = id
        self.url = curls.urls['artist']['head'] + \
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
