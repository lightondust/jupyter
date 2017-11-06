import unittest
from models import test_class
import time
import inspect
import os
from selenium import webdriver

file_name = __file__.split("\\")[-1].split(".")[0]

class Test_Case(test_class.Test_Class):
    file_name = __file__.split("\\")[-1].split(".")[0]

    def test_MD_04(self):
        #迷惑メール情報変更
        select_1 = 1
        select_2 = 2
        selection = "毎週日曜日"
        select_1_new = 2
        select_2_new = 1
        selection_new = "送信しない"

        self.setting_page()
        self.select_spam_info()
        self.edit_spam_info(select_1=select_1, select_2=select_2,
             selection=selection)
        self.assert_message("設定を変更しています")
        self.assert_message("変更が保存されました", wait_time=15)

        self.setting_page()
        self.select_spam_info()
        self.edit_spam_info(select_1=select_1_new, select_2=select_2_new,
             selection=selection_new)
        self.assert_message("設定を変更しています")
        self.assert_message("変更が保存されました", wait_time=15)

        

if __name__ == '__main__':
    unittest.main()