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
### 结果未成功
# 首先生成证书
## 第一步：生成根证书
### 生成根证书
openssl req -out ca.pem -new -x509 -days 3650
### 带参数
openssl req -out ca.pem -new -x509 -days 3650 -subj "/C=CN/ST=BeiJing/O=bigdata/CN=server1/CN=yellowcong/emailAddress=yellowcong@qq.com"
### 部分结果
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
### 生成服务器端证书
openssl x509 -req -in server.req -CA ca.pem -CAkey privkey.pem -CAcreateserial -out server.crt -days 3650

### 合并服务器端私钥和服务器端证书，生成server.pem
cat server.key server.crt > server.pem

### 校验服务器端pem文件
openssl verify -CAfile ca.pem server.pem
### 部分结果
[wymusic@iZuf6g411frzx7ezcnnv92Z ssl]$ openssl x509 -req -in server.req -CA ca.pem -CAkey privkey.pem -CAcreateserial -out server.crt -days 3650
Signature ok
subject=C = CN, ST = JS, O = bigdata, CN = server_mongodb, CN = localhost, emailAddress = 2298930148@qq.com
Getting CA Private Key
Enter pass phrase for privkey.pem:
[wymusic@iZuf6g411frzx7ezcnnv92Z ssl]$ cat server.key server.crt > server.pem
[wymusic@iZuf6g411frzx7ezcnnv92Z ssl]$ openssl verify -CAfile ca.pem server.pem
server.pem: OK

## 第三部分：生成客户端证书
### 生成客户端私钥
openssl genrsa -out client.key 2048
### 生成客户端申请文件
#CN=localhost 是mongo服务的域名地址，这个需要根据自己业务进行修改处理
openssl req -key client.key -new -out client.req -subj "/C=CN/ST=JS/O=bigdata/CN=server1/CN=localhost/emailAddress=2298930148@qq.com"
### 生成客户端证书
openssl x509 -req -in client.req -CA ca.pem -CAkey privkey.pem -CAserial ca.srl  -out client.crt -days 3650

### 合并客户端私钥和客户端证书，生成client.pem
cat client.key client.crt > client.pem

### 校验客户端pem文件
openssl verify -CAfile ca.pem client.pem
### 结果部分
[wymusic@iZuf6g411frzx7ezcnnv92Z ssl]$ openssl genrsa -out client.key 2048
Generating RSA private key, 2048 bit long modulus (2 primes)
...............+++++
........+++++
e is 65537 (0x010001)
[wymusic@iZuf6g411frzx7ezcnnv92Z ssl]$ ls
ca.pem  client.key   server.crt  server.pem
ca.srl  privkey.pem  server.key  server.req
[wymusic@iZuf6g411frzx7ezcnnv92Z ssl]$ openssl req -key client.key -new -out client.req -subj "/C=CN/ST=JS/O=bigdata/CN=server1/CN=localhost/emailAddress=2298930148@qq.com"
[wymusic@iZuf6g411frzx7ezcnnv92Z ssl]$ ls
ca.pem  client.key  privkey.pem  server.key  server.req
ca.srl  client.req  server.crt   server.pem
[wymusic@iZuf6g411frzx7ezcnnv92Z ssl]$ openssl x509 -req -in client.req -CA ca.pem -CAkey privkey.pem -CAserial ca.srl  -out client.crt -days 3650
Signature ok
subject=C = CN, ST = JS, O = bigdata, CN = server1, CN = localhost, emailAddress = 2298930148@qq.com
Getting CA Private Key
Enter pass phrase for privkey.pem:
[wymusic@iZuf6g411frzx7ezcnnv92Z ssl]$ cat client.key client.crt > client.pem
[wymusic@iZuf6g411frzx7ezcnnv92Z ssl]$ openssl verify -CAfile ca.pem client.pem
client.pem: OK
[wymusic@iZuf6g411frzx7ezcnnv92Z ssl]$ ls -al
total 40
drwxrwxr-x 2 wymusic wymusic  197 Jan 16 22:20 .
drwx------ 4 wymusic wymusic  160 Jan 16 21:15 ..
-rw-rw-r-- 1 wymusic wymusic 1371 Jan 16 21:03 ca.pem
-rw-rw-r-- 1 wymusic wymusic   41 Jan 16 22:20 ca.srl
-rw-rw-r-- 1 wymusic wymusic 1249 Jan 16 22:20 client.crt
-rw------- 1 wymusic wymusic 1679 Jan 16 22:19 client.key
-rw-rw-r-- 1 wymusic wymusic 2928 Jan 16 22:20 client.pem
-rw-rw-r-- 1 wymusic wymusic 1021 Jan 16 22:20 client.req
-rw------- 1 wymusic wymusic 1854 Jan 16 21:02 privkey.pem
-rw-rw-r-- 1 wymusic wymusic 1261 Jan 16 22:15 server.crt
-rw------- 1 wymusic wymusic 1675 Jan 16 21:06 server.key
-rw-rw-r-- 1 wymusic wymusic    0 Jan 16 22:16 server.pem
-rw-rw-r-- 1 wymusic wymusic 1029 Jan 16 21:30 server.req

# 配置服务端
## 检查配置文件 mongodb.conf
1. cat <<EOF > /home/wymusic/mongodb/mongodb/mongodb.conf
2. 直接配置文件
#数据库数据存放目录
dbpath = /home/wymusic/mongodb/mongodb/data/db
#日志文件存放目录
logpath = /home/wymusic/mongodb/mongodb/data/log/mongodb.conf
#日志追加方式
logappend = true
#端口
port = 27017
#是否认证
auth = true
#以守护进程的方式在后台运行
fork = true
#远程连接指定ip，否则无法连接，一般不做限制
bind_ip = 0.0.0.0
#最大同时连接数
maxConns = 5
#每次写入会记录一条操作日志（通过journal可以重新构造出写入的数据）。
journal = true
#即使宕机，启动时wiredtiger会先将数据恢复到最近一次的checkpoint点，然后重放后续的journal日志来恢复。
storageEngine = wiredTiger  #存储引擎有mmapv1、wiretiger、mongorocks
Shell 
mongo --sslAllowInvalidCertificates --sslAllowInvalidHostnames --ssl --sslPEMKeyFile /usr/local/mongo/ssl/client.pem --sslCAFile /usr/local/mongo/ssl/ca.pem --host 127.0.0.1
# 确认需要使用反代
## 尝试使用反代完成
安装ss5 需要的配置
yum install gcc openldap-devel pam-devel openssl-devel
使用以下命令获取ss5
wget https://sourceforge.net/projects/ss5/files/ss5/3.8.9-8/ss5-3.8.9-8.tar.gz
解压文件
tar zxvf ./ss5-3.8.9-8.tar.gz
# 以上所有解决方法都不正确，问题重点是服务器控制台没有设置端口同行，需要通过服务器控制台设置可放行的端口
连接语句
mongodb://PJMVSSM:******@IP:PORT/?authSource=nobody&readPreference=primary&directConnection=true&ssl=false