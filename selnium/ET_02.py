import unittest
from models import test_class
import time
import inspect
import os
from selenium import webdriver

class Test_Case(test_class.Test_Class):
    file_name = __file__.split("\\")[-1].split(".")[0]
    not_login = 1

    def test_ET_02(self):
        #管理者画面　
        # ログイン、ログアウト、一覧取得、保存、編集、削除

        # self.URL = self.params_j["URL"]
        # id_v = self.params_j["id_v"]
        # pd_v = self.params_j["pd_v"]
        self.URL = self.URL_admin
        id_v = self.id_admin
        pd_v = self.pd_admin
        operator_id = self.params_j["operator_id"]
        operator_pd = self.params_j["operator_pd"]
        operator_name = self.params_j["operator_name"]
        operator_name_new = self.params_j["operator_name_new"]
        operator_address = self.params_j["operator_address"]

        #ログイン
        self.login_admin(id_v=id_v, pd_v=pd_v)

        #管理者保存
        self.new_operator()
        self.edit_operator(id_v=operator_id, pd_v=operator_pd,
                        name_v=operator_name, address_v=operator_address)

        self.xpath = "//*[contains(text(),'{}')]".format(operator_name)
        self.assertTrue(self.action(do="", assert_if=1, capture=1))

        #管理者編集
        self.change_operator(name_v=operator_name)
        self.edit_operator(name_v=operator_name_new)

        self.xpath = "//*[contains(text(),'{}')]".format(operator_name_new)
        self.assertTrue(self.action(do="", assert_if=1, capture=1))

        #管理者削除
        self.delete_operator(name_v=operator_name_new)

        self.xpath = "//*[contains(text(),'{}')]".format(operator_name_new)
        self.assertFalse(self.action(do="", sleep=2, capture=1, assert_if=1, false_is_error=0))

        #ログアウト
        self.logout_admin()
        self.assert_message("ログアウトが完了しました")


if __name__ == '__main__':
    unittest.main()