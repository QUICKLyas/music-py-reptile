import json
import time as t
from urllib import request

from fake_useragent import UserAgent as ua

import config.c_code as cc
import config.c_urls as curls


class GetSong(object):
    def __init__(self, ids) -> None:
        self.url = curls.urls['song_detail']
        self.req = self.setHeader(ids)

    def setHeader(self, ids):
        header = {
            "User-Agent": ua().chrome
        }
        req = request.Request(
            url=self.url['head'] + ids,
            headers=header
        )
        return req

    def getSongDetail(self):
        print("Start get song's detail " +
              "[" + t.asctime(t.localtime()) + "]" + ":")
        res = request.urlopen(self.req)
        # 获取 song detail 的json 报文
        context = res.read().decode(cc.code['utf-8'])
        # 解析出json
        context = json.loads(context)
        return context
