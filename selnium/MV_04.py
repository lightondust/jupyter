import unittest
from models import test_class
import time
import inspect
import os
from selenium import webdriver

file_name = __file__.split("\\")[-1].split(".")[0]

class Test_Case(test_class.Test_Class):
    file_name = __file__.split("\\")[-1].split(".")[0]
    
    def test_MV_04(self):
        #オートコンプリート

        mail_subject = self.params_j["mail_subject"]
        mail_content = self.params_j["mail_content"]
        mail_address = self.params_j["mail_address"]
        mail_address_keyword = self.params_j["mail_address_keyword"]


        #オートコンプリート有効にする
        self.setting_page()
        self.use_autocomplete(select=1)
        self.save_change()

        #メール送信
        self.mail_page()
        self.create_mail()
        self.set_address(mail_address=mail_address)
        self.set_mail_content(mail_content=mail_content)
        self.set_mail_subject(mail_subject=mail_subject)
        self.send_mail_button()

        #オートコンプリート確認
        self.mail_page()
        self.create_mail()
        self.set_address(mail_address=mail_address_keyword, deal_auto_complete=False)

        #オートコンプリートリセット
        self.xpath = "//*[contains(text(),'{}')]/parent::*//*[contains(text(),'無視')]".format(mail_address)
        self.assertTrue(self.action(do="",capture=1, assert_if=1))
        self.action()

        self.assert_message("リセットされました")

        self.xpath = "//*[contains(text(),'{}')]/parent::*//*[contains(text(),'無視')]".format(mail_address)
        self.assertFalse(self.action(do="",capture=1, assert_if=1, false_is_error=0))
        

if __name__ == '__main__':
    unittest.main()