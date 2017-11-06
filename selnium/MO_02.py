import unittest
from models import test_class
import time
import inspect
from selenium import webdriver

file_name = __file__.split("\\")[-1].split(".")[0]

class Test_Case(test_class.Test_Class):
    file_name = __file__.split("\\")[-1].split(".")[0]
    
    def test_MO_02(self):
        #オリジナルメール取得
        
        mail_box = self.params_j["mail_box"]
        mail_subject = self.params_j["mail_subject"]

        self.mail_page()

        self.select_mail(mail_box=mail_box, keyword=mail_subject)
        self.original_mail()

        self.browser.switch_to.window(self.browser.window_handles[1])

        self.xpath = "//body"
        self.action(do="", capture=1)

        self.browser.close()
        self.browser.switch_to.window(self.browser.window_handles[0])


if __name__ == '__main__':
    unittest.main()