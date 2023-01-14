import GetPlayList.DisposePlayList as dp
import GetPlayList.GetPlayList as gp

gp = gp.GetPlayList()
dp = dp.DisposePlayList()
context = gp.getPlayList()
dp.writePltoJson(context)
