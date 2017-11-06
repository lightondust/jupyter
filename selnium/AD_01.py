import unittest
from models import test_class
import time
import inspect
import os

file_name = __file__.split("\\")[-1].split(".")[0]

class Test_Case(test_class.Test_Class):
    file_name = __file__.split("\\")[-1].split(".")[0]
    # not_login = 1

    def test_AD_01(self):
        # LOGIN_ADD = self.params_j["LOGIN_ADD"]
        # LOGIN_PW = self.params_j["LOGIN_PW"]
        TAG_NAME = self.params_j["TAG_NAME"]

        # アドレスグループ情報
        ADDRESS_GROUP_NAME = self.params_j["ADDRESS_GROUP_NAME"]
        ADDRESS_GROUP_MAIL = self.params_j["ADDRESS_GROUP_MAIL"]
        ADDRESS_GROUP_MEMBAR_NAME = self.params_j["ADDRESS_GROUP_MEMBAR_NAME"]

        # TAG名
        TAG_NAME = self.params_j["TAG_NAME"]
        
        # アドレス登録情報
        save_address_data = {
            "family_name"       : self.params_j["FAMILY_NAME"],
            "last_name"         : self.params_j["LAST_NAME"],
            "family_name_kana"  : self.params_j["FAMILY_NAME_KANA"],
            "last_name_kana"    : self.params_j["LAST_NAME_KANA"],
            "company"           : self.params_j["COMPANY"],
            "company_kana"      : self.params_j["COMPANY_KANA"],
            "mail_address"      : self.params_j["MAIL_ADDRESS"],
            "address_book"      : self.params_j["ADDRESS_BOOK"]
        }

        # LOGIN 
        # print("LOGIN")
        # self.login(id_v=LOGIN_ADD, pd_v=LOGIN_PW,capture=1)


        self.import_initial_address_data()
        

        # アドレスページを表示
        print("アドレスページを表示")
        self.tagMove(1)
        self.capture()

        # アドレス保存
        print("アドレス保存")
        self.save_address(save_address_data,address_book = save_address_data["address_book"])

        # 連絡先の表示
        self.selectAddressGroup(save_address_data["address_book"])
        self.capture()

        # 検索
        print("検索[" + save_address_data["family_name"] + "]")
        self.searchAddress(searchKey=save_address_data["family_name"])
        time.sleep(2)
        self.capture()


        # アドレスの詳細画面に遷移する
        self.addressListOnClick(searchKey=save_address_data["family_name"])

        # タグ追加
        self.save_tag(tag_name=TAG_NAME)

        # タグ紐付け
        print("タグ紐付け [" + TAG_NAME + "]")
        self.tag_setinng_for_address(select_add_book=save_address_data["address_book"], address_name=save_address_data["family_name"], tag_name=TAG_NAME)

        # タグの確認
        print("タグの確認 [" + TAG_NAME + "]")
        self.showTagAddress(target=TAG_NAME)


        # 連絡先の表示
        self.selectAddressGroup(save_address_data["address_book"])
        self.capture()

        # 検索
        print("検索[" + save_address_data["family_name"] + "]")
        self.searchAddress(searchKey=save_address_data["family_name"])
        time.sleep(1)
        self.capture()

        # アドレスの詳細画面に遷移する
        self.addressListOnClick(searchKey=save_address_data["family_name"])

        

        # タグの削除
        print("タグの削除 [" + TAG_NAME + "]")
        self.delete_address_tag(tag_name=TAG_NAME,show_capture=True)


        # アドレス開く
        print("アドレス表示 [" + save_address_data["family_name"] + "]")
        self.confirm_address(address_book=save_address_data["address_book"], keyword=save_address_data["family_name"])
        self.addressListOnClick(searchKey=save_address_data["family_name"])
        self.capture()

        # アドレス削除
        print("アドレスの削除 [" + save_address_data["family_name"] + "]")
        self.mailDel(moveAddBookName=save_address_data["family_name"])

        # 連絡先の表示
        self.selectAddressGroup(save_address_data["address_book"])
        self.capture()

        # 検索
        print("検索[" + save_address_data["family_name"] + "]")
        self.searchAddress(searchKey=save_address_data["family_name"])
        time.sleep(1)
        self.capture()



        self.delete_initial_address_data()
        
 


if __name__ == '__main__':
    unittest.main()