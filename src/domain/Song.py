import myutils.c_ua as cua
import myutils.c_urls as curls


class Song(object):

    def __init__(self, id=curls.urls['song_url']['id']):
        self.id = id
        self.url = curls.urls['song_url']['head'] + \
            str(self.id)
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
            self.url = curls.urls['song_url']['head'] + \
                str(self.id)
        else:
            self.url = url

    def getHead(self):
        return self.head

    def setHead(self, head):
        self.iheadd = head


class SongAble(object):
    def __init__(self, id=curls.urls['song_listen_able']['id']) -> None:
        self.id = id
        self.url = curls.urls['song_listen_able']['head'] + \
            str(self.id)
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
            self.url = curls.urls['song_listen_able']['head'] + \
                str(self.id)
        else:
            self.url = url

    def getHead(self):
        return self.head

    def setHead(self, head):
        self.iheadd = head


class SongDetail(object):
    def __init__(self, ids=curls.urls['song_detail']['id']) -> None:
        self.id = ids
        self.url = curls.urls['song_detail']['head'] + \
            str(self.id)
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
            self.url = curls.urls['song_detail']['head'] + \
                str(self.id)
        else:
            self.url = url

    def getHead(self):
        return self.head

    def setHead(self, head):
        self.iheadd = head
