import unittest
from models import test_class
import time
import inspect
import os
from selenium import webdriver

class Test_Case(test_class.Test_Class):
    file_name = __file__.split("\\")[-1].split(".")[0]

    def test_MO_03(self):
        #フォルダ操作
        mail_box = self.params_j["mail_box"]
        mail_box_new = self.params_j["mail_box_new"]
        move_to = self.params_j["move_to"]

        #フォルダ作成
        self.create_mail_box()
        self.edit_mail_box(mail_box=mail_box, color=3)

        #フォルダ削除
        self.delete_mail_box(keyword=mail_box)

        #フォルダ作成
        self.create_mail_box()
        self.edit_mail_box(mail_box=mail_box, color=4)

        #フォルダ編集、移動
        self.change_mail_box(mail_box=mail_box)
        self.edit_mail_box(mail_box=mail_box_new, 
                            move_to=move_to, color=5)

        #移動されたフォルダを確認、削除
        try:
            self.xpath = "//a[contains(text(),'{}')]/parent::*/preceding-sibling::*//*[@class='btn btnNest']".format(move_to)
            self.action(capture_false=0)
        except:
            pass

        self.delete_mail_box(keyword=mail_box_new)


if __name__ == '__main__':
    unittest.main()