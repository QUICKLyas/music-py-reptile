## 指令

nohup python -u test.py > test.log 2>&1 &
test.py 是要运行的脚本；
test.log 是运行脚本生成的日志文件；
-u 表示每多一条信息就实时输出到 test.log 日志文件中；
& 表示后台执行，运行时可以查看日志。
查看所有进程：
ps -A
查看后台所有 python 运行程序：
ps -ef |grep python

## 关闭后台程序

jobs 查看 jobs 号
kill %jobs
查看进程号 PID
kill PID

## 运行 py

创建的用户中
用户名 ：用户
用户密码 ： 用户名+123
