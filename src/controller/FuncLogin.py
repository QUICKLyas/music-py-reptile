from Crypto.Cipher import AES

import myutils.c_ua as cua
import base64
import random
import codecs
import requests
from http.cookiejar import LWPCookieJar
import hashlib


class FuncLogin(object):

    def __init__(self) -> None:
        self.arg2 = "010001"
        self.arg3 = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
        self.arg4 = "0CoJUm6Qyw8W8jud"
        self.session = requests.Session()
        self.session.headers = {
            "Referer": "https://music.163.com/",
            "User-Agent": cua.uar
        }
        self.session.cookies = LWPCookieJar(
            filename="/mnt/f/IDE/Python/reptile/data/cookie.txt")
        self.__get_random_str()
        pass

    def __AES_encrypt(self, text, key):
        '''
        获取到加密后的数据
        :param text: 首先CBC加密方法，text必须位16位数据
        :param key: 加密的key
        :return: 加密后的字符串
        '''
        iv = "0102030405060708"
        pad = 16 - len(text) % 16
        if isinstance(text, str):
            text = text + pad * chr(pad)
        else:
            text = text.decode("utf-8") + pad*chr(pad)
        aes = AES.new(key=bytes(key, encoding="utf-8"),
                      mode=2, iv=bytes(iv, encoding="utf-8"))
        res = aes.encrypt(bytes(text, encoding="utf-8"))
        res = base64.b64encode(res).decode("utf-8")
        return res

    def __get_encText(self, args1):
        encText = self.__AES_encrypt(args1, self.arg4)
        encText = self.__AES_encrypt(encText, self.random_16_str)
        return encText

    def __get_encSecKey(self):
        text = self.random_16_str[::-1]
        rs = int(codecs.encode(text.encode('utf-8'), 'hex-codec'),
                 16) ** int(self.arg2, 16) % int(self.arg3, 16)
        return format(rs, 'x').zfill(256)

    def __get_random_str(self):
        '''这是16位的随机字符串'''
        str_set = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        random_str = ""
        for i in range(16):
            index = random.randint(0, len(str_set) - 1)
            random_str += str_set[index]
        self.random_16_str = random_str

    def __getFormData(self, args1):
        '''获取到提交的数据'''
        data = {
            "params": self.__get_encText(args1),
            "encSecKey": self.__get_encSecKey()
        }
        return data

    def login(self, username: str = None, password: str = None):
        '''网易云登录'''
        '''
        参数一为构造这样的字典格式
        checkToken: "9ca17ae2e6ffcda170e2e6eed9ee33fb9d9dd6cb7a98ef8eb2d85b879b9ababc6788b6ab96f95afcb8adaabc2af0feaec3b92aadb88ab1c446a1ef0099f65a879f9ba6c85a9bb0a2b9e945f5eca69bd952af95ee9e"
        csrf_token: ""
        password: "5cf36a0d72feb44111716322921ed011"
        phone: "18716758271"
        rememberLogin: "true"
        '''
        api = "https://music.163.com/weapi/login/cellphone?csrf_token="
        headers = {}
        headers["content-type"] = "application/x-www-form-urlencoded"
        headers["user-agent"] = cua.uar
        headers["referer"] = "https://music.163.com/"
        if not username:
            username = input("input your cellphone: ").strip()
        else:
            username = username.strip()
        if not password:
            password = input("input your password: ").strip()
        else:
            password = password.strip()

        self.arg1_login = '{"phone":"%s","password":"%s","rememberLogin":"true","checkToken":"","csrf_token": ""}' % (
            username, hashlib.md5(
                bytes(password, encoding="utf-8")).hexdigest()
        )
        formdata = self.__getFormData(self.arg1_login)
        response = self.session.post(url=api, headers=headers, data=formdata)
        results = response.json()
        print(results)
        # if results['code'] == 200:
        #     self.session.cookies.save()
        #     print("success")
        # else:
        #     print(results["msg"])
