import myutils.c_ua as cua
import myutils.c_urls as curls


class Tags(object):
    def __init__(self, id=curls.urls['tags']['id']) -> None:
        self.id = id
        self.url = curls.urls['tags']['head']
        self.head = {
            'User-Agent': cua.ua
        }

    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id
        self.setUrl("")

    def getUrl(self):
        return self.url

    def setUrl(self, url):
        if(url == ""):
            self.url = curls.urls['tags']['head']
        else:
            self.url = url

    def getHead(self):
        return self.head

    def setHead(self, head):
        self.iheadd = head
