import unittest
from models import test_class
import time
import inspect
import os

class Test_Case(test_class.Test_Class):
    file_name = __file__.split("\\")[-1].split(".")[0]

    def test_AD_03(self):
        #AD_03　プロフィールアップロード、ダウンロード

        data_folder = self.params_j["data_folder"]
        file_name = self.params_j["file_name"]

        base_path=os.getcwd()
        path = os.path.join(base_path, data_folder)
        path = os.path.join(path, file_name)

        address_book = self.params_j["address_book"]
        address_download = self.params_j["address_download"]
        address_upload = self.params_j["address_upload"]

        #プロフィール画像アップロード
        self.address_page()
        self.select_address(address_book=address_book, address=address_upload)
        self.edit_address_button()
        self.upload_profile_img(path)

        self.xpath = "//img[contains(@class,'avatar')]"
        self.action(do="", sleep=2, capture=1)

        #形式チェックで保存できない場合の対応コード
        self.xpath="//p[contains(text(),'その他')]/parent::*/parent::*//div[@class='btn']"
        self.action()
        self.save_address_button()

        #プロフィールダウンロード
        self.address_page()
        self.open_address(address_book=address_book, address=address_download, capture=0)

        self.xpath = "//img[contains(@class,'avatar')]"
        self.action(do="", sleep=2, capture=1)

        self.address_page()
    


if __name__ == '__main__':
    unittest.main()