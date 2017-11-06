import unittest
from models import test_class
import time
import inspect
import os
from selenium import webdriver

class Test_Case(test_class.Test_Class):
    file_name = __file__.split("\\")[-1].split(".")[0]
    
    def test_address_import_export(self):
        #アドレスインポート

        file_list = self.params_j["file_list_address"]
        data_folder = self.params_j["data_folder"]
        #address_list = [name.split("_")[-1] for name in file_list]
        address_book_name = self.params_j["address_book_name"]

        base_path=os.getcwd()

        self.confirm_address_book(keyword="連絡先")

        #インポート
        for file_n in file_list:
            path = os.path.join(base_path, data_folder, file_n) + ".tgz"

            self.setting_page()
            self.select_datatype_import(select=2)

            self.xpath = "//settings-import-export//input[@type='file']"
            time.sleep(1)
            el = self.browser.find_element_by_xpath(self.xpath)
            time.sleep(1)
            el.send_keys(path)
            
            #self.upload_file(path)
            self.file_import()
            self.assert_message("インポートに成功しました")

            self.confirm_address_book(keyword=address_book_name)
            #self.delete_mail_box(file_n.split("_")[-1])

        #アドレスエクスポート

        self.setting_page()
        self.select_datatype_export(select=2)

        self.file_export()

if __name__ == '__main__':
    unittest.main()