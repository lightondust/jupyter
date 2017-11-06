import json
import os
import codecs
import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException

class BaseModel():

    def __init__(self):
        # print(INBOX_NAME)
        pass


    def capture(self):
        time.sleep(1)
        name = self.file_name + "_" + str(self.file_no) + "_" + self.browser_selected

        #エビデンスのキャプチャ
        path = os.path.join(self.dir_path, \
                name + ".png")
        self.browser.save_screenshot(path)
        self.file_no = self.file_no + 1
        return True


    def nowTime(self):
        now = datetime.datetime.now()
        return now.strftime("%Y%m%d%H%M%S") + "%04d" % (now.microsecond // 1000)

    def tagMove(self,type=0):
        #0:Mailタブ or 1:アオレスタブ or 2:設定タブ
        if (type==0):
            self.xpath = "//a[contains(@href, '#/mail')]"
        elif(type==1):
            self.xpath = "//a[contains(@href, '#/address')]"
        elif(type==2):
            self.xpath = "//a[contains(@href, '#/settings')]"
        
        self.action()

    def element_find_xpath(self, find_xpath=""):
        try :
            self.browser.find_element_by_xpath(find_xpath)
            return True
        except NoSuchElementException:
            return False

    def element_find_xpath_wait(self, find_xpath="",wait_time=10):

        try :
            WebDriverWait(self.browser, wait_time).until(EC.presence_of_element_located((By.XPATH, find_xpath)))
            return True
        except NoSuchElementException:
            return False
        except TimeoutException:
            return False

