import unittest
from models import test_class
import time
import inspect

file_name = __file__.split("\\")[-1].split(".")[0]

class Test_Case(test_class.Test_Class):
    file_name = __file__.split("\\")[-1].split(".")[0]

    def test_tag(self):

        # Login
        TAG_NAME = self.params_j["TAG_NAME"]

        # アドレス情報
        ADDRESS_NAME = self.params_j["ADDRESS_NAME"] + str(self.nowTime())
        ADDRESS_BOOK_FIRST = self.params_j["ADDRESS_BOOK_FIRST"]

        # アドレスグループ情報
        ADDRESS_GROUP_NAME = self.params_j["ADDRESS_GROUP_NAME"] + str(self.nowTime())
        ADDRESS_GROUP_MAIL = self.params_j["ADDRESS_GROUP_MAIL"]
        ADDRESS_GROUP_MEMBAR_NAME = self.params_j["ADDRESS_GROUP_MEMBAR_NAME"]

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

        add_address_group = {
            "group_name": ADDRESS_GROUP_NAME, 
            "group_member_name": ADDRESS_GROUP_MEMBAR_NAME,
            "group_member_address": ADDRESS_GROUP_MAIL,
        }

        # アドレスページを表示
        print("アドレスページを表示")
        self.tagMove(1)

        # アドレスグループ作成
        print("アドレスグループ作成")
        self.save_address_group(add_address_group, address_book = "連絡先")

        # 連絡先の表示
        print("連絡先の表示")
        self.selectAddressGroup("連絡先")
        self.capture()

        # 検索
        print("検索[" + ADDRESS_GROUP_NAME + "]")
        self.searchAddress(searchKey=ADDRESS_GROUP_NAME)
        self.capture()

        # グループの確認
        print("グループの確認 [" + ADDRESS_GROUP_NAME + "]")
        self.addressListOnClick(searchKey=ADDRESS_GROUP_NAME)
        self.capture()

        # アドレスブック追加
        print("アドレスブック追加 [" + ADDRESS_BOOK_FIRST + "]")
        self.save_address_book(address_book_name=ADDRESS_BOOK_FIRST)
        self.capture()

        # 検索
        print("検索 [" + ADDRESS_GROUP_NAME + "]")
        self.searchAddress(searchKey=ADDRESS_GROUP_NAME)
        self.capture()

        # グループの確認
        print("グループの確認 [" + ADDRESS_GROUP_NAME + "]")
        self.addressListOnClick(searchKey=ADDRESS_GROUP_NAME)
        self.capture()

        # アドレスブックの移動
        print("アドレスブックの移動 [" + ADDRESS_BOOK_FIRST + "]")
        self.addGroupMove(moveAddBookName=ADDRESS_BOOK_FIRST)
        self.capture()

        # アドレスブックの確認
        print("アドレスブックの確認 [" + ADDRESS_BOOK_FIRST + "]")
        self.selectAddressGroup(address_book=ADDRESS_BOOK_FIRST)

        # グループの確認
        print("グループの確認 [" + ADDRESS_GROUP_NAME + "]")
        self.addressListOnClick(searchKey=ADDRESS_GROUP_NAME)
        self.capture()

        # グループの削除
        print("グループの削除 [" + ADDRESS_GROUP_NAME + "]")
        self.groupDel(moveAddBookName=ADDRESS_GROUP_NAME)


        # 検索
        print("検索 [" + ADDRESS_GROUP_NAME + "]")
        self.searchAddress(searchKey=ADDRESS_GROUP_NAME)
        self.capture()

        # アドレスブックの削除
        print("アドレスブックの削除 [" + ADDRESS_BOOK_FIRST + "]")
        self.delete_address_book(address_book_name=ADDRESS_BOOK_FIRST)
        self.capture()

        time.sleep(2)
        pass

if __name__ == '__main__':
    unittest.main()