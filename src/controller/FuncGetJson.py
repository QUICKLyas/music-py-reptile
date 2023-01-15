import json
import time as t
from urllib import request

import config.c_code as cc
import config.t_file as tf


class GetJson(object):
    def __init__(self) -> None:
        pass

    def getJsonFromUrl(self, ob, name):
        print("[" + t.asctime(t.localtime()) + "]" +
              "Start get " + name + "\n")
        req = request.Request(
            url=ob.url,
            headers=ob.head
        )
        res = request.urlopen(req)
        context = res.read().decode(cc.code['utf-8'])
        context = json.loads(context)
        return context

    def writeJson(self, context, file_name):
        tf.writeJson(context, file_name=file_name)
