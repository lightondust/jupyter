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

    def test_tag(self):
        # LOGIN情報
        # self.LOGIN_ADD = self.params_j["LOGIN_ADD"]
        # self.LOGIN_PW = self.params_j["LOGIN_PW"]
        self.LOGIN_ADD = self.id_v
        self.LOGIN_PW = self.pd_v

        self.TAG_NAME = self.params_j["TAG_NAME"]
        # インポート情報
        self.FILE_LIST_MAIL = self.params_j["FILE_LIST_MAIL"]
        self.DATA_FOLDER = self.params_j["DATA_FOLDER"]
        self.IMPORT_MAILBOX_NAME = self.params_j["IMPORT_MAILBOX_NAME"]
        self.IMPORT_MAIL_SUB = self.params_j["IMPORT_MAIL_SUB"]
        self.CONFIRM_MAIL_SUB = self.params_j["CONFIRM_MAIL_SUB"]

        
        self.init_login()
        self.init_mail_import()
        
        ###################
        # FILTER SETTING
        ###################

        # 設定画面のImport/Export機能画面を表示
        print("設定画面のImport/Export機能画面を表示")
        self.showSettingView(moveSetview=True, showType=3)
        time.sleep(1)

        # Filterの作成
        self.fiter_create()
        time.sleep(1)

        # Filterの実行
        self.run_filter()
        time.sleep(1)

        # メールボックスの確認
        print("メールボックス： " + self.IMPORT_MAILBOX_NAME)
        self.confirm_mail(mail_box=self.IMPORT_MAILBOX_NAME, mail_subject=self.CONFIRM_MAIL_SUB)
        time.sleep(1)

        # 設定画面のImport/Export機能画面を表示
        print("設定画面のImport/Export機能画面を表示")
        self.showSettingView(moveSetview=True, showType=3)
        time.sleep(1)

        # フィルターの削除
        self.fiter_del()
        time.sleep(1)

        self.delete_mail_box(keyword=self.IMPORT_MAILBOX_NAME)
        time.sleep(1)

        self.tagMove(0)
        time.sleep(1)


    def init_login(self):
        # LOGIN 
        print("LOGIN")
        self.login(id_v=self.LOGIN_ADD, pd_v=self.LOGIN_PW, capture=1)


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