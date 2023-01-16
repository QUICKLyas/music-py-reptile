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
# ��������֤��
## ��һ�������ɸ�֤��
### ���ɸ�֤��
openssl req -out ca.pem -new -x509 -days 3650
### ������
openssl req -out ca.pem -new -x509 -days 3650 -subj "/C=CN/ST=BeiJing/O=bigdata/CN=server1/CN=yellowcong/emailAddress=yellowcong@qq.com"
���
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
## ���ɷ�������֤��
openssl x509 -req -in server.req -CA ca.pem -CAkey privkey.pem -CAcreateserial -out server.crt -days 3650

## �ϲ���������˽Կ�ͷ�������֤�飬����server.pem
cat server.key server.crt > server.pem

## У���������pem�ļ�
openssl verify -CAfile ca.pem server.pem

# ������Կ 
