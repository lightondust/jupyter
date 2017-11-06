import unittest
from models import test_class
import time
import inspect
import os
from selenium import webdriver

file_name = __file__.split("\\")[-1].split(".")[0]

class Test_Case(test_class.Test_Class):
    file_name = __file__.split("\\")[-1].split(".")[0]
    not_login = 1

    # LOGIN情報
    RECEIVE_USER_LOGIN_ADD = ""
    RECEIVE_USER_LOGIN_PW = ""
    TRANSFER_USER_LOGIN_ADD = ""
    TRANSFER_USER_LOGIN_PW = ""

    TRANSFER_SETTING_NAME = ""
    TRANSFER_SETTING_ADD = ""

    MAIL_SUBJECT = ""
    MAIL_CONTENTS = ""
    MAIL_KEYWORD = ""

    def test_outside_account(self):

        self.init_data()

        # 蛯名君・和田君のメールアドレス情報 OK

        # 受信ユーザのデータ確認
        self.receive_user_mail_search()

        self.transfer_login_and_setting_view()

        # 送信設定
        self.transfer_setting(trans_title=self.TRANSFER_SETTING_NAME , trans_mail=self.TRANSFER_SETTING_ADD)
        self.transfer_active(title=self.TRANSFER_SETTING_NAME)

        # メール転送
        self.mail_page()
        self.create_mail()
        self.set_address(mail_address=self.TRANSFER_USER_LOGIN_ADD)
        self.set_mail_content(mail_content=self.MAIL_CONTENTS)
        self.set_mail_subject(mail_subject=self.MAIL_SUBJECT)
        self.send_mail_button()

        # 送信されたことを送信済みメールボックスで確認
        # self.confirm_mail()
        self.confirm_mail_box(keyword="送信済みメール") #ここで送信済みメールボックスに移動しない
        self.searchMail(searchKey=self.MAIL_SUBJECT)
        self.logout()

        # 受信ユーザのデータ確認
        self.receive_user_mail_search()

        # 自動転送の設定削除
        self.transfer_login_and_setting_view()

        # 自動転送の設定を削除
        self.transfer_del(title=self.TRANSFER_SETTING_NAME)


    def receive_user_mail_search(self):
        
        # 和田君のメールボックスにメールが転送されていること。
        self.init_login(account_id=self.RECEIVE_USER_LOGIN_ADD, account_pw=self.RECEIVE_USER_LOGIN_PW)
        self.confirm_mail_box()
        self.searchMail(searchKey=self.MAIL_SUBJECT)

        # self.mailListOnClick(searchKey=self.MAIL_SUBJECT)

        pass


    def transfer_login_and_setting_view(self):
        self.logout()
        # 送信済みユーザ
        self.init_login(account_id=self.TRANSFER_USER_LOGIN_ADD, account_pw=self.TRANSFER_USER_LOGIN_PW)

        # 設定画面に遷移
        self.showSettingView(moveSetview=True, showType=6)

        pass
        

    def init_data(self):
        # LOGIN情報
        # self.RECEIVE_USER_LOGIN_ADD = self.params_j["RECEIVE_USER_LOGIN_ADD"]
        # self.RECEIVE_USER_LOGIN_PW = self.params_j["RECEIVE_USER_LOGIN_PW"]
        # self.TRANSFER_USER_LOGIN_ADD = self.params_j["TRANSFER_USER_LOGIN_ADD"]
        # self.TRANSFER_USER_LOGIN_PW = self.params_j["TRANSFER_USER_LOGIN_PW"]

        self.RECEIVE_USER_LOGIN_ADD = self.id_MD_02_recieve
        self.RECEIVE_USER_LOGIN_PW = self.pd_MD_02_recieve
        self.TRANSFER_USER_LOGIN_ADD = self.id_MD_02_transfer
        self.TRANSFER_USER_LOGIN_PW = self.pd_MD_02_transfer

        self.TRANSFER_SETTING_NAME = self.params_j["TRANSFER_SETTING_NAME"]
        self.TRANSFER_SETTING_ADD = self.params_j["TRANSFER_SETTING_ADD"]

        self.MAIL_SUBJECT = self.params_j["MAIL_SUBJECT"]
        self.MAIL_CONTENTS = self.params_j["MAIL_CONTENTS"]
        self.MAIL_KEYWORD = self.params_j["MAIL_KEYWORD"]

        pass


    def init_login(self, account_id="", account_pw=""):
        # LOGIN 
        print("LOGIN")
        self.login(id_v=account_id, pd_v=account_pw, capture=1)


    def init_mail_import(self):
        ###################
        # INIT
        ###################

        # 設定画面のImport/Export機能画面を表示
        print("設定画面のImport/Export機能画面を表示")
        self.showSettingView(moveSetview=True, showType=8)

        # メールのインポート
        print("run_mail_import")
        self.mailImport(mailPathList=self.FILE_LIST_MAIL, folderName=self.DATA_FOLDER)

        # メールボックスの確認
        print("メールボックス： " + self.IMPORT_MAILBOX_NAME)
        self.confirm_mail(mail_box=self.IMPORT_MAILBOX_NAME, mail_subject=self.IMPORT_MAIL_SUB)

        

if __name__ == '__main__':
    unittest.main()