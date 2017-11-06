import unittest
from models import test_class
import time
import inspect
import os

file_name = __file__.split("\\")[-1].split(".")[0]

class Test_Case(test_class.Test_Class):
    file_name = __file__.split("\\")[-1].split(".")[0]
    
    def test_send_mail(self):
        #メール添付、ファイル添付、メール下書き保存、送信

        mail_subject = self.params_j["mail_subject"]
        mail_content = self.params_j["mail_content"]
        mail_box_attach = self.params_j["mail_box_attach"]
        mail_keyword_attach = self.params_j["mail_keyword_attach"]

        data_folder = self.params_j["data_folder"]
        file_name = self.params_j["file_name"]

        base_path=os.getcwd()
        path = os.path.join(base_path, data_folder)
        path = os.path.join(path, file_name)

        #メール添付下書き保存
        self.mail_page()
        self.create_mail()
        self.set_address(mail_address=self.id_v)
        self.set_mail_content(mail_content=mail_content)
        self.set_mail_subject(mail_subject=mail_subject)

        #メール添付
        self.attach_mail(mail_box=mail_box_attach, mail_keyword=mail_keyword_attach)
        time.sleep(5)

        #ファイル添付
        self.attach_file(path)

        #下書き保存
        self.save_draft()

        #下書き保存したメールを開いて送信
        self.mail_page()
        self.draft_open(mail_subject)
        self.send_mail_button()

        #メール確認
        self.confirm_mail(mail_subject=mail_subject)


if __name__ == '__main__':
    unittest.main()