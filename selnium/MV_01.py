import unittest
from models import test_class
import time
import inspect

class Test_Case(test_class.Test_Class):
    file_name = __file__.split("\\")[-1].split(".")[0]
    
    def test_MV_01(self):
        #メール一覧、メール取得、添付ファイルダウンロード

        mail_box = self.params_j["mail_box"]
        mail_keyword = self.params_j["mail_keyword"]
        file_name = self.params_j["file_name"]

        #メール画面
        self.mail_page()

        #メールボックス指定してメールをダブルクリック
        self.mail_open(mail_box=mail_box, keyword=mail_keyword, capture=1)

        #添付ファイルダウンロード
        self.download_attachment(file_name=file_name, capture=1)


if __name__ == '__main__':
    unittest.main()