import unittest
from models import test_class
import time
import inspect
import os

class Test_Case(test_class.Test_Class):
    file_name = __file__.split("\\")[-1].split(".")[0]
    
    def test_MD_05(self):
        #必着設定

        file_list = self.params_j["file_list"]
        data_folder = self.params_j["data_folder"]
        white_selection = self.params_j["white_selection"]
        white_content = self.params_j["white_content"]
        white_content_new = self.params_j["white_content_new"]

        base_path = os.getcwd()
        file_n = file_list[0]
        path = os.path.join(base_path, data_folder, file_n)

        self.setting_page()
        self.select_white_list(selection="From")
        self.import_white_list(path=path)
        self.assert_message("設定を変更しています")
        self.assert_message("変更が保存されました", wait_time=15)

        self.setting_page()
        self.select_white_list(selection="From")
        self.export_white_list()
        self.save_white_list()
        self.assert_message("設定を変更しています")
        self.assert_message("変更が保存されました", wait_time=15)

        for selection in white_selection:
            
            #編集1
            self.setting_page()
            self.select_white_list(selection=selection)
            self.edit_white_list(content=white_content[selection], capture=1)
            self.save_white_list()
            self.assert_message("設定を変更しています")
            self.assert_message("変更が保存されました", wait_time=15)

            #編集2
            self.setting_page()
            self.select_white_list(selection=selection)
            self.edit_white_list(content=white_content_new[selection], capture=1, clear=True)
            self.save_white_list()
            self.assert_message("設定を変更しています")
            self.assert_message("変更が保存されました", wait_time=15)



if __name__ == '__main__':
    unittest.main()