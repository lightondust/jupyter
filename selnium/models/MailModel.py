import time
import os
from models import BaseModel
from selenium import webdriver

class MailModel(BaseModel.BaseModel):
#class MailModel():
    def __init__(self):
        pass
    
    def mail_page(self):
        #メールページへ遷移
        self.xpath = "(//a[contains(@href, '#/mail')])[2]" 
        self.action(sleep=2)

    def mail_open(self, mail_box="受信箱", keyword="", capture=0):
        #指定したメールを開く
        self.xpath = "//*[contains(@class,'sidebar')]//a[contains(text(),'{}')]".format(mail_box) 
        self.action(sleep=2)
        
        self.xpath = "//*[contains(text(),'{}')]".format(keyword)
        self.action(sleep=2, do="", capture=capture)        
        self.action(do="double_click")        

    def select_mail(self, mail_box="受信箱", keyword=""):
        self.xpath = "//*[contains(@class,'sidebar')]//a[contains(text(),'{}')]".format(mail_box) 
        self.action(sleep=2)
        
        self.xpath = "//*[contains(text(),'{}')]/parent::*/parent::*/preceding-sibling::*//input".format(keyword)
        self.action(sleep=2, capture=1)

    def move_mail(self, mail_box="受信箱"):
        #select_mailで選んだメールをmail_boxに移動させる 「1件のメッセージを「BBQ」に移動しました」

        self.xpath = "//navi-item//*[contains(text(),'移動')]/parent::*"    
        self.action()

        self.xpath = "//dialog-holder//a[contains(text(),'{}')]".format(mail_box)    
        self.action()

        self.xpath = "//dialog-holder//*[contains(text(),'OK')]"
        self.action(do="", capture=1)
        self.action()

    def set_flag_to_mail(self, set=True):
        #フラグを付ける　1件のメッセージにフラグが付けられました・外されました。

        self.xpath = "//navi-item//*[contains(text(),'その他')]/parent::*"    
        self.action()

        if set:
            self.xpath = "//*[contains(text(),'フラグをつける')]"    
            self.action()
        else:
            self.xpath = "//*[contains(text(),'フラグをはずす')]"    
            self.action()

    def original_mail(self, capture=1):
        #フラグを付ける　1件のメッセージにフラグが付けられました・外されました。

        self.xpath = "//navi-item//*[contains(text(),'その他')]/parent::*"    
        self.action()

        self.xpath = "//*[contains(text(),'ヘッダと本文を表示')]"    
        self.action(do="", capture=capture)
        self.action()


    def set_spam(self):
        #迷惑メール通報ボタン　どちらも　"通報を受け付けました"

        self.xpath = "//navi-item//*[contains(text(),'迷惑')]/parent::*"    
        self.action()
        
    def delete_mail(self):
        #メール削除　
        # フォルダから：1件のメッセージをゴミ箱に移動しました
        # ゴミ箱の中（物理削除）：1件のメッセージを削除しました。
        self.xpath = "//navi-item//*[contains(text(),'削除')]/parent::*"    
        self.action()
        
        
    def download_attachment(self, file_name="", capture=0):
        self.xpath = "//*[contains(text(),'{}')]".format(file_name) 
        self.action(sleep=2, capture=capture)

    def create_mail(self):
        #メール作成ボタン
        self.xpath = "//*[contains(text(),'メール作成')]/parent::*" 
        self.action()

    def reply_mail(self, mail_box="受信箱", keyword=""):
        #メールに返信

        self.select_mail(mail_box=mail_box, keyword=keyword)
        # self.xpath = "//*[contains(@class,'sidebar')]//a[contains(text(),'{}')]".format(mail_box) 
        # self.action(sleep=2)
        
        # self.xpath = "//*[contains(text(),'{}')]/parent::*/parent::*/preceding-sibling::*//input".format(keyword)
        # self.action(sleep=2)

        self.xpath = "//navi-item//*[contains(text(),'返信')]/parent::*"    
        self.action()

        self.xpath = "//li[contains(text(),'返信')]"    
        self.action()

    def draft_open(self, keyword):
        #下書きメールを開く
        self.xpath = "//*[contains(@class,'sidebar')]//a[contains(text(),'{}')]".format("下書き") 
        self.action(sleep=2)
        
        self.xpath = "//*[contains(text(),'{}')]/parent::*/parent::*/preceding-sibling::*//input".format(keyword)
        self.action(do="double_click", sleep=2)


    def set_address(self, auto_complete=False,
                    mail_address="", to="To", deal_auto_complete=True):
        #アドレス入力 auto_complete=trueでオートコンプリートのキャッチ

        self.xpath = "//*[contains(@class,'mailEdit')]//*[contains(text(),'表示')]/parent::*"
        self.action()

        text = {"To":"宛先", "CC": "CC"}
        self.xpath = "//*[contains(text(),'{}')]/following-sibling::*//input".format(text[to]) 
        content = mail_address
        self.action(do = "send_keys", content = content)

        #オートコンプリート処理
        if deal_auto_complete:
            try:
                self.xpath = "//li/span"
                if auto_complete:
                    self.action(sleep=2, capture=1, false_is_error=0)
                    auto_complete_on = True
                    return auto_complete_on
                else:
                    self.action(sleep=2, false_is_error=0)
            except:
                if auto_complete:
                    auto_complete_on = False
                    return auto_complete_on

    def select_address(self, keyword = [], to_list =[], address_book="連絡先"):
        #アドレス選択、メールアドレスをアドレスブックから選択、
        #keyword=[選ぶアドレスのリスト]、to_list=["宛先","CC","BCC"]
        
        self.xpath = "//*[contains(text(),'宛先')]"
        self.action()

        if address_book:
            self.xpath = "//*[contains(text(),'送信先の選択')]/following-sibling::*//select"
            content = address_book
            self.action(do="select", content=content)

        for roll in to_list:
            for key in keyword:
                self.xpath = "//*[contains(text(),'{}')]/parent::*/following-sibling::*//input".format(key)
                self.action()

                self.xpath = "//mail-edit-address-select//*[contains(text(),'{}')]".format(roll)
                self.action()

        self.xpath = "//mail-edit-address-select//*[contains(text(),'OK')]"
        self.action(do="", capture=1)
        self.action()

    def set_mail_subject(self, mail_subject=""):
        #件名入力
        self.xpath = "//*[contains(text(),'件名')]/parent::*/following-sibling::*//input" 
        content = mail_subject
        self.action(do = "send_keys", content = content)
    
    def set_mail_content(self, mail_content=""):
        #本文入力
        self.xpath = "//textarea[@id='mailbody-textarea']" 
        content = mail_content
        self.action(do = "send_keys", content = content)

    def attach_mail(self, mail_box="", mail_keyword=""):
        #メール添付

        self.xpath = "//mail-edit//*[contains(text(),'添付') and contains(@class,'mailEdit')]"
        self.action()

        self.xpath = "//mail-edit//*[contains(text(),'メールを添付')]"
        self.action()

        self.xpath = "//attach-mail-select//select"
        self.action(do="select", content=mail_box)

        self.xpath = "//*[contains(text(),'{}')]/parent::*/parent::*/preceding-sibling::*//input".format(mail_keyword)
        self.action()

        self.xpath = "//attach-select//*[contains(text(),'OK')]"
        self.action(do="", capture=1)
        self.action()

    def attach_file(self, path=""):
        #ファイル添付

        self.xpath = "//mail-edit//*[contains(text(),'添付') and contains(@class,'mailEdit')]"
        self.action()

        self.xpath = "//input[contains(@type,'file')]"
        time.sleep(1)
        element = self.browser.find_element_by_xpath(self.xpath)
        element.send_keys(path)

        self.xpath = "//attach-select//*[contains(text(),'OK')]"
        self.action(do="", capture=1)
        self.action()


    def save_draft(self):
        #下書き保存
        self.xpath = "//div[@id='contentsHeader']//nav//*[contains(text(),'下書き保存')]/parent::*"
        self.action(do="", capture=1)
        self.action()
    
        self.xpath = "//*[contains(text(),'{}')]".format("下書きが保存されました")
        self.assertTrue(self.action(do="", capture=1, assert_if=1))

        time.sleep(3)
        
    def send_mail_button(self):
        #メール送信ボタン
        self.xpath = "//div[@id='contentsHeader']//nav//*[contains(text(),'送信')]/parent::*"
        self.action(do="", capture=1)
        self.action()

        self.xpath = "//*[contains(text(),'メッセージが送信されました')]"
        self.assertTrue(self.action(do="", capture=1, assert_if=1))   

        time.sleep(3)     


    def search_condition_button(self):
        #検索条件ボタン
        self.xpath = "//*[contains(@title,'検索条件')]" 
        self.action()

    def set_search_condition(self,mail_box="",
                            from_v="", to="", subject="", content=""):
        #検索条件設定 
        # from_v:差出人 
        # to:宛先またはCC 
        # subject:件名 
        # content:本文

        if mail_box:
            self.xpath = "//search-detail//input[contains(@*,'folderPath')]/parent::*"
            self.action()

            self.xpath = "//search-detail//a[contains(text(),'{}')]".format(mail_box)
            self.action()
        
        if from_v:
            self.xpath = "//search-detail//*[contains(text(),'{}')]/following-sibling::*//input".format("差出人")
            self.action(do="send_keys", content = from_v)

        if to:
            self.xpath = "//search-detail//*[contains(text(),'{}')]/following-sibling::*//input".format("宛先または")
            self.action(do="send_keys", content = to)
            
        if subject:
            self.xpath = "//search-detail//*[contains(text(),'{}')]/following-sibling::*//input".format("件名")
            self.action(do="send_keys", content = subject)

        if content:
            self.xpath = "//search-detail//*[contains(text(),'{}')]/following-sibling::*//input".format("本文")
            self.action(do="send_keys", content = content)

    def save_search_condition(self):
        self.xpath = "//search-detail//*[contains(text(),'検索条件を保存')]"
        self.action(do="",capture=1)
        self.action()

    def edit_search_condition_button(self, name="", delete=False):
        self.xpath = "//section//*[contains(text(),'{}')]".format(name)
        self.action()

        self.xpath = "//section//*[contains(text(),'{}')]/parent::*/parent::*/following-sibling::*//*[contains(text(),'編集')]".format(name)
        self.action()

        if delete:
            self.xpath = "//li[contains(text(),'削除')]"
            self.action()

            self.xpath = "//modal-dialog//*[contains(text(),'OK')]"
            self.action(do="", capture=1)
            self.action()

        else:
            self.xpath = "//*[contains(text(),'検索条件を編集')]"
            self.action()


    def edit_search_condition(self, name=""):
        if name:
            self.xpath = "//input[@name='name']"
            self.action(do="send_keys", content = name)

        self.xpath = "//dialog-holder//*[contains(text(),'OK')]"
        self.action(do="",capture=1)
        self.action()


        



    def send_mail(self, draft=0, reply=0, send_draft=0, auto_complete=0, 
        to="To",
        keyword = [], to_list =[], address_book="",
        mail_address="",
        mail_subject="",
        mail_contents="",
        reply_keyword="",
        reply_mailbox="受信箱",
        draft_keyword="",
        attatch_mail=False,
        attatch_mail_box="",
        attatch_mail_keyword=""
        ):
        #メール送信
        #to="To""CC"でmail_address、mail_subject、mail_contents指定で、メール送信
        #to="addressbook"、keyword、to_list、address_book、mail_subectとmail_content指定で、アドレス帳から選択して送信
        #auto_complete=1でオートコンプリートを確認する
        #draft=1で送信せず下書き保存
        #reply=1 reply_keyword、reply_mailbox指定で指定したメールに返信する

        self.xpath = "(//a[contains(@href, '#/mail')])[2]" 
        self.action(sleep=2)

        #メールに返信する場合
        if reply:
            #メールボックス選択
            self.xpath = "//*[contains(@class,'sidebar')]//a[contains(text(),'{}')]".format(reply_mailbox) 
            self.action(sleep=2)
            
            self.xpath = "//*[contains(text(),'{}')]/parent::*/parent::*/preceding-sibling::*//input".format(reply_keyword)
            self.action(sleep=2)

            self.xpath = "//navi-item//*[contains(text(),'返信')]/parent::*"    
            self.action()

            self.xpath = "//li[contains(text(),'返信')]"    
            self.action()

        #下書きから送信の場合
        elif send_draft:
            self.xpath = "//*[contains(@class,'sidebar')]//a[contains(text(),'{}')]".format("下書き") 
            self.action(sleep=2)
            
            self.xpath = "//*[contains(text(),'{}')]/parent::*/parent::*/preceding-sibling::*//input".format(draft_keyword)
            self.action(do="double_click", sleep=2)

        #新規作成の場合        
        else:
            self.xpath = "//*[contains(text(),'メール作成')]/parent::*" 
            self.action()

        self.xpath = "//*[@id='cc_bcc_toggle_block']//*[contains(text(),'表示')]/parent::*"
        self.action()

        if to in ["To", "CC"]:
            text = {"To":"宛先", "CC": "CC"}
            self.xpath = "//*[contains(text(),'{}')]/following-sibling::*//input".format(text[to]) 
            content = mail_address
            self.action(do = "send_keys", content = content)

            #オートコンプリート対策、対応
            try:
                self.xpath = "//li/span[2]"
                if auto_complete:
                    self.action(sleep=2, capture=1, false_is_error=0)
                    auto_complete_on = True
                else:
                    self.action(sleep=2, false_is_error=0)
            except:
                if auto_complete:
                    auto_complete_on = False

        elif to == "address_book": #登録済みアドレスから選択する
            self.xpath = "//*[contains(text(),'宛先')]"
            self.action()

            if address_book:
                self.xpath = "//*[contains(text(),'送信先の選択')]/following-sibling::*//select"
                content = address_book
                self.action(do="select", content=content)
           

            for roll in to_list:
                for key in keyword:
                    self.xpath = "//*[contains(text(),'{}')]/parent::*/following-sibling::*//input".format(key)
                    self.action()

                    self.xpath = "//mail-edit-address-select//*[contains(text(),'{}')]".format(roll)
                    self.action()

            self.xpath = "//mail-edit-address-select//*[contains(text(),'OK')]"
            self.action()

        if mail_subject:
            self.xpath = "//*[contains(text(),'件名')]/parent::*/following-sibling::*//input" 
            content = mail_subject
            self.action(do = "send_keys", content = content)

        if mail_contents:
            self.xpath = "//textarea[@id='mailbody-textarea']" 
            content = mail_contents
            self.action(do = "send_keys", content = content)

        if attach_mail():
            self.xpath = "//mail-edit//*[contains(text(),'添付') and contains(@class,'mailEdit')]"
            self.action()

            self.xpath = "//mail-edit//*[contains(text(),'メールを添付')]"
            self.action()

            self.xpath = "//attach-mail-select//select"
            self.action(do="select", content=attatch_mail_box)

            self.xpath = "//*[contains(text(),'{}')]/parent::*/parent::*/preceding-sibling::*//input".format(attatch_mail_keyword)
            self.action()

            self.xpath = "//attach-select//*[contains(text(),'OK')]"
            self.action(do="", capture=1)
            self.action()



        if draft:
            self.xpath = "//div[@id='contentsHeader']//nav//*[contains(text(),'下書き保存')]/parent::*"
            self.action(do="", capture=1)
            self.action()
        
            self.xpath = "//*[contains(text(),'{}')]".format("下書きが保存されました")
            self.assertTrue(self.action(do="", capture=1, assert_if=1))

            time.sleep(3)

        else:
            self.xpath = "//div[@id='contentsHeader']//nav//*[contains(text(),'送信')]/parent::*"
            self.action(do="", capture=1)
            self.action()

            self.xpath = "//*[contains(text(),'メッセージが送信されました')]"
            self.assertTrue(self.action(do="", capture=1, assert_if=1))   

            time.sleep(3)     

        if auto_complete:
            return auto_complete_on

    def confirm_mail_box(self, keyword="受信箱", exist=True, parent_box=[]):
        #メールフォルダ確認
        self.xpath = "(//a[contains(@href, '#/mail')])[2]" 
        self.action(sleep=2)

        # フォルダ階層を開く場合：
        if parent_box:
            for box in parent_box:
                try:
                    self.xpath = "//a[contains(text(),'{}')]/parent::*/preceding-sibling::*//*[@class='btn btnNest']".format(box)
                    self.action(capture_false=0)
                except:
                    pass

        self.xpath = "//*[contains(text(),'{}')]".format(keyword)
        if exist:
            self.assertTrue(self.action(do="", capture=1, assert_if=1))
        else:
            self.assertFalse(self.action(do="", capture=1, assert_if=1, false_is_error=0))


    def confirm_mail_box_for_outmail(self, user_name="", folder_name=""):
        ''' confirm_mail_box_for_outmail ：外部アカウントのメールボックスの確認
        user_name : 外部アカウントのユーザ名
        folder_name : 表示フォルダ名
        '''

        self.xpath = "//*[contains(text(),'{0}')]/parent::*/parent::*/parent::*/parent::*//*[contains(text(),'{1}')]".format(user_name, folder_name)
        self.action(capture=1)

        pass

    def create_mail_box(self):
        #メールフォルダ作成ボタン
        self.xpath = "(//a[contains(@href, '#/mail')])[2]" 
        self.action()

        self.xpath = "//*[contains(text(),'新しいフォルダ')]" 
        self.action()

    def change_mail_box(self, mail_box=""):
        #メールフォルダ編集ボタン
        self.xpath = "(//a[contains(@href, '#/mail')])[2]" 
        self.action(sleep=2)

        self.xpath = "//folder-item//*[contains(text(),'{}')]".format(mail_box)
        self.action()

        self.xpath = "//*[contains(text(),'{}')]/parent::*/parent::*/parent::*//*[contains(text(),'編集')]".format(mail_box)
        self.action()

        self.xpath = "//li[contains(text(),'フォルダを編集')]" 
        self.action(do="", capture=1) #キャプチャ
        self.action()


    def edit_mail_box(self, mail_box="", 
                        move_to="", color=0):
        #メールフォルダ項目編集、保存
        if mail_box:
            self.xpath = "//*[contains(text(),'フォルダ名')]/parent::*//input" 
            self.action(do = "send_keys", content = mail_box)
        
        if color:
            self.xpath = "//*[contains(@class,'isOn')]//color-selector//div[contains(@class,'Btn')]" 
            self.action()

            self.xpath = "//color-selector//*[contains(@class,'isOn')]//*[contains(@class,'chipC{}')]".format(color)
            self.action()
            
        if move_to:
            self.xpath = "//folder-edit//a[contains(text(),'{}')]".format(move_to) 
            self.action()

        self.xpath = "//dialog-holder//*[contains(text(),'OK')]" 

        self.action(do="", capture=1)
        self.action()
            

    def delete_mail_box(self, keyword, capture=1):
        #メールフォルダ削除　keywordはフォルダ名
        self.xpath = "(//a[contains(@href, '#/mail')])[2]" 
        self.action(sleep=2)

        self.xpath = "//folder-item//*[contains(text(),'{}')]".format(keyword)
        self.action()

        self.xpath = "//*[contains(text(),'{}')]/parent::*/parent::*/parent::*//*[contains(text(),'編集')]".format(keyword)
        self.action()

        time.sleep(1)

        self.xpath = "//li[contains(text(),'フォルダを削除')]" 
        self.capture()
        self.action()
        self.assert_message("した")

        #エラーメッセージ対応
        try:
            self.xpath = "//modal-dialog//*[contains(text(),'OK')]" 
            self.action(capture=1, capture_false=0)
            print(keyword,"関連のフォルダ削除の時にエラーメッセージが表示されました")
        except:
            pass
        
        time.sleep(1)
        

    def confirm_mail(self, delete=0, exist=1,
         confirm_to=[], 
         confirm_content=[], 
         mail_box="受信箱", mail_subject=""):
        #メールを確認
        # delete=1の場合は削除する
        # confirm_to=[keyword,...]でメールの宛先を確認
        # confirm_content=[keyword,...]でcontains(text(),'keyword')式で確認できる項目を確認

        self.xpath = "(//a[contains(@href, '#/mail')])[2]" 
        self.action(sleep=2)

        self.xpath = "//*[contains(@class,'sidebar')]//a[contains(text(),'{}')]".format(mail_box) 
        self.action(sleep=2)
        
        self.xpath = "//*[contains(text(),'{}')]".format(mail_subject)
        self.assertTrue(self.action(do="", capture=1, assert_if=1, sleep=2))

        #宛先を確認する場合
        if confirm_to:
            self.action(do="double_click")

            for content in confirm_to:
                self.xpath = "//*[contains(text(),'宛先')]/following-sibling::*//span"
                el = WebDriverWait(self.browser, 10).until(
                    EC.presence_of_element_located((By.XPATH, self.xpath))
                    )
                self.assertTrue(content in el.text)

        #普通の確認（contains(text(),''))形式でとれるもの
        elif confirm_content:
            self.action(do="double_click")
            for content in confirm_content:
                self.xpath = "//*[contains(text(),'{}')]".format(content)
                self.assertTrue(self.action(do="", capture=1, assert_if=1))

        #確認のち削除する場合
        if delete==1:
            self.xpath = "//*[contains(@class,'sidebar')]//a[contains(text(),'{}')]".format(mail_box) 
            self.action(sleep=2)
            
            self.xpath = "//*[contains(text(),'{}')]/parent::*/parent::*/preceding-sibling::*//input".format(mail_subject)
            self.action(sleep=2)

            self.xpath = "//navi-item//*[contains(text(),'削除')]/parent::*"    
            self.action(sleep=2)

            self.xpath = "//*[contains(text(),'ゴミ箱に移動しました')]"
            self.assertTrue(self.action(do="", capture=1, assert_if=1))

            time.sleep(3)

    def showMail(self, target="受信箱"):
        self.xpath = "//a[contains(@href, '#/mail')]" 
        self.action(sleep=2)
        self.xpath = "//*[contains(@class,'sidebar')]//*[contains(text(),'{}')]".format(target) 
        self.action(sleep=2)


    def tag_setinng_for_mail(self, mail_box="受信箱",mail_subject="test", tag_name=""):
        self.xpath = "(//a[contains(@href, '#/mail')])[2]" 
        self.action(sleep=2)

        self.xpath = "//*[contains(@class,'sidebar')]//a[contains(text(),'{}')]".format(mail_box) 
        self.action(sleep=2)

        self.xpath = "//*[contains(text(),'{}')]/parent::*/parent::*/preceding-sibling::*//input".format(mail_subject)
        self.action(sleep=2)

        self.xpath="//*[contains(text(),'タグ')]/parent::*"
        self.action() 

        self.xpath="//*[contains(text(),'{}')]/preceding-sibling::*//checkbox".format(tag_name) #/div
        self.action() 

        self.xpath="//*[contains(text(),'適用')]"
        self.action() 



    def mailImport(self, mailPathList={}, folderName=""):
        
        file_list = mailPathList
        data_folder = folderName
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

        pass
 
    def emlImport(self, emlPathList={}, folderName=""):
            
        file_list = emlPathList
        data_folder = folderName
        mail_folder_list = [name.split("_")[-1] for name in file_list]

        base_path=os.getcwd()

        #インポート
        for file_n in file_list:
            path = os.path.join(base_path, data_folder, file_n) + ".eml"

            self.xpath = "//*[contains(@class,'isOn')]//*//input[@type='file']"
            time.sleep(1)
            el = self.browser.find_element_by_xpath(self.xpath)
            time.sleep(1)
            el.send_keys(path)
            self.capture()
            
            self.xpath = "//*[contains(@class,'isOn')]//*[contains(text(),'通報する')]"
            self.action()
            self.assert_message("通報しますか？")


            self.xpath = "//*[contains(@class,'isOn')]//*[contains(text(),'OK')]"
            self.action()
            self.assert_message("通報されました")




        pass

    def searchMail(self, searchKey=""):
        # 検索
        # 一覧表示画面から特定メールを検索する
        self.xpath = "//*[@id='contentsHeader']//*[@type='search']" 
        content = searchKey  
        self.action(do = "send_keys", content = content)

        self.xpath = "//*[@id='contentsHeader']//*[@class='searchBtn']"
        self.action(do = "click", capture=1)

    def mailListOnClick(self, searchKey=""):
        # アドレス選択
        # アドレス一覧表示画面から特定のアドレスを選択して詳細を表示する

        self.xpath = "//*[@id='mainContents']//div[@class='listItem']//*[contains(text(),'{}')]".format(searchKey)
        self.action(do = "double_click", capture=1)

    def confirm_outside_box(self, account_name=""):
        '''
        confirm_outside_box ：外部アカウントのメールボックスを確認する
        account_name : 外部アカウント名
        '''
        self.tagMove(0)
        # フォルダが出てくるまでループ
        while not self.element_find_xpath(find_xpath="//*[contains(text(),'" + str(account_name)+ "')]"):
            print("メールフォルダで [ " + account_name + "]を確認できませんでした 10秒待機します")
            time.sleep(10)
            self.tagMove(0)
            pass

    def confirm_open_outside_box(self, account_name="", isOpen=True):
        '''
        confirm_open_outside_box:
            外部アカウントのメールボックスを開く。
            開く階層は一つだけである。

        account_name : 外部アカウント名
        '''

        self.tagMove(0)
        

        if isOpen:
            
            if not self.element_find_xpath(find_xpath="//*[contains(text(),'{}')]/parent::*/parent::*//span[contains(@class,'isOpen')]".format(account_name)):
                # 開いていなければ開く
                self.xpath = "//*[contains(text(),'{}')]/parent::*/parent::*//div[@class='menuNest']".format(account_name)
                self.action()
        else:
            self.xpath = "//*[contains(text(),'{}')]/parent::*/parent::*//div[@class='menuNest']".format(account_name)
            self.action()