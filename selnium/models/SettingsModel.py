import time
from models import BaseModel
import os

class SettingsModel(BaseModel.BaseModel):
    def __init__(self):
        pass

    def setting_page(self):
        #設定画面に遷移
        self.xpath = "//a[contains(@href, '#/settings')]" 
        self.action()

    def change_password(self, password, password_new):
        #パスワード変更、メッセージassert付き、変更を保存するは不要

        self.xpath = "//button[contains(text(),'パスワードを変更')]"
        self.action()

        self.xpath = "//input[@ng-reflect-name='oldPassword']"
        content = password
        self.action(do="send_keys", content=content)

        self.xpath = "//input[@ng-reflect-name='newPassword']"
        content = password_new
        self.action(do="send_keys", content=content)
        
        self.xpath = "//input[@ng-reflect-name='confirmNewPassword']"
        content = password_new
        self.action(do="send_keys", content=content)

        self.xpath = "//*[contains(@class,'modalWindowBtn')]//*[contains(text(),'変更')]"
        self.action(capture=1)

        self.xpath = "//*[contains(@class,'isOn')]//*[contains(text(),'OK')]"
        self.action()

        self.assert_message("変更が保存されました")

    def display_mode(self, select):
        #メール表示形式　１HTML、２テキスト
        self.xpath = "(//input[@name='{}'])[{}]".format("displayMode",select) 
        self.action(capture=1)

    def display_format(self, select):
        #メールスレッド表示　１メッセージ、２スレッド
        self.xpath = "(//input[@name='{}'])[{}]".format("displayFormat",select) 
        self.action(capture=1)

    def display_name_mode(self, select):
        #ディスプレイネーム　１表示名、２メールアドレス
        self.xpath = "(//input[@name='{}'])[{}]".format("displayNameMode",select) 
        self.action(capture=1)

    def display_list_style(self, select):
        #一覧の分割表示　１上下に分割、２左右に分割、３分割しない
        self.xpath = "(//input[@name='{}'])[{}]".format("displayListStyle",select) 
        self.action(capture=1)

    def use_snippet(self, select):
        #ス二ぺット表示　１する、２しない
        self.xpath = "(//input[@name='{}'])[{}]".format("useSnippet",select) 
        self.action(capture=1)
        
    def read_soon(self, select):
        #一覧でのメッセージ操作　１すぐに既読にする、２既読にしない
        self.xpath = "(//input[@name='{}'])[{}]".format("readSoon",select) 
        self.action(capture=1)

    def use_popup(self, select):
        #ハイライト通知　１する、２しない
        self.xpath = "(//input[@name='{}'])[{}]".format("usePopup",select) 
        self.action(capture=1)

    def download_img(self, select, mail_address="", delete=False, delete_address=""):
        #画像の自動ダウンロード　１する、２しない、しないときにmail_addressを信頼するメールアドレスに登録
        #登録したアドレスを削除するにはdelete=True、delete_address=削除するアドレス
        self.xpath = "(//input[@name='{}'])[{}]".format("downloadImg",select) 
        self.action(capture=1)

        if select == 2 and mail_address:
            self.xpath = "//input[@name='address']"
            self.action(do="send_keys", content=mail_address)

            self.xpath = "//settings-safety-address-list//*[contains(text(),'追加')]"
            self.action(capture=1)

        if delete:
            self.xpath = "//*[contains(text(),'{}')]/parent::*//following-sibling::*//*[contains(@class,'CloseRed')]".format(delete_address)
            self.action(capture=1)


    def auto_save_address(self,select):
        #アドレス自動保存
        self.xpath = "(//input[@name='{}'])[{}]".format("autoSaveAddress",select) 
        self.action(capture=1)

    def use_autocomplete(self,select):
        #オートコンプリート使用 select、１：保存、２：しない
        self.xpath = "(//input[@name='{}'])[{}]".format("useAutocomplete",select) 
        self.action(capture=1)

    def set_prefix(self, prefix_contents):
        #プリフィックス変更
        self.xpath = "//input[@name='prefix']"
        content = prefix_contents
        self.action(do="send_keys", content=content, capture=1)



    def change_theme(self, selection):
        #テーマ変更　selection="Panda""Manta""Flamingo""プレーン"
        self.xpath = "//select[@name='theme']"
        self.action(do = "select", content = selection)


    def change_language(self, selection):
        self.xpath = "//select[@name='language']"
        self.action(do = "select", content = selection)
        


    def display_size(self, select):
        #文字サイズ　select =1,2,3で大中小
        self.xpath = "(//input[@name='{}'])[{}]".format("displaySize",select) 
        self.action(capture=1)


    def select_datatype_import(self, select):
        #インポートタイプ　select =1メール、2アドレスブック
        self.xpath = "(//input[@name='{}'])[{}]".format("raido300",select) 
        self.action()

        if select==2:
            self.xpath = "//select[@name='samplename']" 
            self.action(do = "select", content = "OCNメール")


    def select_datatype_export(self, select):
        #エクスポートタイプ　select =1メール、2アドレスブック
        self.xpath = "(//input[@name='{}'])[{}]".format("radio310",select) 
        self.action()

    # def upload_file(self, file_path):
    #     #ファイルアップロード　
    #     #self.xpath = "//settings-import-export//*[contains(text(),'ファイル選択')]/parent::*//input[@type='file']"
    #     self.xpath = "//input[@type='file']"
    #     self.action(do="send_keys", content=file_path, capture=1)

    def file_import(self):
        #インポートボタン　「インポートに成功しました」
        self.xpath = "//*[contains(text(),'インポート') and contains(@class,'btn')]"
        self.action(do="", capture=1) #ボタンを押す前にキャプチャ
        self.action()

    def file_export(self):
        #エクスポートボタン　「インポートに成功しました」
        self.xpath = "//settings-import-export//*[contains(text(),'エクスポート') and contains(@class,'btn')]"
        self.action(do="", capture=1) #ボタンを押す前にキャプチャ
        self.action(capture=1)
        

    def save_change(self, english=False):
        #変更を保存する、
        if english:
            self.xpath = "//*[contains(text(),'Save changes')]" 
        else:
            self.xpath = "//*[contains(text(),'変更を保存')]" 
        
        self.action()

    def change_settings(self, set="", select=1, params={}, assert_if=True):
        """
        set=変更項目、
        select=選択肢、上から１，２，３…
        params=変更内容、変更項目によって異なる
        assert_if、設定保存メッセージをキャプチャするかどうか
        """

        #設定画面でアドレス自動保存
        self.xpath = "//a[contains(@href, '#/settings')]" 
        self.action()

        #選択値の変更
        if set in ["auto_save_address","use_autocomplete"]:
            if set == "auto_save_address":
                if select == 1: #自動保存する
                    self.xpath = "(//input[@name='{}'])[1]".format("autoSaveAddress") 
                if select == 2: #自動保存しない
                    self.xpath = "(//input[@name='{}'])[2]".format("autoSaveAddress") 
            elif set == "use_autocomplete":
                if select == 1: #自動保存する
                    self.xpath = "(//input[@name='{}'])[1]".format("useAutocomplete") 
                if select == 2: #自動保存しない
                    self.xpath = "(//input[@name='{}'])[2]".format("useAutocomplete") 
                    
            self.action(capture=1)


        #内容の変更
        if set in ["prefix","password"]:

            if set == "prefix":
                self.xpath = "//input[@name='prefix']"
                content = params["content"]
                self.action(do="send_keys", content=content, capture=1)

            if set == "password":
                self.xpath = "//button[contains(text(),'パスワードを変更')]"
                self.action()

                self.xpath = "//input[@ng-reflect-name='oldPassword']"
                content = params["PASSWORD"]
                self.action(do="send_keys", content=content)

                self.xpath = "//input[@ng-reflect-name='newPassword']"
                content = params["PASSWORD_NEW"]
                self.action(do="send_keys", content=content)
                
                self.xpath = "//input[@ng-reflect-name='confirmNewPassword']"
                content = params["PASSWORD_NEW"]
                self.action(do="send_keys", content=content)

                self.xpath = "//*[contains(@class,'modalWindowBtn')]//*[contains(text(),'変更')]"
                self.action(capture=1)

                self.xpath = "//*[contains(@class,'isOn')]//*[contains(text(),'OK')]"
                self.action()

                self.xpath = "//*[contains(text(),'変更が保存されました')]"
                self.assertTrue(self.action(do="",capture=1, assert_if=1))                

        self.xpath = "//*[contains(text(),'変更を保存')]" 
        self.action()

        if assert_if:
            pass

        time.sleep(3)


    def import_initial_mail_data(self):
        #メール初期データインポート

        file_list = self.initial_params_j["file_list_mail"]
        data_folder = self.initial_params_j["data_folder"]
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
            
            #self.upload_file(path)
            self.file_import()
            self.assert_message("インポートに成功しました")

            self.confirm_mail_box(file_n.split("_")[-1])
            #self.delete_mail_box(file_n.split("_")[-1])

    def import_initial_address_data(self):
        #アドレス初期データインポート
        
        file_list = self.initial_params_j["file_list_address"]
        data_folder = self.initial_params_j["data_folder"]
        #address_list = [name.split("_")[-1] for name in file_list]
        address_book_name = self.initial_params_j["address_book_name"]

        base_path=os.getcwd()

        self.confirm_address_book(keyword="連絡先")

        #インポート
        for file_n in file_list:
            path = os.path.join(base_path, data_folder, file_n) + ".tgz"

            self.setting_page()
            self.select_datatype_import(select=2)

            self.xpath = "//settings-import-export//input[@type='file']"
            time.sleep(1)
            el = self.browser.find_element_by_xpath(self.xpath)
            time.sleep(1)
            el.send_keys(path)
            
            #self.upload_file(path)
            self.file_import()
            self.assert_message("インポートに成功しました")

            self.confirm_address_book(keyword=address_book_name)
            #self.delete_mail_box(file_n.split("_")[-1])

    def delete_initial_mail_data(self):
        #初期メールデータの削除
        for file_n in self.initial_params_j["file_list_mail"]:
            mail_box = file_n.split("_")[-1]
            try:
                self.delete_mail_box(keyword=mail_box)
            except:
                print("can not remove",mail_box)


    def delete_initial_address_data(self):
        #初期アドレスデータ削除

        for file_n in self.initial_params_j["address_book_list"]:
            try:
                self.delete_address_book(address_book_name=file_n)
            except:
                print("can not remove",file_n)
    



    def showSettingView(self, moveSetview=False, showType=0):
        '''
        showSettingView 設定画面の画面切り替え
        moveSetview
            True    移動前に設定画面に遷移する
            False   設定画面に遷移しない

        showType    設定画面の特定機能の画面に遷移する
            0   :メールアカウント
            1   :メール
            2   :署名
            3   :フィルター管理
            4   :迷惑メール自動判定
            5   :アカウント設定
            6   :自動転送設定
            7   :表示
            8   :インポート/エクスポート
            9   :迷惑メールブロックサービス
        '''
        # 設定画面の画面切り替え
        typeName="#/settings#mailSettings"

        if moveSetview:
            self.tagMove(2)
            pass

        # メールアカウント
        if showType == 0:
            typeName = "#/settings#mailAccount"
            pass
        # メール
        elif showType == 1:
            typeName = "#/settings#mailSettings"
            pass
        # 署名
        elif showType == 2:
            typeName = "#/settings#signature"
            pass
        # フィルター管理
        elif showType == 3:
            typeName = "#/settings#filterManagement"
            pass
        # 迷惑メール自動判定
        elif showType == 4:
            typeName = "#/settings#spamDetection"
            pass
        # アカウント設定
        elif showType == 5:
            typeName = "#/settings#accoutSettings"
            pass
        # 自動転送設定
        elif showType == 6:
            typeName = "#/settings#transferSettings"
            pass
        # 表示
        elif showType == 7:
            typeName = "#/settings#theme"
            pass
        # インポート/エクスポート
        elif showType == 8:
            typeName = "#/settings#importExport"
            pass
        # 迷惑メールブロックサービス
        elif showType == 9:
            typeName = "#/settings#spamBlock"
            pass
        # 表示処理
        self.xpath = "//*[@id='sidebar']/div[@class='menu menuType3 layoutTableWrapPc']//a[@href='{}']".format(typeName)
        self.action(capture=1)

        print(str(showType) + " 表示しました")


    ############################
    # フィルター 機能
    ############################
    def show_filter_dialog(self, showRenewView=True):
        # フィルターダイアログの変更
        # showRenewView : Trueなら 簡単設定, Falseなら 詳細設定

        renewalXpath = "//dialog-holder//dialog-wrapper//settings-filter//a[contains(text(),'詳細設定')]"
        existingXpath = "//dialog-holder//dialog-wrapper//settings-filter//a[contains(text(),'リニューアル版での設定')]"

        if self.element_find_xpath(find_xpath=renewalXpath):
            
            if not showRenewView:
                self.xpath = renewalXpath
                self.action()
                print("簡単設定から詳細設定に変更")
            else:
                print("簡単設定です")
        else:
            if showRenewView:
                self.xpath = existingXpath
                self.action()
                print("詳細設定から簡単設定に変更")
            else:
                print("詳細設定です")
            

    def fiter_create(self):        
        self.xpath = "//button[contains(text(),'新しいフィルタ')]" 
        self.action()

        ##############
        # 詳細設定 ダイアログに変更
        ##############

        self.show_filter_dialog(showRenewView=False)

        self.xpath = "//*[@class='modalWindow modalWindowType3 detailFilterWindow isOn']//input[@ng-reflect-name='filterName']"
        content = u"Newフィルター情報"
        self.action(do = "send_keys", content = content)

        self.xpath = "//*[@class='modalWindow modalWindowType3 detailFilterWindow isOn']//input[@ng-reflect-name='value']"
        content = u"私物の持ち込み"
        self.action(do = "send_keys", content = content)


        self.xpath = "//*[contains(text(),'アクション条件')]/parent::*/parent::*/following-sibling::*//select"
        self.action(do="select", content="破棄する", capture=1)

        self.xpath = "//settings-filter//*[contains(@class,'isOn')]//*[contains(text(),'OK')]"
        self.action()

        self.xpath = "//modal-dialog//*[contains(text(),'OK')]"
        self.action()
        self.assert_message("しました")
        

    def run_filter(self):
        # フィルター実行ボタンの押下
        self.xpath = "//button[contains(text(),'フィルターを実行')]" 
        self.action()

        self.xpath = "//folder-item//*[contains(text(),'BBQ')]"
        self.action(capture=1)

        self.xpath = "//*[contains(@class,'isOn')]//*[contains(text(),'OK')]"
        self.action(capture=1)
        self.assert_message("しました。")

        pass
        

    def renawalFilter(self):
        # フィルター設定(詳細設定画面の設定)
        self.xpath = "//*[contains(text(),'フィルター名')]/following-sibling::*//input" 
        content = u"seleniumフィルター" 
        self.action(do = "send_keys", content = content)
        
        time.sleep(1)
        
        self.xpath = "//*[contains(text(),'差出人：')]/following-sibling::*//input" 
        content = "selenium@chickenmail01.techfirm.co.jp" 
        self.action(do = "send_keys", content = content)
        
        time.sleep(1)
        
        self.xpath = "//*[contains(text(),'宛先：')]/following-sibling::*//input" 
        content = "seleniumnakayosi@chickenmail01.techfirm.co.jp" 
        self.action(do = "send_keys", content = content)
        
        time.sleep(1)
        
        self.xpath = "//*[contains(text(),'件名：')]/following-sibling::*//input"  
        content = "seleniumsubj" 
        self.action(do = "send_keys", content = content)
        
        time.sleep(1)
        
        self.xpath = "//*[contains(text(),'本文：')]/following-sibling::*//input"  
        content = "seleseleniumtext" 
        self.action(do = "send_keys", content = content)
        
        time.sleep(1)
        
        self.xpath = "//settings-filter/div/form/div[2]/div[3]/div[2]/div/div[2]/select" 
        content = u"を含まない" 
        self.action(do = "select", content = content)
        
        time.sleep(1)
        
        self.xpath = "//*[contains(@class,'isOn')]//*[contains(text(),'既読にする')]/preceding-sibling::input" 
        self.action()
        
        time.sleep(1)
        
        self.xpath = "//*[contains(@class,'isOn')]//*[contains(text(),'フラグをつける')]/preceding-sibling::input" 
        self.action()
        
        time.sleep(1)
        
        self.xpath = "//settings-filter//*[contains(text(),'OK')]" 
        self.action()
        
        time.sleep(1)
        
        self.xpath = "//modal-dialog//*[contains(text(),'OK')]" 
        self.action()

        time.sleep(1)

        self.xpath = "//a[contains(@href, '#/settings')]" 
        self.action()

        time.sleep(1)

        self.xpath = "//*[contains(text(),'seleniumフィルタ')] /parent::*/parent::*/following-sibling::*//button[contains(text(),'編集')]" 
        self.action()

        time.sleep(1)

        self.xpath = "//*[contains(text(),'フィルター名')]/following-sibling::*//input" 
        content = u"seleniumフィルター編集した" 
        self.action(do = "send_keys", content = content)

        time.sleep(1)
        
        self.xpath = "//*[contains(@class,'isOn')]//*[contains(text(),'既読にする')]/preceding-sibling::input" 
        self.action()

        time.sleep(1)
        
        self.xpath = "//settings-filter//*[contains(text(),'OK')]" 
        self.action()
        
        time.sleep(1)
        
        self.xpath = "//modal-dialog//*[contains(text(),'OK')]" 
        self.action()

        time.sleep(1)

        self.xpath = "//a[contains(@href, '#/settings')]" 
        self.action()
        
        #フィルター削除
        time.sleep(10)
        self.xpath = "//a[contains(@href, '#/settings')]" 
        self.action()

        time.sleep(1)
        self.xpath = "//div[@id='mainContents']/div[24]/div[2]/div[2]/div/div[3]/div[3]/div/div[3]/span/span[2]" 
        self.xpath = "//*[contains(text(),'seleniumフィルタ')] /parent::*/parent::*/following-sibling::*//span[@class='btn']"
        self.action()

        time.sleep(1)

        self.xpath = "//modal-dialog//*[contains(text(),'OK')]" 
        self.action()

        time.sleep(1)

        self.xpath = "//a[contains(@href, '#/settings')]" 
        self.action()

    def fiter_del(self):
         # フィルターの削除
        self.capture()
        print("Fiter Delete")
        time.sleep(5)
        self.xpath = "//*[contains(text(),'Newフィルター情報')]/parent::*/parent::*/following-sibling::*//span[@class='btn']"
        self.action(capture=1)

        self.xpath = "//*[contains(@class,'isOn')]//*[contains(text(),'OK')]"
        self.action()
        self.assert_message("しました")

        pass

    def fiter_update(self):
         # フィルターの変更処理
        pass

    ##############################
    #  外部アカウント
    ##############################

    def outside_connection(self, address="",id="", pw="", user_name="", server="",ssl=True):
        # 外部アカウント紐付け
        self.xpath = "//*[contains(text(),'外部アカウントを追加')]"
        self.action()

        self.inputData("//*[contains(@class,'isOn')]//div[contains(text(),'メールアドレス')]/parent::*//input", address)
        self.inputData("//*[contains(@class,'isOn')]//div[contains(text(),'アカウント名')]/parent::*//input", user_name)


        # ラジオボタン
        self.xpath = "//*//*[contains(@class,'isOn')]//div[contains(text(),'アカウントの種類')]/parent::*//input[@ng-reflect-value='1']"
        self.action()

        self.inputData("//*[contains(@class,'isOn')]//div[contains(text(),'アカウントのユーザー名')]/parent::*//input", id)

        self.inputData("//*[contains(@class,'isOn')]//div[contains(text(),'メールサーバー')]/parent::*//input", server)
        self.inputData("//*[contains(@class,'isOn')]//div[contains(text(),'パスワード')]/parent::*//input", pw)

        # 1個目だから対処できる
        self.xpath = "//*[contains(text(),'このサーバーにアクセスするときに暗号化接続（SSL）を使用')]/parent::*/input"
        self.action(capture=1)

        # 接続テストを実行
        self.xpath = "//*[contains(@class,'isOn')]//*[contains(text(),'設定をテスト')]"
        self.action(capture=1)

        self.capture()
        # アカウントのテスト接続完了時のダイアログ[OK]
        print("アカウントのテスト接続完了時のダイアログ[OK]")
        self.xpath = "//*[contains(@class,'isOn')]//*[contains(@class,'btn btnBlock btnType2') and //*[contains(text(),'OK')]]"
        self.action(wait=1,capture=1)

        time.sleep(3)

        # 下部のOKボタンを押下
        print("下部のOKボタンを押下")
        self.xpath = "//*[contains(@class,'isOn')]//*[contains(text(),'OK')]"
        self.action(capture=1)

        # 保存時の確認ダイアログ
        self.xpath = "//modal-dialog//div[@class='modalWindow isOn']//*[contains(text(),'OK')]"
        self.action(capture=1)
        self.assert_message("変更が保存されました。")
        
        pass

    def outside_disconnect(self, text=""):
        ''' outside_disconnect 外部アカウントの削除
        text 削除するユーザのメールアドレスまたはアカウント名を入力すること
        '''

        self.showSettingView(moveSetview=True, showType=5)
        self.xpath = "//*[contains(text(),'{}')]/parent::*//span[@class='btn']".format(text)
        self.action()

        self.xpath ="//modal-dialog//div[@class='modalWindow isOn']//*[contains(text(),'OK')]"
        self.action()

        errorFlag =  self.element_find_xpath_wait(find_xpath="//modal-dialog//*[contains(text(),'OK')]", wait_time=1)
        print("フラグ結果： " + str(errorFlag))

        while errorFlag:
            print("エラーダイアログが表示されました 閉じます")
            self.xpath = "//modal-dialog//*[contains(text(),'OK')]"
            self.action()

            print("15秒待機します")
            time.sleep(15)

            self.xpath = "//*[contains(text(),'{}')]/parent::*//span[@class='btn']".format(text)
            self.action()
            self.xpath ="//modal-dialog//div[@class='modalWindow isOn']//*[contains(text(),'OK')]"
            self.action()

            errorFlag =  self.element_find_xpath_wait(find_xpath="//modal-dialog//*[contains(text(),'OK')]", wait_time=10)
            print("フラグ結果： " + str(errorFlag))

        print("削除処理が終了しました")


        pass

    def outside_change_user_name(self,user_name, after_name, pw):
        '''
        アカウント名を変更する
        user_name：変更前のユーザ名
        after_name；変更後のユーザ名
        '''

        print("outside_change_user_name")
        
        self.showSettingView(moveSetview=True, showType=5)
        
        # 編集ボタンの押下
        print("編集ボタンを押下")
        self.xpath = "//*[contains(text(),'{}')]/parent::*//button".format(user_name)
        self.action(capture=1)

        # アカウント名の変更
        print("アカウント名の変更")
        self.inputData("//*[contains(@class,'isOn')]//div[contains(text(),'アカウント名')]/parent::*//input", after_name)

        # パスワードの設定
        print("パスワードの変更1")
        self.inputData("//*[contains(@class,'isOn')]//div[contains(text(),'パスワード')]/parent::*//input", pw)

        # 下部のOKボタンを押下
        print("アカウントのテスト接続完了時のダイアログ[OK]1")
        self.xpath = "//*[contains(@class,'isOn')]//*[contains(text(),'OK')]"
        self.action(capture=1)
        time.sleep(0.5)

        # 保存時の確認ダイアログ
        print("保存時の確認ダイアログ1")
        self.xpath = "//modal-dialog//*[contains(text(),'OK')]"
        self.action()

        # エラーダイアログが出ているか確認する

        errorFlag =  self.element_find_xpath_wait(find_xpath="//modal-dialog//*[contains(text(),'OK')]")
        print("フラグ結果： " + str(errorFlag))

        while errorFlag:
            print("エラーダイアログが表示されました 閉じます")
            self.xpath = "//modal-dialog//*[contains(text(),'OK')]"
            self.action()

            print("20秒　に再度削除処理を実施する")
            time.sleep(20)

            # 下部のOKボタンを押下
            print("アカウントのテスト接続完了時のダイアログ[OK]2")
            self.xpath = "//*[contains(@class,'isOn')]//*[contains(text(),'OK')]"
            self.action(capture=1)


            # 保存時の確認ダイアログ
            print("保存時の確認ダイアログ2")
            self.xpath = "//modal-dialog//*[contains(text(),'OK')]"
            self.action()
            errorFlag = self.element_find_xpath_wait(find_xpath="//modal-dialog//*[contains(text(),'した')]",wait_time=1)

        print("アラートを確認")
        self.capture()
        self.assert_message("した")
        time.sleep(1)
        

        pass

    def inputData(self, xpath="", content=""):
        self.xpath = xpath
        self.action(do = "send_keys", content = content, capture = 1)
        pass


    def transfer_setting(self, trans_title="", trans_mail=""):

        # ボタンを押下()        
        self.xpath = "//button[contains(text(),'新しい転送設定')]"
        self.action()

        self.inputData(xpath="//*[contains(text(),'自動転送設定名')]/parent::*/parent::*//input", content=trans_title)
        self.inputData(xpath="//*[contains(text(),'転送先メールアドレス')]/parent::*/parent::*//input", content=trans_mail)

        # ラジオボタンの選択(転送メールの保存)
        self.xpath = "//*[contains(text(),'転送メールの保存')]/parent::*/parent::*//input[@ng-reflect-value='1']"
        self.action()

        # ラジオボタンの選択
        self.xpath = "//*[contains(text(),'転送の内容')]/parent::*/parent::*//input[@ng-reflect-value='0']"
        self.action()

        # ラジオボタンの選択(転送時間)
        self.xpath = "//*[contains(text(),'転送時間')]/parent::*/parent::*//input[@ng-reflect-value='0']"
        self.action()

        self.xpath = "//*[contains(@class,'isOn')]//*[contains(text(),'OK')]"
        self.action()

        self.xpath = "//*[contains(@class,'modalWindow isOn')]//*[contains(text(),'OK')]"
        self.action()
        self.assert_message("した")
        
        time.sleep(3)

        pass

    def transfer_active(self, title=""):
        self.showSettingView(moveSetview=True, showType=6)

        self.xpath = "//span[contains(text(),'{}')]/parent::*/parent::*//span[contains(text(),'変更')]".format(title)
        self.action(capture=1)

        self.xpath = "//*[contains(@class,'isOn')]//*[contains(text(),'OK')]"
        self.action()
        self.assert_message("設定が保存されました。")

        pass

    
    def transfer_del(self, title=""):
        self.showSettingView(moveSetview=True, showType=6)


        self.xpath = "//span[contains(text(),'{}')]/parent::*/parent::*//span[contains(@class,'icon iconCloseRed iconXSmall iconSpaceLeft1')]".format(title)
        self.action(capture=1)

        self.xpath = "//*[contains(@class,'isOn')]//*[contains(text(),'OK')]"
        self.action()
        self.assert_message("設定が保存されました。")

        pass


    def select_white_list(self, selection):
        #必着設定選択 selection= From、件名、宛先

        self.xpath = "//*[contains(text(),'{}で設定する')]".format(selection)
        self.action()

    def edit_white_list(self, content="", select=1, capture=0, clear=False):
        #必着設定編集、content=編集内容、select=何番目の項目を編集するか

        if clear:
            self.xpath = "//*[contains(@class,'isOn')]//*[contains(text(),'すべてクリア')]"
            self.action(do="",capture=1)
            self.action()

        self.xpath = "(//*[contains(@class,'isOn')]//input[@type='text'])".format(select)
        self.action(do="", capture=capture)
        self.action(do="send_keys", content=content)

    def save_white_list(self):
        #必着設定保存

        self.xpath = "//*[contains(@class,'isOn')]//*[contains(text(),'OK')]"
        self.action(do="", capture=1)
        self.action()

        self.xpath = "//modal-dialog//*[contains(text(),'OK')]"
        self.action()

    def import_white_list(self, path, capture=1):
        #必着設定インポート 設定を変更しています->変更が保存されました
        self.xpath = "//*[contains(@class,'isOn')]//input[@type='file']"
        self.action(clear=0, do="send_keys", content=path)

        self.xpath = "//*[contains(@class,'isOn')]//*[contains(text(),'選択ファイルを反映')]"
        self.action(do="", capture=capture)
        self.action()
        

    def export_white_list(self, capture=1):
        #必着設定エクスポート
        self.xpath = "//*[contains(@class,'isOn')]//*[contains(text(),'エクスポート')]"
        self.action(do="", capture=capture)
        self.action(capture=capture)

    def select_spam_info(self):
        #迷惑メール設定ボタン
        self.xpath = "//*[contains(text(),'迷惑メールブロックサービス')]/parent::*/following-sibling::*//button[contains(text(),'設定する')]"
        self.action()

    def edit_spam_info(self, select_1=0, select_2=0, selection="", capture=1):
        #迷惑メール設定編集
        # select_1,select_2=1,2
        #selection="毎日、毎週日曜日、送信しない"

        self.xpath = "(//input[@formcontrolname='subjectPrefix'])[{}]".format(select_1)
        self.action(do="",capture=capture)

        if select_1:
            self.xpath = "(//input[@formcontrolname='subjectPrefix'])[{}]".format(select_1)
            self.action()

        if select_2:
            self.xpath = "(//input[@formcontrolname='moveSpam'])[{}]".format(select_2)
            self.action()

        if selection:
            self.xpath = "//select[@formcontrolname='spamListSendInterval']"
            self.action(do="select", content=selection)

        self.xpath = "//*[contains(@class,'isOn')]//*[contains(text(),'OK')]"
        self.action(do="", capture=capture)
        self.action()

        self.xpath = "//modal-dialog//*[contains(text(),'OK')]"
        self.action()


    def edit_spam_open_eml(self):
        self.xpath="//*[contains(text(),'判定漏れ迷惑メール通報')]/parent::*/parent::*//*[contains(text(),'設定する')]"
        self.action()

