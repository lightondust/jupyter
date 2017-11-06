import unittest
from models import test_class
import time
import inspect
import os

file_name = __file__.split("\\")[-1].split(".")[0]

class Test_Case(test_class.Test_Class):
    file_name = __file__.split("\\")[-1].split(".")[0]
    # not_login = 1

    def test_tag(self):
        # LOGIN_ADD = self.params_j["LOGIN_ADD"]
        # LOGIN_PW = self.params_j["LOGIN_PW"]
        FILE_LIST_EML = self.params_j["FILE_LIST_EML"]
        DATA_FOLDER = self.params_j["DATA_FOLDER"]

        # LOGIN 
        # print("LOGIN")
        # self.login(id_v=LOGIN_ADD, pd_v=LOGIN_PW,capture=1)

        self.showSettingView(moveSetview=True, showType=9)

        self.edit_spam_open_eml()
        
        self.emlImport(emlPathList=FILE_LIST_EML, folderName=DATA_FOLDER)

        time.sleep(10)


 


if __name__ == '__main__':
    unittest.main()