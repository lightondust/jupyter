import time
from models import BaseModel

class TagModel(BaseModel.BaseModel):
    
    COLOR_RED = "1"
    COLOR_PINK = "2"
    COLOR_PURPLE = "3"
    COLOR_BLUE = "4"


    def __init__(self):
        pass

    def save_tag(self, tag_name=""):
        """ save_tag 新規タブの作成
            tag_name : タグ名
        """
        self.xpath = "//a[contains(@href, '#/mail')]"
        self.action()

        self.xpath = "//aside//*[contains(text(),'新しいタグ')]" 
        self.action()

        self.xpath = "//*[contains(@aria-hidden,'false')]//*[contains(text(),'タグ名')]/following-sibling::*//input" 
        content = tag_name
        self.action(do = "send_keys", content = content)
        
        self.xpath = "//*[contains(@aria-hidden,'false')]//*[contains(@class,'colorSelectBtn')]"
        self.action()

        self.xpath = "//*[contains(@aria-hidden,'false')]//color-selector//*[contains(@class,'isOn')]//span[contains(@class,'C{}')]".format("4")
        self.action(capture=1)

        self.xpath = "//tag-edit//*[contains(@aria-hidden,'false')]//*[contains(text(),'OK')]"
        self.action()

    def set_tag(self, keyword="", tag_name="", address_book="連絡先"):
        """ set_tag タグの紐付け
            tag_name : タグ名
            address_book : 紐づけるアドレスブック
        """
        self.xpath = "//a[contains(@href, '#/mail')]"
        self.action()

        self.xpath = "//*[contains(@class,'sidebar')]//*[contains(text(),'{}')]".format(address_book) 
        self.action(sleep=3)

        self.xpath = "//*[contains(text(),'{}')]".format(keyword)
        self.xpath = self.xpath + "/parent::*/parent::*//input"
        self.action()

        self.xpath="//*[contains(text(),'タグ')]/parent::*"
        self.action() 

        self.xpath="//*[contains(text(),'{}')]/preceding-sibling::*//checkbox".format(tag_name) #/div
        self.action() 

        self.xpath="//*[contains(text(),'適用')]"
        self.action(capture=1, sleep=2) 

    def confirm_tag(self, exist=1, keyword="", delete=0):
        self.confirm_address_book(exist=exist, keyword=keyword)


    def delete_tag(self, tag_name=""):
        """ delete_tag タグの削除
            tag_name : タグ名
        """
        self.xpath = "//a[contains(@href, '#/mail')]" 
        self.action()

        self.xpath = "//*[contains(@class,'sidebar')]//*[contains(text(),'{}')]".format(tag_name) 
        self.action()

        self.xpath = self.xpath + "/parent::*/following-sibling::*//*[contains(text(),'編集')]"
        self.action()

        self.xpath = "//*[contains(text(),'タグを削除')]" 
        self.action(capture=1)

        self.xpath = "//modal-dialog//*[contains(text(),'OK')]" 
        self.action()

        time.sleep(2)

    def delete_address_tag(self, tag_name="", show_capture=False):
        """ delete_tag タグの削除
        tag_name : タグ名
        """
        self.tagMove(1)

        self.xpath = "//*[contains(@class,'sidebar')]//*[contains(text(),'{}')]".format(tag_name) 
        self.action()

        self.xpath = self.xpath + "/parent::*/following-sibling::*//*[contains(text(),'編集')]"
        self.action()

        self.xpath = "//*[contains(text(),'タグを削除')]" 
        if show_capture:
            self.action(capture=1)
        else:
            self.action(capture=0)

        self.xpath = "//modal-dialog//*[contains(text(),'OK')]" 
        self.action()

        time.sleep(2)

    def change_tag_color(self, tag_name="", color_num="1"):
        """ change_tag_color タグのカラーを変更
            tag_name : タグ名
            color_num : カラー番号：1-8で設定すること
        """
        self.xpath = "//a[contains(@href, '#/mail')]" 
        self.action()

        self.xpath = "//*[contains(@class,'sidebar')]//*[contains(text(),'{}')]".format(tag_name) 
        self.action()

        self.xpath = self.xpath + "/parent::*/following-sibling::*//*[contains(text(),'編集')]"
        self.action()

        self.xpath = "//li[contains(text(),'タグを編集')]"
        self.action()

        self.xpath = "//*[contains(@aria-hidden,'false')]//*[contains(@class,'colorSelectBtn')]"
        self.action()

        self.xpath = "//*[contains(@aria-hidden,'false')]//color-selector//*[contains(@class,'isOn')]//span[contains(@class,'C{}')]".format(color_num)
        self.action(capture=1)

        self.xpath = "//tag-edit//*[contains(@aria-hidden,'false')]//*[contains(text(),'OK')]"
        self.action()

    def tag_setinng_for_mail(self, mail_box="受信箱",mail_subject="test", tag_name=""):
        """ tag_setinng_for_mail メールにタグを紐づける
        mail_box : メールボックスの設定
        mail_subject : メールの件名
        tag_name : 設定するタグ名
        """
        self.xpath = "//a[contains(@href, '#/mail')]" 
        self.action(sleep=2)

        self.xpath = "//*[contains(@class,'sidebar')]//a[contains(text(),'{}')]".format(mail_box) 
        self.action(sleep=2)

        self.xpath = "//*[contains(text(),'{}')]/parent::*/parent::*/preceding-sibling::*//input".format(mail_subject)
        self.action(sleep=2)

        self.xpath="//*[contains(text(),'タグ')]/parent::*"
        self.action() 

        self.xpath="//*[contains(text(),'{}')]/preceding-sibling::*//checkbox".format(tag_name) #/div
        self.action(sleep=2, capture=1) 

        self.xpath="//*[contains(text(),'適用')]"
        self.action() 


    def tag_setinng_for_address(self, select_add_book="", address_name="", tag_name=""):
        """ tag_setinng_for_address アドレスにタグを紐づける
        address_name : 紐づけるアドレス・アドレスグループ名
        tag_name : 設定するタグ名
        """
        # アドレスページに遷移
        self.tagMove(1)
        self.action(sleep=2)

        # 連絡先の表示
        print("連絡先の表示[" + select_add_book + "]")
        self.selectAddressGroup(select_add_book)
        self.capture()

        # 検索
        print("検索[" + address_name + "]")
        self.searchAddress(searchKey=address_name)

        self.xpath = "//*[contains(text(),'{}')]/parent::*/parent::*//input".format(address_name)
        self.action(sleep=1)

        self.xpath="//*[contains(text(),'タグ')]/parent::*"
        self.action() 

        self.xpath="//*[contains(text(),'{}')]/preceding-sibling::*//checkbox".format(tag_name) #/div
        self.action(sleep=1, capture=1) 

        self.xpath="//*[contains(text(),'適用')]"
        self.action()
        self.assert_message("した")

    def showTagMail(self, target="", exist=True):
        """ showTagMail 特定のタグ一覧を表示
        target : 確認するタグ名
        """
        self.xpath = "//a[contains(@href, '#/mail')]" 
        self.action(sleep=2)
        self.xpath = "//*[contains(@class,'sidebar')]//*[contains(text(),'{}')]".format(target) 
        self.action(sleep=2)

        self.xpath = "//*[contains(text(),'{}')]".format(target)
        if exist:
            self.assertTrue(self.action(do="",capture=1, assert_if=1))
        else:
            self.assertFalse(self.action(do="",capture=1, assert_if=1, false_is_error=0))

    def showTagAddress(self, target="", exist=True):
        """ showTagMail 特定のタグ一覧を表示
        target : 確認するタグ名
        """
        self.tagMove(1)
        self.action(sleep=2)

        self.xpath = "//*[contains(@class,'sidebar')]//*[contains(text(),'{}')]".format(target) 
        self.action(sleep=2)

        self.xpath = "//*[contains(text(),'{}')]".format(target)
        if exist:
            self.assertTrue(self.action(do="",capture=1, assert_if=1))
        else:
            self.assertFalse(self.action(do="",capture=1, assert_if=1, false_is_error=0))
