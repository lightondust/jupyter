import time
from models import BaseModel

class AddressManageModel(BaseModel.BaseModel):
    def __init__(self):
        pass

    def showMailFolder(self, target="" , capture="aaaa"):
        """ showMailFolder 特定のメールフォルダを開く
        target : 確認するメールフォルダ
        """
        self.xpath = "//a[contains(@href, '#/mail')]" 
        self.action(sleep=2)
        self.xpath = "//*[contains(@class,'sidebar')]//*[contains(text(),'{}')]".format(target) 
        self.action(sleep=2, capture=1)


    def searchAddress(self, searchKey=""):
        # アドレスの検索
        # アドレス一覧表示画面から特定のアドレスを検索する
        self.xpath = "//*[@id='contentsHeader']//*[@type='search']" 
        content = searchKey  
        self.action(do = "send_keys", content = content)

        self.xpath = "//*[@id='contentsHeader']//*[@class='searchBtn']"
        self.action(do = "click", capture=1)

    def addressListOnClick(self, searchKey=""):
        # アドレス選択
        # アドレス一覧表示画面から特定のアドレスを選択して詳細を表示する

        self.xpath = "//*[@id='mainContents']//div[@class='listItem']//*[contains(text(),'{}')]".format(searchKey)
        self.action(do = "double_click", capture=1)


    def addGroupMove(self, moveAddBookName=""):
        # アドレスグループの移動
        self.xpath = "//*[@id='contentsHeader']//navi-item[@icon='iconMove']//div[@class='navItem']"
        self.action(do = "click")

        self.xpath = "//*[@id='contentsWrap']//div[@class='modalWindow selectAdbookWindow isOn']//address-book-list//div[@class='menuText']//a[contains(text(),'{}')]".format(moveAddBookName)
        self.action(do = "click", capture=1)

        self.xpath = "//div[@class='modalWindow selectAdbookWindow isOn']//div[@class='modalWindowBtnSet']//div[@class='modalWindowBtn']//*[contains(text(),'OK')]"
        self.action(do = "click")

    def selectAddressGroup(self, address_book="連絡先"):
        #アドレス、アドレスグループ削除
        print("連絡先の表示 [" + address_book +"]")

        self.xpath = "//*[contains(@class,'sidebar')]//*[contains(text(),'{}')]".format(address_book) 
        self.action(sleep=3)


    def groupDel(self, moveAddBookName=""):
        # グループの削除：グループの画面を表示している時のみ実行可能
        self.xpath = "//*[@id='contentsHeader']//navi-item[@icon='iconTrash']//div[@class='navItem']"
        self.action(do = "click", capture=1)
        time.sleep(2)

        self.xpath = "//modal-dialog//div[@class='modalWindow isOn']//*[contains(text(),'OK')]"
        self.action(do = "click")

        time.sleep(2)

    def mailDel(self, moveAddBookName=""):
        # グループの削除：グループの画面を表示している時のみ実行可能
        self.xpath = "//*[@id='contentsHeader']//navi-item[@icon='iconTrash']//div[@class='navItem']"
        self.action(do = "click", capture=1)
        time.sleep(2)

        self.xpath = "//modal-dialog//div[@class='modalWindow isOn']//*[contains(text(),'OK')]"
        self.action(do = "click")

        time.sleep(2)

