import unittest
from models import test_class
import time
import inspect

class Test_Case(test_class.Test_Class):
    file_name = __file__.split("\\")[-1].split(".")[0]

    def test_initial(self):
        #同名のjsonファイルにtrue、falseを指定するとことで初期データインポートと事後削除を行う
        pass
    
if __name__ == '__main__':
    unittest.main()