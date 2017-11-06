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
    LOGIN_ADD = ""
    LOGIN_PW = ""
    TAG_NAME = ""
    # インポート情報
    FILE_LIST_MAIL = ""
    DATA_FOLDER = ""
    IMPORT_MAILBOX_NAME = ""
    IMPORT_MAIL_SUB = ""

    # 確認用SUB
    CONFIRM_MAIL_SUB = ""

    # 外部アカウント
    GMAIL_ACCOUNT_ADD = ""
    GMAIL_ACCOUNT_ID = ""
    GMAIL_ACCOUNT_PW = ""
    GMAIL_ACCOUNT_NAME = ""
    GMAIL_ACCOUNT_SERVER = ""
    GMAIL_ACCOUNT_SSL = False
    GMAIL_ACCOUNT_AFTER_NAME = ""

    def test_outside_account(self):

        self.init_data()

        ###################
        # 外部アカウント 紐付け
        ###################
        self.init_login(account_id=self.LOGIN_ADD, account_pw=self.LOGIN_PW)

        self.tagMove(2)

        # 設定画面で外部アカウントを紐づける
        self.showSettingView(moveSetview=True, showType=5)
        self.capture()

        # 外部アカウント接続
        self.outside_connection(address=self.GMAIL_ACCOUNT_ADD, id=self.GMAIL_ACCOUNT_ID,
                                pw=self.GMAIL_ACCOUNT_PW, user_name=self.GMAIL_ACCOUNT_NAME, server=self.GMAIL_ACCOUNT_SERVER)

        # メールの確認
        # 1. テスト太郎のメールボックスを開く
        print("メールボックスを確認する")
        self.confirm_outside_box(account_name=self.GMAIL_ACCOUNT_NAME)

        # # フォルダを開く
        print("外部アカウントのフォルダを開く")
        self.confirm_open_outside_box(account_name=self.GMAIL_ACCOUNT_NAME)

        time.sleep(1)


        # # 2. メールフォルダ内の確認
        print("外部アカウントのフォルダを開く [" + self.GMAIL_ACCOUNT_NAME + " : " + "受信箱" + "]")
        self.confirm_mail_box_for_outmail(user_name=self.GMAIL_ACCOUNT_NAME, folder_name="受信箱")
        time.sleep(1)
        self.capture()

        # # フォルダを閉じる
        print("外部アカウントのフォルダを閉じる")
        self.confirm_open_outside_box(account_name=self.GMAIL_ACCOUNT_NAME, isOpen=False)


        # アカウント変更
        # 1. 設定画面から名前を変更
        self.outside_change_user_name(user_name=self.GMAIL_ACCOUNT_NAME, after_name=self.GMAIL_ACCOUNT_AFTER_NAME, pw=self.GMAIL_ACCOUNT_PW)

        # 2. メールボックスの確認
        # フォルダを開く
        print("外部アカウントのフォルダを開く")
        self.confirm_open_outside_box(account_name=self.GMAIL_ACCOUNT_AFTER_NAME)

        time.sleep(1)

        # # 2. メールフォルダ内の確認
        print("外部アカウントのフォルダを開く [" + self.GMAIL_ACCOUNT_AFTER_NAME + " : " + "受信箱" + "]")
        self.tagMove(0)
        self.confirm_mail_box_for_outmail(user_name=self.GMAIL_ACCOUNT_AFTER_NAME, folder_name="受信箱")
        time.sleep(1)
        self.capture()

        # 外部アカウントの削除
        self.outside_disconnect(text=self.GMAIL_ACCOUNT_AFTER_NAME)
        self.showSettingView(moveSetview=True, showType=5)
        time.sleep(1)
        self.capture()

        # 削除後のメールボックスの確認        
        self.tagMove(0)
        time.sleep(1)
        self.capture()
        

    def init_data(self):
        # LOGIN情報
        # self.LOGIN_ADD = self.params_j["LOGIN_ADD"]
        # self.LOGIN_PW = self.params_j["LOGIN_PW"]
        self.LOGIN_ADD = self.id_GA_01
        self.LOGIN_PW = self.pd_GA_01
        self.TAG_NAME = self.params_j["TAG_NAME"]
        # インポート情報
        self.FILE_LIST_MAIL = self.params_j["FILE_LIST_MAIL"]
        self.DATA_FOLDER = self.params_j["DATA_FOLDER"]
        self.IMPORT_MAILBOX_NAME = self.params_j["IMPORT_MAILBOX_NAME"]
        self.IMPORT_MAIL_SUB = self.params_j["IMPORT_MAIL_SUB"]
        self.CONFIRM_MAIL_SUB = self.params_j["CONFIRM_MAIL_SUB"]

        # 外部アカウント
        self.GMAIL_ACCOUNT_ADD = self.params_j["GMAIL_ACCOUNT_ADD"]
        self.GMAIL_ACCOUNT_ID = self.params_j["GMAIL_ACCOUNT_ID"]
        self.GMAIL_ACCOUNT_PW = self.params_j["GMAIL_ACCOUNT_PW"]
        self.GMAIL_ACCOUNT_NAME = self.params_j["GMAIL_ACCOUNT_NAME"]
        self.GMAIL_ACCOUNT_SERVER = self.params_j["GMAIL_ACCOUNT_SERVER"]
        self.GMAIL_ACCOUNT_SSL = self.params_j["GMAIL_ACCOUNT_SSL"]
        self.GMAIL_ACCOUNT_AFTER_NAME = self.params_j["GMAIL_ACCOUNT_AFTER_NAME"]

        pass        


    def init_login(self, account_id="", account_pw=""):
        # LOGIN 
        print("LOGIN")
        self.login(id_v=account_id, pd_v=account_pw, capture=1)



if __name__ == '__main__':
    unittest.main()