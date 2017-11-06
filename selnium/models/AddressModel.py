import time
from models import BaseModel

class AddressModel(BaseModel.BaseModel):
    def __init__(self):
        pass

    def address_page(self):
        #アドレスページ
        self.xpath = "//a[contains(@href, '#/address')]"
        self.action()

    def open_address(self,address_book="連絡先", address="", capture=1):
        #アドレスをダブルクリックで開く
        self.xpath = "//*[contains(@class,'sidebar')]//*[contains(text(),'{}')]".format(address_book) 
        self.action(sleep=3)
            
        self.xpath = "//*[contains(text(),'{}')]".format(address)
        self.action(do="double_click", capture=capture)

    def select_address(self, address_book="連絡先", address=""):
        #アドレスのチェックボックスにチェックを入れる
        self.xpath = "//*[contains(@class,'sidebar')]//*[contains(text(),'{}')]".format(address_book) 
        self.action(sleep=3)

        self.xpath = "//*[contains(text(),'{}')]".format(address)
        self.xpath = self.xpath + "/parent::*/parent::*//input"
        self.action()


    def edit_address_button(self):
        #アドレス編集ボタンを押す
        self.xpath="//*[contains(text(),'編集')]/parent::*"
        self.action() 

    def upload_profile_img(self, path):
        self.xpath="//*[contains(text(),'変更') or contains(text(),'写真を追加')]"
        self.action() 

        time.sleep(1)
        self.xpath="//input[@class='input-image']"
        el = self.browser.find_element_by_xpath(self.xpath)
        time.sleep(1)
        el.send_keys(path)

        self.xpath="//address-image-select//*[contains(text(),'OK')]"
        self.action(do="", capture=1) 
        self.action() 
        

    def save_address_button(self):
        self.xpath = "//*[contains(text(),'保存')]/parent::*"
        self.action(do="", capture=1)
        self.action()

        self.xpath = "//*[contains(text(),'アドレスが保存されました')]"
        self.assertTrue(self.action(do="",capture=1, assert_if=1))

        

    def save_address(self, params={
                    "family_name":"testfamily", "last_name":"", 
                    "family_name_kana" : "", "last_name_kana" : "",
                    "company" : "", "company_kana" : "",
                    "mail_address" : "testaddress@chickenmail01.techfirm.co.jp"},
                    address_book = "連絡先"
                    ):
        #アドレス保存
        self.xpath = "//a[contains(@href, '#/address')]"
        self.action()

        self.xpath ="//*[contains(text(), '新規連絡先')]/parent::*"
        self.action()

        #アドレスブック選択
        self.xpath ="//form//*[contains(text(),'選択')]"
        self.action()

        self.xpath = "//address-book-select//a[contains(text(),'{}')]".format(address_book)
        self.action()

        self.xpath = "//address-book-select//*[contains(text(),'OK')]"
        self.action()

        #パラメータ入力
        self.xpath = "//*[contains(text(),'名前')]/parent::*/following-sibling::*//input[@type='text']"
        content = params["family_name"]
        self.action(do = "send_keys", content = content)

        self.xpath = "(//*[contains(text(),'名前')]/parent::*/following-sibling::*//input[@type='text'])[2]"
        content = params["last_name"]
        self.action(do = "send_keys", content = content)

        self.xpath = "//*[contains(text(),'フリガナ')]/parent::*/following-sibling::*//input[@type='text']"
        content = params["family_name_kana"]
        self.action(do = "send_keys", content = content)

        self.xpath = "(//*[contains(text(),'フリガナ')]/parent::*/following-sibling::*//input[@type='text'])[2]"
        content = params["last_name_kana"]
        self.action(do = "send_keys", content = content)
    
        self.xpath = "//*[contains(text(),'会社')]/parent::*/following-sibling::*//input[@type='text']"
        content = params["company"]
        self.action(do = "send_keys", content = content)

        self.xpath = "(//*[contains(text(),'フリガナ')]/parent::*/following-sibling::*//input[@type='text'])[3]"
        content = params["company_kana"]
        self.action(do = "send_keys", content = content)

        self.xpath = "//*[contains(text(),'メールアドレス')]/parent::*/following-sibling::*//input[@type='text']"
        content = params["mail_address"]
        self.action(do = "send_keys", content = content, capture=1)
        
        self.xpath = "//*[contains(text(),'保存')]/parent::*"
        self.action()

        self.xpath = "//*[contains(text(),'アドレスが保存されました')]"
        self.assertTrue(self.action(do="",capture=1, assert_if=1))

        time.sleep(3)


    def save_address_group(self,params={
        "group_name": "test_group", "group_member_name": "test_group_member_name",
        "group_member_address": "test_group_member_address@@chickenmail01.techfirm.co.jp",
        },
        address_book = "連絡先"):
        #アドレスグループ保存
        self.xpath = "//a[contains(@href, '#/address')]"
        self.action()

        self.xpath ="//*[contains(text(), '新規グループ')]/parent::*"
        self.action()

        #アドレスブック選択
        self.xpath ="//form//*[contains(text(),'選択')]"
        self.action()

        self.xpath = "//address-book-select//a[contains(text(),'{}')]".format(address_book)
        self.action()

        self.xpath = "//address-book-select//*[contains(text(),'OK')]"
        self.action()

        self.xpath = "//*[contains(text(),'連絡先グループ名')]/parent::*/following-sibling::*//input[@type='text']"
        content = params["group_name"]
        self.action(do = "send_keys", content = content)
        
        self.xpath = "//*[contains(text(),'表示名')]/parent::*/following-sibling::*//input[@type='text']"
        content = params["group_member_name"]
        self.action(do = "send_keys", content = content)
        
        self.xpath = "//*[contains(text(),'メールアドレス')]/parent::*/following-sibling::*//input[@type='text']"
        content = params["group_member_address"]
        self.action(do = "send_keys", content = content)

        self.xpath = "//*[contains(text(),'グループメンバーに追加')]"
        self.action(capture=1)

        self.xpath = "//*[contains(text(),'保存')]/parent::*"
        self.action()

        self.xpath = "//*[contains(text(),'アドレスグループが保存されました')]"
        self.assertTrue(self.action(do="",capture=1, assert_if=1))

        time.sleep(3)

    def save_address_book(self, address_book_name):
        #アドレスブック保存
        self.xpath = "//a[contains(@href, '#/address')]"
        self.action()

        self.xpath = "//*[contains(text(),'新しいアドレスブック')]" 
        self.action()

        self.xpath = "//*[contains(text(),'アドレスブック名')]/following-sibling::*//input" 
        content = address_book_name
        self.action(do = "send_keys", content = content)
        
        self.xpath = "//address-book-edit//color-selector//*[contains(@class,'colorSelectBtn')]"
        self.action()

        self.xpath = "(//address-book-edit//color-selector//label/span)[3]"
        self.action(capture=1)

        self.xpath = "//address-book-edit//*[contains(text(),'OK')]"
        self.action(capture=1)
        self.assert_message("した")
        
    def confirm_address(self, exist=1, keyword="test70", address_book="連絡先", delete=0):
        #アドレス、アドレスグループ確認
        self.xpath = "//a[contains(@href, '#/address')]" 
        self.action()

        self.xpath = "//*[contains(@class,'sidebar')]//*[contains(text(),'{}')]".format(address_book) 
        self.action(sleep=3)

        self.xpath = "//*[contains(text(),'{}')]".format(keyword)
        if exist == 1:
            self.assertTrue(self.action(do="", capture=1, assert_if=1))
        elif exist == 0:
            self.assertFalse(self.action(do="", capture=1, assert_if=1, false_is_error=0))

        if delete == 1:
            self.xpath = "//*[contains(text(),'{}')]".format(keyword)
            self.xpath = self.xpath + "/parent::*/parent::*//input"
            self.action()

            self.xpath="//*[contains(text(),'削除')]/parent::*"
            self.action() 

            self.xpath = "//modal-dialog//*[contains(text(),'OK')]" 
            self.action()
           

    def confirm_address_book(self, exist=1, keyword=""):
        #アドレスブック確認
        self.xpath = "//a[contains(@href, '#/address')]"
        self.action()

        self.xpath = "//*[@id='sidebarInner']//a[contains(text(),'{}')]".format(keyword)
        if exist == 1:
            self.assertTrue(self.action(do="", sleep=2, capture=1, assert_if=1))
        elif exist == 0:
            self.assertFalse(self.action(do="", sleep=2, capture=1, assert_if=1, false_is_error=0))



    def delete_address(self, keyword="test70", address_book="連絡先"):
        #アドレス、アドレスグループ削除
        self.xpath = "//a[contains(@href, '#/address')]" 
        self.action()

        self.xpath = "//*[contains(@class,'sidebar')]//*[contains(text(),'{}')]".format(address_book) 
        self.action(sleep=3)

        self.xpath = "//*[contains(text(),'{}')]".format(keyword)
        self.xpath = self.xpath + "/parent::*/parent::*//input[@type='checkbox']"
        self.action()

        self.xpath="//*[contains(text(),'削除')]/parent::*"
        self.action() 

        self.xpath = "//modal-dialog//*[contains(text(),'OK')]" 
        self.action()


    def delete_address_book(self, address_book_name=""):
        #アドレスブック削除
        self.xpath = "//a[contains(@href, '#/address')]"
        self.action()

        self.xpath = "//*[contains(@class,'sidebar')]//*[contains(text(),'{}')]".format(address_book_name) 
        self.action()

        self.xpath = self.xpath + "/parent::*/parent::*/following-sibling::*//*[contains(text(),'編集')]"
        self.action()

        self.xpath = "//*[contains(text(),'アドレスブックを削除')]" 
        self.action(capture=1)

        self.xpath = "//modal-dialog//*[contains(text(),'OK')]" 
        self.action()

        time.sleep(2)

