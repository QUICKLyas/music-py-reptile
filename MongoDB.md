mongoDB��tgz�� λ��
F:\DB\Mongo
ʹ��winscp ���䵽Զ�˵ķ�������

�ڷ������ϴmongoDB���ݿ�ķ���
tar -zxvf <ѹ����������>

��ѹ֮���ƶ���ѹ�õ��ļ����������ļ�
������mongoDB���ļ���mongodb
�ڽ�ѹ�õ��ļ��ڲ�����
mkdir data data/db data/log



��mongodb�д��������ļ�mongodb.conf
��� vim ./mongodb.conf
���ݣ�
# ���ö�дȨ��
sudo chmod 666 data/db data/log
# ���ݿ����ݴ��Ŀ¼
dbpath=/usr/local/mongodb/data/db
# ��־�ļ����Ŀ¼
logpath=/usr/local/mongodb/data/log/mongodb.log
# ��־׷�ӷ�ʽ
logappend=true
# �˿�
port=27017
# �Ƿ���֤
auth=true
# ���ػ����̷�ʽ�ں�̨����
fork=true
# Զ������Ҫָ��ip�������޷����ӣ�0.0.0.0��������ip����
bind_ip=0.0.0.0

���û���
��
sudo vim /etc/profile
ĩβ������ݣ�
export MONGODB_HOME=/usr/local/mongodb
export PATH=$PATH:$MONGODB_HOME/bin
����profile�ļ�

# ��̨��������
mongod -f /usr/local/mongodb/mongodb.conf 

# ����mongo ---mongo

���÷���ǽ
systemctl status firewalld �鿴����ǽ״̬
systemctl start firewalld ��������ǽ
# ����27017 �˿�
sudo firewall-cmd --zone=public --add-port=27017/tcp --permanent
# �÷���ǽ������Ч
sudo firewall-cmd --reload
# �鿴���ŵĶ˿ڣ���֤�Ƿ�ɹ�
sudo firewall-cmd --zone=public --list-ports

������״̬
# mongodb ����״̬
ps aux | grep mongo
# ���˿��Ƿ�ɹ�
netstat -lamp | grep 27017
# ���netstat�����Ҳ�������װnetstat
yum install -y net-tools

ֹͣ����
# ͨ������IDɱ��
# ͨ��mongod����ر�mongodb����
mongod -f /home/mongodb/mongodb/mongo.conf

���ÿ�������
vim /lib/systemd/system/mongodb.service
�����Զ������ļ�
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

������������ܹ�����
����
systemctl start mongodb.service
�鿴״̬
systemctl status mongodb.service
�趨��������
systemctl enable mongodb.service
���ط����ļ�mongodb.service
systemctl daemon-reload

����һ������mongoDB�Ľ�ɫ
����
1. mongo
���ݿ���
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
# ��¼
> db.auth("root","")
1
> show tables
system.users
system.version

���������������ʹ�õ��û������ݿ�
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
ʹ�ÿ��ӻ���������Զ��mongodb��ʹ��mongoDBCompass
#### ����
TLS/SSL is disabled. If possible, enable TLS/SSL to avoid security vulnerabilities.
�����޷��������ӣ���Ҫssl
### ���δ�ɹ�
# ��������֤��
## ��һ�������ɸ�֤��
### ���ɸ�֤��
openssl req -out ca.pem -new -x509 -days 3650
### ������
openssl req -out ca.pem -new -x509 -days 3650 -subj "/C=CN/ST=BeiJing/O=bigdata/CN=server1/CN=yellowcong/emailAddress=yellowcong@qq.com"
### ���ֽ��
[wymusic@ ssl]$ ls
ca.pem  privkey.pem
## �ڶ����� ���ɷ����֤��
###  ���ɷ�������˽Կ
openssl genrsa -out server.key 2048
### ���ɷ������������ļ� cat server.req
/**
#CN=localhost ��mongo�������еĽڵ�������Ϣ������Բ��Ͼͻᱨ��
 */
openssl req -key server.key -new -out server.req 
/** -subj "/C=CN/ST=JS/O=bigdata/CN=server1/CN=localhost/emailAddress=2298930148@qq.com"
 */
