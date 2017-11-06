import unittest
from models import test_class
import time
import inspect

class Test_Case(test_class.Test_Class):
    file_name = __file__.split("\\")[-1].split(".")[0]
    not_login=1
    
    def test_login(self):
        #セッション確認

        self.assertFalse(self.get_cookies(), "ログイン前セッションがないこと")
        self.login(self.id_v, self.pd_v, assert_if=True)
        self.assertTrue(self.get_cookies(), "ログイン後セッションがセットされたこと")

if __name__ == '__main__':
    unittest.main()