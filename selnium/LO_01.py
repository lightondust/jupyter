import unittest
from models import test_class
import time
import inspect

class Test_Case(test_class.Test_Class):
    file_name = __file__.split("\\")[-1].split(".")[0]
    not_login=1
    
    def test_login(self):
        #ログイン、パスワード変更、セッション確認

        # id_v = self.params_j["id_v"]
        # pd = self.params_j["PD"]
        # pd_new = self.params_j["PD_NEW"]

        id_v = self.id_LO_01
        pd = self.pd_LO_01
        pd_new = self.pd_LO_01_new

        #ログイン
        self.login(id_v, pd, assert_if=True)

        #パスワード変更
        self.setting_page()
        self.change_password(pd, pd_new)

        #ログアウト
        self.logout()
        self.assert_message("ログアウトが完了しました")

        #旧pdでログイン失敗
        self.login(id_v, pd, assert_if=False)
        self.assert_message("パスワードが正しくありません")
                
        #新pdでログイン
        self.login(id_v, pd_new, assert_if=True)

        #パスワード戻す
        self.setting_page()
        self.change_password(pd_new, pd)


if __name__ == '__main__':
    unittest.main()