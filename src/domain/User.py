import myutils.c_ua as cua
import myutils.c_urls as curls


class UserLoginCellPhone(object):
    def __init__(self,
                 phone=curls.urls['user_login_cellphone']['phone'],
                 password=curls.urls['user_login_cellphone']['password']) -> None:
        self.phone = phone
        self.password = password
        self.url = curls.urls['user_login_cellphone']['head'] + \
            self.phone + self.password
        self.head = {
            'User-Agent': cua.ua
        }

    def getPhone(self):
        return self.phone

    def setPhone(self, phone=curls.urls['user_login_cellphone']['ph']):
        self.phone += str(phone)
        self.setUrl("")

    def getPassword(self):
        return self.password

    def setPassword(self, password=curls.urls['user_login_cellphone']['pa']):
        self.password += str(password)
        self.setUrl("")

    def getUrl(self):
        return self.url

    def setUrl(self, url):
        if(url == ""):
            self.url = curls.urls['user_login_cellphone']['head'] + \
                self.phone + self.password
        else:
            self.url = url

    def getHead(self):
        return self.head

    def setHead(self, head):
        self.iheadd = head
