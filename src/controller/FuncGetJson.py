import json
import time as t
from urllib import request

import mongo.FuncColle as funccol
import myutils.c_code as cc
import myutils.t_file as tf


class GetJson(object):
    def __init__(self) -> None:
        self.colF = funccol.Colle()
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

    def writeJsonToDataBase(self, context, col_name):
        self.colF.insertDocument(context, col_name)
