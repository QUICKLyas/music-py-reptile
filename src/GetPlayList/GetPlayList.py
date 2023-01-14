import json
import time as t
from urllib import request

from fake_useragent import UserAgent as ua

import config.c_code as cc
import config.c_urls as curls


class GetPlayList(object):
    def __init__(self):
        self.url = curls.urls['playlist']
        self.req = self.setHeader()

    def setHeader(self):
        header = {
            'User-Agent': ua().chrome
        }
        req = request.Request(
            url=self.url['head'] +
            str(self.url['offset']) + self.url["limit"],
            headers=header
        )
        return req

    def getPlayList(self):
        print("Start get PlayList "+"[" + t.asctime(t.localtime()) + "]" + ":")
        res = request.urlopen(self.req)
        # 获取playlist的json报文
        context = res.read().decode(cc.code['utf-8'])
        # 解析出json
        context = json.loads(context)
        print(len(context['playlists']))
        return context
