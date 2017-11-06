import time
from models import BaseModel

class LoginModel(BaseModel.BaseModel):
    def __init__(self):
        pass


    def login(self, id_v, pd_v, capture=1, assert_if=True):
        """
        capture=0,1でキャプチャする、しない
        """
        URL = self.URL
        self.browser.refresh()
        self.browser.get(URL)          
        self.xpath = "//*[@name='Email']"
        self.action(do="send_keys", content = id_v)
        self.xpath = "//*[@name='Password']"
        self.action(do="send_keys", content = pd_v)
        self.xpath = "//*[@name='Submit']" 
        self.action(capture=capture)

        if assert_if:
            self.xpath = "(//a[contains(@href, '#/mail')])[2]" 
            self.action(do="", sleep=2, capture=capture)

    def logout(self):
        self.xpath = "//header//a[contains(text(),'ログアウト')]"
        self.action(sleep=2)

    def get_cookies(self):
        return self.browser.get_cookies()
   
    def login_operator(self, id_v, pd_v, address_v, capture=1, assert_if=True):
        """
        保守者ログイン
        capture=0,1でキャプチャする、しない
        """
        URL = self.URL
        self.browser.refresh()
        self.browser.get(URL)          
        self.xpath = "//*[@name='operatorId']"
        self.action(do="send_keys", content = id_v)
        self.xpath = "//*[@name='operatorPassword']"
        self.action(do="send_keys", content = pd_v)
        self.xpath = "//*[@name='mailAddress']"
        self.action(do="send_keys", content = address_v, capture=capture)
        self.xpath = "//button[@type='submit']" 
        self.action()

        if assert_if:
            self.xpath = "(//a[contains(@href, '#/mail')])[2]" 
            self.action(do="", sleep=2, capture=capture)

    def change_operator_pd(self,id_v, pd_v, pd_n, capture=1):
        """
        保守者パスワード変更
        """

        self.xpath = "//*[contains(text(),'パスワード変更')]" 
        self.action()

        self.xpath = "//*[@name='operatorId']"
        self.action(do="send_keys", content = id_v)

        self.xpath = "//*[@name='relicPassword']"
        self.action(do="send_keys", content = pd_v)

        self.xpath = "//*[@name='newPassword']"
        self.action(do="send_keys", content = pd_n)

        self.xpath = "//*[@name='checkNewPassword']"
        self.action(do="send_keys", content = pd_n)

        self.xpath = "//*[contains(text(),'変更')]" 
        self.action(do="", capture=capture)
        self.action()



    def login_admin(self, id_v, pd_v, capture=1, assert_if=True):
        """
        管理者ログイン
        capture=0,1でキャプチャする、しない
        """
        URL = self.URL
        self.browser.refresh()
        self.browser.get(URL)          
        self.xpath = "//*[@name='adminId']"
        self.action(do="send_keys", content = id_v)
        self.xpath = "//*[@name='adminPass']"
        self.action(do="send_keys", content = pd_v, capture=capture)
        self.xpath = "//*[@name='Submit']" 
        self.action()

        if assert_if:
            self.xpath = "//*[contains(text(),'追加') and @class='menuText']" 
            self.action(do="", sleep=2, capture=capture)

    def logout_admin(self):
        """
        管理者ログアウト
        """
        self.xpath = "//*[contains(text(),'ログアウト')]"
        self.action(sleep=2)


    def new_operator(self):
        #管理者保存ボタン
        self.xpath = "//*[contains(text(),'追加') and @class='menuText']" 
        self.action()

    def change_operator(self, name_v=""):
        #管理者更新ボタン
        self.xpath = "//*[contains(text(),'{}')]/parent::*/following-sibling::*//*[contains(text(),'更新')]".format(name_v)
        self.action()

    def edit_operator(self, id_v="", pd_v="", name_v="", address_v=""):
        #管理者編集

        if id_v:
            self.xpath = "//*[contains(@ng-reflect-name,'operatorId')]"
            self.action(do="send_keys", content = id_v)

        if pd_v:
            self.xpath = "//*[contains(@class,'isOn')]//*[contains(@ng-reflect-name,'operatorPassword') or contains(@ng-reflect-name,'updaterPassword')]"
            self.action(do="send_keys", content = pd_v)

        if name_v:
            self.xpath = "//*[contains(@class,'isOn')]//*[contains(@ng-reflect-name,'operatorName') or contains(@ng-reflect-name,'updaterName')]"
            self.action(do="send_keys", content = name_v)
        
        if address_v:
            self.xpath = "//*[contains(@class,'isOn')]//*[contains(@ng-reflect-name,'operatorMailAddress') or contains(@ng-reflect-name,'updaterMailAddress')]"
            self.action(do="send_keys", content = address_v)

        self.xpath = "//*[contains(@class,'isOn')]//*[contains(@class,'modalWindow')]//*[contains(text(),'追加') or contains(text(),'変更')]"
        self.action(do="", capture=1)
        self.action()


    def delete_operator(self, name_v=""):
        #管理者削除
        self.xpath = "//*[contains(text(),'{}')]/parent::*/following-sibling::*//*[contains(text(),'削除')]".format(name_v)
        self.action()

        self.xpath = "//modal-dialog//*[contains(text(),'OK')]"
        self.action(do="",capture=1)
        self.action()

