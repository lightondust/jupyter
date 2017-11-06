import unittest
from models import test_class
import time
import inspect

class Test_Case(test_class.Test_Class):
    file_name = __file__.split("\\")[-1].split(".")[0]
    
    def test_MV_05(self):
        #検索条件作成編集削除

        mail_box = self.params_j["mail_box"]
        from_v = self.params_j["from_v"]
        to = self.params_j["to"]
        subject = self.params_j["subject"]
        content = self.params_j["content"]
        search_name = self.params_j["search_name"]
        search_name_new = self.params_j["search_name_new"]

        #検索条件作成
        self.mail_page()
        self.search_condition_button()
        self.set_search_condition(mail_box=mail_box, from_v=from_v,
                to=to, subject=subject, content=content)
        self.save_search_condition()
        self.edit_search_condition(name=search_name)
        self.confirm_mail(mail_box=search_name, mail_subject=subject)

        #検索条件編集
        self.edit_search_condition_button(name=search_name)
        self.edit_search_condition(name=search_name_new)
        self.confirm_mail_box(search_name_new)
        self.confirm_mail(mail_box=search_name_new, mail_subject=subject)

        self.edit_search_condition_button(name=search_name_new, delete=True)
        self.confirm_mail_box(search_name_new, exist=False)

if __name__ == '__main__':
    unittest.main()