import unittest
from models import test_class
import time
import inspect

file_name = __file__.split("\\")[-1].split(".")[0]

class Test_Case(test_class.Test_Class):
    file_name = __file__.split("\\")[-1].split(".")[0]

    def test_tag(self):
        TAG_NAME = self.params_j["TAG_NAME"]
        mail_subject = self.params_j["mail_subject"]
        mail_box = self.params_j["mail_box"]

        # 新規タグの作成
        self.save_tag(tag_name=TAG_NAME)

        # メールを確認する
        self.confirm_mail(mail_box=mail_box, mail_subject=mail_subject)

        # タグの紐付け（チキンメール）
        self.tag_setinng_for_mail(mail_box=mail_box, mail_subject=mail_subject, tag_name=TAG_NAME)

        # メールを確認する
        self.confirm_mail(mail_box=mail_box, mail_subject=mail_subject)

        # タグの確認
        self.showTagMail(target=TAG_NAME)

        # メールを確認する
        self.confirm_mail(mail_box=mail_box, mail_subject=mail_subject)

        # タグのカラーを変更
        self.change_tag_color(tag_name=TAG_NAME, color_num="6")

        # タグの削除
        self.delete_tag(tag_name=TAG_NAME)

        # メールを確認する
        self.confirm_mail(mail_box=mail_box, mail_subject=mail_subject)

        pass


if __name__ == '__main__':
    unittest.main()