### ���ɷ�������֤��
openssl x509 -req -in server.req -CA ca.pem -CAkey privkey.pem -CAcreateserial -out server.crt -days 3650

### �ϲ���������˽Կ�ͷ�������֤�飬����server.pem
cat server.key server.crt > server.pem

### У���������pem�ļ�
openssl verify -CAfile ca.pem server.pem
### ���ֽ��
[wymusic@iZuf6g411frzx7ezcnnv92Z ssl]$ openssl x509 -req -in server.req -CA ca.pem -CAkey privkey.pem -CAcreateserial -out server.crt -days 3650
Signature ok
subject=C = CN, ST = JS, O = bigdata, CN = server_mongodb, CN = localhost, emailAddress = 2298930148@qq.com
Getting CA Private Key
Enter pass phrase for privkey.pem:
[wymusic@iZuf6g411frzx7ezcnnv92Z ssl]$ cat server.key server.crt > server.pem
[wymusic@iZuf6g411frzx7ezcnnv92Z ssl]$ openssl verify -CAfile ca.pem server.pem
server.pem: OK

## �������֣����ɿͻ���֤��
### ���ɿͻ���˽Կ
openssl genrsa -out client.key 2048
### ���ɿͻ��������ļ�
#CN=localhost ��mongo�����������ַ�������Ҫ�����Լ�ҵ������޸Ĵ���
openssl req -key client.key -new -out client.req -subj "/C=CN/ST=JS/O=bigdata/CN=server1/CN=localhost/emailAddress=2298930148@qq.com"
### ���ɿͻ���֤��
openssl x509 -req -in client.req -CA ca.pem -CAkey privkey.pem -CAserial ca.srl  -out client.crt -days 3650

### �ϲ��ͻ���˽Կ�Ϳͻ���֤�飬����client.pem
cat client.key client.crt > client.pem

### У��ͻ���pem�ļ�
openssl verify -CAfile ca.pem client.pem
### �������
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

# ���÷����
## ��������ļ� mongodb.conf
1. cat <<EOF > /home/wymusic/mongodb/mongodb/mongodb.conf
2. ֱ�������ļ�
#���ݿ����ݴ��Ŀ¼
dbpath = /home/wymusic/mongodb/mongodb/data/db
#��־�ļ����Ŀ¼
logpath = /home/wymusic/mongodb/mongodb/data/log/mongodb.conf
#��־׷�ӷ�ʽ
logappend = true
#�˿�
port = 27017
#�Ƿ���֤
auth = true
#���ػ����̵ķ�ʽ�ں�̨����
fork = true
#Զ������ָ��ip�������޷����ӣ�һ�㲻������
bind_ip = 0.0.0.0
#���ͬʱ������
maxConns = 5
#ÿ��д����¼һ��������־��ͨ��journal�������¹����д������ݣ���
journal = true
#��ʹ崻�������ʱwiredtiger���Ƚ����ݻָ������һ�ε�checkpoint�㣬Ȼ���طź�����journal��־���ָ���
storageEngine = wiredTiger  #�洢������mmapv1��wiretiger��mongorocks
Shell 
mongo --sslAllowInvalidCertificates --sslAllowInvalidHostnames --ssl --sslPEMKeyFile /usr/local/mongo/ssl/client.pem --sslCAFile /usr/local/mongo/ssl/ca.pem --host 127.0.0.1
# ȷ����Ҫʹ�÷���
## ����ʹ�÷������
��װss5 ��Ҫ������
yum install gcc openldap-devel pam-devel openssl-devel
ʹ�����������ȡss5
wget https://sourceforge.net/projects/ss5/files/ss5/3.8.9-8/ss5-3.8.9-8.tar.gz
��ѹ�ļ�
tar zxvf ./ss5-3.8.9-8.tar.gz
# �������н������������ȷ�������ص��Ƿ���������̨û�����ö˿�ͬ�У���Ҫͨ������������̨���ÿɷ��еĶ˿�
�������
mongodb://PJMVSSM:******@IP:PORT/?authSource=nobody&readPreference=primary&directConnection=true&ssl=false