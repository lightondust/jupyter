import unittest
from models import test_class
import time
import inspect
import os
from selenium import webdriver

class Test_Case(test_class.Test_Class):
    file_name = __file__.split("\\")[-1].split(".")[0]
    not_login = 1

    def test_ET_03(self):
        #保守者画面　
        #ログイン、ログアウト、パスワード変更

        # self.URL = self.params_j["URL"]
        # id_v = self.params_j["id_v"]
        # pd_v = self.params_j["pd_v"]
        # pd_n = self.params_j["pd_n"]
        self.URL = self.URL_operator
        id_v = self.id_operator
        pd_v = self.pd_operator
        pd_n = self.pd_operator_new
        mail_address = self.params_j["mail_address"]

        #ログイン
        self.login_operator(id_v=id_v, pd_v=pd_v, address_v=mail_address)

        #ログアウト
        self.logout()
        self.assert_message("ログアウトが完了しました")

        #パスワード変更（ログイン画面読み込んでから）
        self.get_url(self.URL)
        self.change_operator_pd(id_v=id_v, pd_v=pd_v, pd_n=pd_n)

        #旧パスワードログイン失敗
        self.get_url(self.URL)
        self.login_operator(id_v=id_v, pd_v=pd_v, address_v=mail_address, assert_if=False)
        self.assert_message("正しくありません")

        #新パスワードログイン
        self.get_url(self.URL)
        self.login_operator(id_v=id_v, pd_v=pd_n, address_v=mail_address)
        self.logout()

        #パスワード戻す
        self.get_url(self.URL)
        self.change_operator_pd(id_v=id_v, pd_v=pd_n, pd_n=pd_v)


if __name__ == '__main__':
    unittest.main()