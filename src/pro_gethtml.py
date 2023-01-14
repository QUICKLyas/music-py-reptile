import json
from urllib import request

from fake_useragent import UserAgent as ua

import config.c_ua as cua
import config.c_urls as curls
import config.t_file as tf
import pro_parse as pparse


class GetHtml(object):
    def __init__(self):
        self.urls = curls.urls
        self.p = pparse.Parse()

    def SetHeader(self):
        header = {
            'User-Agent': ua().chrome
        }
        # create request include ua
        req = request.Request(
            url=self.urls[0]['head'] +
            str(self.urls[0]['offset'])+self.urls[0]['limit'],
            headers=header
        )
        return req

    def GetHtml(self):
        print("start...")
        # send request
        req = self.SetHeader()
        res = request.urlopen(req)
        # pickup answer as utf-8 txt
        answer = res.read().decode('utf-8')
        # transmit as utf-8 json
        answer = json.loads(answer)
        return answer

    def ParseAns(self, context):
        # print(context)
        self.p.ParsePlayList(context)
        return

    def WriteHtml(self, context):
        tf.WriteJson(context)
