import unittest
import codecs
import json
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from models import AddressManageModel, AddressModel, BaseModel, DisplayModel, EtcModel, ExAccountModel, InOutModel, LoginModel, MailModel, PortalModel, ProvisioningModel, ReciviveSettingModel, SettingsModel, ShowMailModel, TagModel, UtilModel

class Test_Class(unittest.TestCase, 
                AddressManageModel.AddressManageModel,
                AddressModel.AddressModel,
                DisplayModel.DisplayModel,
                EtcModel.EtcModel,
                ExAccountModel.ExAccountModel,
                InOutModel.InOutModel,
                LoginModel.LoginModel,
                MailModel.MailModel,
                PortalModel.PortalModel,
                ProvisioningModel.ProvisioningModel,
                ReciviveSettingModel.ReciviveSettingModel,
                SettingsModel.SettingsModel,
                ShowMailModel.ShowMailModel,
                TagModel.TagModel,
                UtilModel.UtilModel):

    # RESULT_DIR = ["evidence"]
    PARAMS_FILE = "params.json"
    
    not_login = 0
    file_no = 1
    
    def setUp(self):
        '''
        not_login=1をtestクラスの下に書くと自動ログインしない
        '''

        #全体パラメータ
        file_o = codecs.open(self.PARAMS_FILE,"r","utf-8")
        params_j = json.load(file_o)
        file_o.close()

        self.URL = params_j["URL"]
        self.id_v = params_j["settings"]["id"]
        self.pd_v = params_j["settings"]["password"]
        self.URL_admin = params_j["URL_admin"]
        self.id_admin = params_j["settings"]["id_admin"]
        self.pd_admin = params_j["settings"]["pd_admin"]
        self.URL_operator = params_j["URL_operator"]
        self.id_operator = params_j["settings"]["id_operator"]
        self.pd_operator = params_j["settings"]["pd_operator"]
        self.pd_operator_new = params_j["settings"]["pd_operator_new"]
        
        self.id_LO_01 = params_j["settings"]["id_LO_01"]
        self.pd_LO_01 = params_j["settings"]["pd_LO_01"]
        self.pd_LO_01_new = params_j["settings"]["pd_LO_01_new"]
        self.id_CO_01 = params_j["settings"]["id_CO_01"]
        self.pd_CO_01 = params_j["settings"]["pd_CO_01"]
        self.id_MD_02_recieve = params_j["settings"]["id_MD_02_recieve"]
        self.pd_MD_02_recieve = params_j["settings"]["pd_MD_02_recieve"]
        self.id_MD_02_transfer = params_j["settings"]["id_MD_02_transfer"]
        self.pd_MD_02_transfer = params_j["settings"]["pd_MD_02_transfer"]
        self.id_GA_01 = params_j["settings"]["id_GA_01"]
        self.pd_GA_01 = params_j["settings"]["pd_GA_01"]

        self.browser_selected = params_j["settings"]["browser"]
        self.initial_params_j = params_j["initial_params"]
        self.RESULT_DIR = params_j["evidence_folder"]

        self.dir_path = ""
        for dir_e in self.RESULT_DIR:
            if dir_e:
                self.dir_path = os.path.join(self.dir_path, dir_e)

        #エビデンス、フォルダ、上の階層
        if os.path.exists(self.dir_path):
            pass
        else:
            os.mkdir(self.dir_path)

        #シナリオ用のフォルダパス
        self.dir_path = os.path.join(self.dir_path, self.file_name)

        #エビデンス、フォルダ、下の階層
        if os.path.exists(self.dir_path):
            pass
        else:
            os.mkdir(self.dir_path)


        #テストデータ読み込み
        file_input = self.file_name + ".json"
        file_o = codecs.open(file_input, "r", "utf-8")
        self.params_j = json.load(file_o)
        file_o.close()

        if "import_initial_mail" in self.params_j:
            self.import_initial_mail = self.params_j["import_initial_mail"]
        else:
            self.import_initial_mail = False

        if "delete_initial_mail" in self.params_j:
            self.delete_initial_mail = self.params_j["delete_initial_mail"]
        else:
            self.delete_initial_mail = False

        if "import_initial_address" in self.params_j:
            self.import_initial_address = self.params_j["import_initial_address"]
        else:
            self.import_initial_address = False

        if "delete_initial_address" in self.params_j:
            self.delete_initial_address = self.params_j["delete_initial_address"]
        else:
            self.delete_initial_address = False

        #ブラウザ立ち上げ
        self.browser = self.start(self.browser_selected)

        #ログイン
        if self.not_login:
            pass
        else:
            try:
                #ログイン
                self.login(self.id_v, self.pd_v)
            except:
                self.browser.close()
                print("ログイン失敗")
                raise

        #初期データインポート

        if self.import_initial_mail:
            self.import_initial_mail_data()

        if self.import_initial_address:
            self.import_initial_address_data()




    def tearDown(self):
        #初期データ削除

        if self.delete_initial_mail:
            self.delete_initial_mail_data()

        if self.delete_initial_address:
            self.delete_initial_address_data()

        self.browser.quit()

    def action(self, do="click", wait=1, content="", scroll=1, 
        capture=0, clear=1, 
        assert_if=0, capture_false=1, false_is_error=1,
        sleep=1, wait_time=10):
        """指定xpathのエレメントに対して指定の仕様で動作をする：
        wait=0は待たない。
        wait=1で要素が現れるのを待つ
        do="click"はクリック。
        do="send_keys"で要素に入力、content="入力内容"
        do="select"はセレクトボックス、content="選択値"
        do=""は何もしない（do="",wait=1コンビで要素が現れるのを待ってキャプチャする）。
        scroll=2でボトムまでスクロールする。
        scroll=1で要素までスクロールする。
        scroll=0はスクロールしない。
        captureは正常場合のキャプチャするか否か
        capture_falseは異常の場合のキャプチャするか否か
        false_is_errorは異常の場合にエラーとしてキャプチャするか否か
        wait_time：要素が現れるのを待つ時間
        """

        file_name = self.file_name
        file_no = self.file_no
        browser = self.browser
        xpath = self.xpath

        time.sleep(sleep)

        try:
            #トップまでスクロール
            browser.execute_script("window.scrollTo(0, 0)")

            #要素を待つ
            if wait:
                el = WebDriverWait(browser, wait_time).until(
                    EC.presence_of_element_located((By.XPATH, xpath))
                    )
            else:
                el = browser.find_element_by_xpath(xpath)

            #要素までスクロール
            if scroll == 1:
                el.location_once_scrolled_into_view
                browser.execute_script("window.scrollBy(0,300)")
            elif scroll == 2:
                browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            
            #動作選択
            if do == "click":
                el.click()
            elif do == "double_click":
                ActionChains(browser).move_to_element(el).double_click(el).perform()
                #browser.execute_script("document.getElementById('INBOX-17').click()")
            elif do == "send_keys":
                if clear == 1:
                    el.clear()
                el.send_keys(content)
            elif do == "select":
                Select(el).select_by_visible_text(content)
            elif do == "edit_html_mail":
                xpath = '//*[@id="mail-edit_ifr"]'
                iframe = browser.find_element_by_xpath(xpath)
                browser.switch_to.frame(iframe)
                html = browser.find_element_by_xpath("//html")
                html.send_keys("edit html")
                body = browser.find_element_by_xpath("//body")
                body.send_keys("edit body")
                browser.switch_to.default_content()


            #エビデンスのキャプチャ
            if capture ==1:
                path = os.path.join(self.dir_path, \
                        file_name + "_" + str(file_no) + "_" + self.browser_selected + ".png")
                browser.save_screenshot(path)
                return True

            if assert_if:
                return True

        except:
            if capture_false == 1:
                if false_is_error:
                    path = os.path.join(self.dir_path, \
                            file_name + "_" + str(file_no) + "_" + self.browser_selected + "_error.png")
                    browser.save_screenshot(path)
                else:
                    path = os.path.join(self.dir_path, \
                            file_name + "_" + str(file_no) + "_" + self.browser_selected + ".png")
                    browser.save_screenshot(path)
            if assert_if:
                return False
            # print("error: case", file_name, "No.", file_no)
            raise
            
        finally:
            self.browser = browser
            if capture == 1:
                self.file_no = file_no + 1
#            self.file_no = self.no + 1




        




