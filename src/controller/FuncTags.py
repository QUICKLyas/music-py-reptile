import time as t

import domain.Tags as tgs
import controller.FuncGetJson as fgJ
import mongo.FuncColle as funccol
import service.Parse as parse


class Tags(object):
    def __init__(self) -> None:
        self.tgs = tgs.Tags()

        self.f = fgJ.GetJson()
        self.fc = funccol.Colle()
        self.p = parse.Parse()
        pass

    # 只存储tags，id是时间戳，所以需要updata的处理
    def writeTagstoMongo(self):
        print("[" + t.asctime(t.localtime()) + "]" +
              "Start get " + "catlist")
        context = self.f.getJsonFromUrl(self.tgs, "catlist")
        # code all sub categories
        #  0       1       2       3       4
        # ['语种', '风格', '场景', '情感', '主题']
        categories = self.p.readTagsCategories(context=context)
        sub = self.p.readTagsSub(context)
        answer = [
            {
                "id": int(t.time()),
                "name": "tags",
                "categories": categories,
                "sub": sub,
                "subSpring": context['sub']
            }
        ]
        sublist = self.p.readTagsSubtoListId(context)
        answer.extend(sublist)
        # print(len(answer))
        # print(answer)
        self.f.writeJsonToDataBase(
            0, context=answer, col_name="tags")
        return
