import unittest
from models import test_class
import time
import inspect

file_name = __file__.split("\\")[-1].split(".")[0]

class Test_Case(test_class.Test_Class):
    file_name = __file__.split("\\")[-1].split(".")[0]
    
    def test_MO_01(self):
        
        mail_box_from = self.params_j["mail_box_from"]
        mail_subject = self.params_j["mail_subject"]
        mail_box_to = self.params_j["mail_box_to"]
        mail_box_delete = self.params_j["mail_box_delete"]
        mail_subject_delete = self.params_j["mail_subject_delete"]

        self.mail_page()

        #フラグを付ける
        self.select_mail(mail_box=mail_box_from, keyword=mail_subject)
        self.set_flag_to_mail()
        self.assert_message("フラグが付けられました")
        self.confirm_mail(mail_box=mail_box_from, mail_subject=mail_subject)

        #フラグを外す
        self.select_mail(mail_box=mail_box_from, keyword=mail_subject)
        self.set_flag_to_mail(set=False)
        self.assert_message("フラグが外され")
        self.confirm_mail(mail_box=mail_box_from, mail_subject=mail_subject)

        #メールを移動
        self.select_mail(mail_box=mail_box_from, keyword=mail_subject)
        self.move_mail(mail_box=mail_box_to)
        self.assert_message("に移動しました")

        #メールを戻す
        self.mail_page()
        self.select_mail(mail_box=mail_box_to, keyword=mail_subject)
        self.move_mail(mail_box=mail_box_from)
        self.assert_message("に移動しました")

        #メールを削除
        self.mail_page()
        self.select_mail(mail_box=mail_box_delete, keyword=mail_subject_delete)
        self.delete_mail()
        self.assert_message("ゴミ箱に移動しました")

        self.select_mail(mail_box="ゴミ箱", keyword=mail_subject_delete)
        self.delete_mail()
        self.assert_message("メッセージを削除しました")

if __name__ == '__main__':
    unittest.main()