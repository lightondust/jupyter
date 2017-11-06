import unittest
from models import test_class
import time
import inspect
import os

class Test_Case(test_class.Test_Class):
    file_name = __file__.split("\\")[-1].split(".")[0]

    def test_spam(self):
        #迷惑メール通報、解除

        mail_box = self.params_j["mail_box"]
        mail_subject = self.params_j["mail_subject"]

        #迷惑メール通報
        self.mail_page()
        self.select_mail(mail_box=mail_box, keyword=mail_subject)
        self.set_spam()
        self.assert_message("通報を受け付けました")
   
        #迷惑メール解除
        self.mail_page()
        self.select_mail(mail_box="迷惑メール", keyword=mail_subject)
        self.set_spam()
        self.assert_message("通報を受け付けました")

        #メールを元のフォルダに戻す
        self.mail_page()
        self.select_mail(mail_box="受信箱", keyword=mail_subject)
        self.move_mail(mail_box=mail_box)
        self.assert_message("に移動しました")

if __name__ == '__main__':
    unittest.main()