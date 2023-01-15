import controller.FuncGetJson as fgJ
import domain.PlayList as pl

# 新建对象
pp = pl.PlayList()
# 新建方法对象
f = fgJ.GetJson()
# 获取内容
context = f.getJsonFromUrl(pp, "playlist")
f.writeJson(context, file_name="pl")
