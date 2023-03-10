'''
Author: QUICKLyas 2298930148@qq.com
Date: 2023-01-18 19:45:48
LastEditors: QUICKLyas 2298930148@qq.com
LastEditTime: 2023-01-20 09:00:28
FilePath: /reptile/src/controller/FuncGetJson.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import json
import requests
import ssl as s
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

        req = request.Request(
            url=ob.url,
            headers=ob.head
        )
        # print(ob.url)
        ssl = s._create_unverified_context()
        res = request.urlopen(req, context=ssl)
        context = res.read().decode(cc.code['utf-8'])
        context = json.loads(context)
        return context

    def getCookieFromUrl(self, ob, name):
        req = request.Request(
            url=ob.url,
            headers=ob.head
        )
        session = requests.session()
        cookies = session.get(ob.url).cookies.get_dict()
        print(cookies)

    def writeJsonToDataBase(self, limit, context, col_name):
        return self.colF.insertDocument(limit, context, col_name)
