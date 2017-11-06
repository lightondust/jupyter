import unittest
from models import test_class
import time
import inspect
import os
from selenium import webdriver

class Test_Case(test_class.Test_Class):
    file_name = __file__.split("\\")[-1].split(".")[0]
    
    def test_mail_import_export(self):
        #メールインポート

        file_list = self.params_j["file_list_mail"]
        data_folder = self.params_j["data_folder"]
        mail_folder_list = [name.split("_")[-1] for name in file_list]

        base_path=os.getcwd()

        #インポート
        for file_n in file_list:
            path = os.path.join(base_path, data_folder, file_n) + ".tgz"

            self.setting_page()
            self.select_datatype_import(select=1)

            self.xpath = "//settings-import-export//input[@type='file']"
            time.sleep(1)
            el = self.browser.find_element_by_xpath(self.xpath)
            time.sleep(1)
            el.send_keys(path)
            
            self.file_import()
            self.assert_message("インポートに成功しました")

            self.confirm_mail_box(file_n.split("_")[-1])

        #メールエクスポート

        self.setting_page()
        self.select_datatype_export(select=1)

        self.file_export()

        time.sleep(5)


if __name__ == '__main__':
    unittest.main()