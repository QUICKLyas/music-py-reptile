mongoDB的tgz包 位置
F:\DB\Mongo
使用winscp 传输到远端的服务器上

在服务器上搭建mongoDB数据库的服务
tar -zxvf <压缩包的名字>

解压之后移动解压好的文件，并设置文件
此例中mongoDB的文件是mongodb
在解压好的文件内部创建
mkdir data data/db data/log



在mongodb中创建配置文件mongodb.conf
命令： vim ./mongodb.conf
内容：
# 设置读写权限
sudo chmod 666 data/db data/log
# 数据库数据存放目录
dbpath=/usr/local/mongodb/data/db
# 日志文件存放目录
logpath=/usr/local/mongodb/data/log/mongodb.log
# 日志追加方式
logappend=true
# 端口
port=27017
# 是否认证
auth=true
# 以守护进程方式在后台运行
fork=true
# 远程连接要指定ip，否则无法连接；0.0.0.0代表不限制ip访问
bind_ip=0.0.0.0

配置环境
打开
sudo vim /etc/profile
末尾添加内容：
export MONGODB_HOME=/usr/local/mongodb
export PATH=$PATH:$MONGODB_HOME/bin
重载profile文件

# 后台启动服务
mongod -f /usr/local/mongodb/mongodb.conf 

# 启动mongo ---mongo

设置防火墙
systemctl status firewalld 查看防火墙状态
systemctl start firewalld 启动防火墙
# 设置27017 端口
sudo firewall-cmd --zone=public --add-port=27017/tcp --permanent
# 让防火墙设置生效
sudo firewall-cmd --reload
# 查看开放的端口，验证是否成功
sudo firewall-cmd --zone=public --list-ports

检查服务状态
# mongodb 进程状态
ps aux | grep mongo
# 检查端口是否成功
netstat -lamp | grep 27017
# 如果netstat命令找不到，安装netstat
yum install -y net-tools

停止服务
# 通过进程ID杀死
# 通过mongod命令关闭mongodb服务
mongod -f /home/mongodb/mongodb/mongo.conf

设置开机自启
vim /lib/systemd/system/mongodb.service
生成自动启动文件
[Unit]
    Description=mongodb
    After=network.target remote-fs.target nss-lookup.target
[Service]
    Type=forking
    ExecStart=/home/mongodb/mongodb/bin/mongod -f /home/mongodb/mongodb/mongodb.conf
    ExecReload=/bin/kill -s HUP $MAINPID
    ExecStop=/home/mongodb/mongodb/bin/mongod -f /home/mongodb/mongodb/mongodb.conf --shutdown
    PrivateTmp=true
[Install]
    WantedBy=multi-user.target

是上面的设置能够运行
启动
systemctl start mongodb.service
查看状态
systemctl status mongodb.service
设定开机自启
systemctl enable mongodb.service
重载服务文件mongodb.service
systemctl daemon-reload

设置一个操作mongoDB的角色
首先
1. mongo
数据库内
2. use admin
db.createUser({user:"root",pwd:"",roles:[{role:"userAdminAnyDatabase",db:"admin"}]})
Successfully added user: {
        "user" : "root",
        "roles" : [
                {
                        "role" : "userAdminAnyDatabase",
                        "db" : "admin"
                }
        ]
}
3. 
> use admin
switched to db admin
> show tables
Warning: unable to run listCollections, attempting to approximate collection names by parsing connectionStatus
# 登录
> db.auth("root","")
1
> show tables
system.users
system.version

创建本爬虫程序所使用的用户和数据库
db.createUser({user:'PJMVSSM',pwd:'',roles:[{role:'readWrite',db:'nobody'}]})

> use nobody
switched to db nobody
> db.createUser({user:'PJMVSSM',pwd:'',roles:[{role:'readWrite',db:'nobody'}]})
Successfully added user: {
        "user" : "PJMVSSM",
        "roles" : [
                {
                        "role" : "readWrite",
                        "db" : "nobody"
                }
        ]
}
使用可视化工具连接远程mongodb，使用mongoDBCompass
#### 报错：
TLS/SSL is disabled. If possible, enable TLS/SSL to avoid security vulnerabilities.
发现无法正常连接，需要ssl
# 首先生成证书
## 第一步：生成根证书
### 生成根证书
openssl req -out ca.pem -new -x509 -days 3650
### 带参数
openssl req -out ca.pem -new -x509 -days 3650 -subj "/C=CN/ST=BeiJing/O=bigdata/CN=server1/CN=yellowcong/emailAddress=yellowcong@qq.com"
结果
[wymusic@ ssl]$ ls
ca.pem  privkey.pem
## 第二部： 生成服务端证书
###  生成服务器端私钥
openssl genrsa -out server.key 2048
### 生成服务器端申请文件 cat server.req
/**
#CN=localhost 是mongo机器运行的节点域名信息，如果对不上就会报错
 */
openssl req -key server.key -new -out server.req 
/** -subj "/C=CN/ST=JS/O=bigdata/CN=server1/CN=localhost/emailAddress=2298930148@qq.com"
 */
## 生成服务器端证书
openssl x509 -req -in server.req -CA ca.pem -CAkey privkey.pem -CAcreateserial -out server.crt -days 3650

## 合并服务器端私钥和服务器端证书，生成server.pem
cat server.key server.crt > server.pem

## 校验服务器端pem文件
openssl verify -CAfile ca.pem server.pem

# 生成密钥 
