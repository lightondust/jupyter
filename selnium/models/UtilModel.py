import time
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
from models import MailModel, SettingsModel, AddressModel, UtilModel
from models import BaseModel

class UtilModel(BaseModel.BaseModel):
    def __init__(self):
        pass

    def start(self, selection):
        """指定のブラウザをそれぞれの仕様で立ち上げる"""
        base_path = os.getcwd()
        path = os.path.join(base_path,self.dir_path)

        if selection == "Chrome":
            chromeOptions = webdriver.ChromeOptions()
            prefs = {"download.default_directory" : path}
            chromeOptions.add_experimental_option("prefs", prefs)
            browser = webdriver.Chrome(chrome_options=chromeOptions)
            browser.maximize_window()

        elif selection == "Chromesp":
            browser = webdriver.Chrome()
            browser.set_window_size(412,732)

        elif selection == "Firefox":
            browser = webdriver.Firefox()
            browser.set_window_size(1936,1056)

        elif selection == "Android":
            browser = webdriver.Remote(desired_capabilities=DesiredCapabilities.ANDROID)
            browser.maximize_window()

        elif selection == "PhantomJS":
            browser = webdriver.PhantomJS()
            browser.set_window_size(1936,1056)

        elif selection == "Ie":
            browser = webdriver.Ie()
            browser.set_window_size(1936,1056)
        
        return browser

    def get_url(self, url):
        self.browser.get(url)

    def close_browser(self):
        self.browser.close()

    def get_css_property(self, property_select):
        #cssプロパティを読み取る
        self.action(do="")
        el = self.browser.find_element_by_xpath(self.xpath)
        return el.value_of_css_property(property_select)

    def assert_message(self,message, wait_time=10):
        #メッセージボックスの確認する
        self.xpath = "//*[contains(text(),'{}')]".format(message)
        self.assertTrue(self.action(do="",capture=1, assert_if=1, wait_time=wait_time))

        time.sleep(3)