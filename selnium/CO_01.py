import unittest
from models import test_class
import time
import inspect

file_name = __file__.split("\\")[-1].split(".")[0]

class Test_Case(test_class.Test_Class):
    file_name = __file__.split("\\")[-1].split(".")[0]
    not_login=1
    
    def test_theme(self):
        #表示設定
        selection_list = self.params_j["List"]

        #ログインID,PD
        # id_v = self.params_j["id_v"]
        # pd = self.params_j["PD"]
        id_v = self.id_CO_01
        pd = self.pd_CO_01

        #ログイン
        self.login(id_v, pd, assert_if=True)

        #初期化
        self.setting_page()
        self.change_theme("プレーン")
        self.save_change()

        for selection in selection_list:

            #設定変更
            self.setting_page()
            self.change_theme(selection)
            self.save_change()
            self.assert_message("詳細設定が保存されました")

            #色を確認
            self.setting_page()
            self.xpath = "//aside"
            self.assertTrue(self.params_j[selection][0] in self.get_css_property("background"))

            self.xpath = "//*[contains(@class,'headerUserOperationWrap')]"
            self.assertTrue(self.params_j[selection][1] in self.get_css_property("background"))

            #文字サイズ変更
            for size in ["1","3","2"]:
                self.display_size(select=size)
                self.save_change()
                self.assert_message("詳細設定が保存されました")
                time.sleep(6)

            #言語変更
            for language in ["英語","Japanese"]:
                self.change_language(selection=language)
                if language == "Japanese":
                    self.save_change(english=True)
                    self.assert_message("詳細設定が保存されました")
                else:
                    self.save_change()
                    self.assert_message("Advanced settings saved")
                time.sleep(6)
                    
            


                


if __name__ == '__main__':
    unittest.main()