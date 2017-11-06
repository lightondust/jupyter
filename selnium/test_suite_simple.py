import unittest
import codecs
import json
import os
from datetime import datetime
# テストケースを読み込む
import AD_01, AD_02, AD_03, CO_01, ET_02, ET_03, GA_01, IE_01, IE_02, LO_01, LO_03, MD_01, MD_02, MD_04, MD_05, MO_01, MO_02, MO_03, MO_04, MO_05, MV_01, MV_03, MV_04, MV_05, TG_01
import initial_data, final_data
from models import test_class

DIR_LOG = "log"
PARAMS_FILE = "params.json"

# テストスイートを作成
def suite():
    # テストスイート定義
    test_suite = unittest.TestSuite()

    # addTestを用いてテストスイートに追加
    # test_suite.addTest(unittest.makeSuite(ET_02.Test_Case))
    # test_suite.addTest(unittest.makeSuite(ET_03.Test_Case))
    # test_suite.addTest(unittest.makeSuite(IE_01.Test_Case))
    # test_suite.addTest(unittest.makeSuite(IE_02.Test_Case))
    # test_suite.addTest(unittest.makeSuite(AD_01.Test_Case))
    # test_suite.addTest(unittest.makeSuite(initial_data.Test_Case)) #初期データインポート

    # test_suite.addTest(unittest.makeSuite(AD_02.Test_Case))
    # test_suite.addTest(unittest.makeSuite(AD_03.Test_Case))
    # test_suite.addTest(unittest.makeSuite(GA_01.Test_Case))

    # test_suite.addTest(unittest.makeSuite(LO_01.Test_Case))
    # test_suite.addTest(unittest.makeSuite(LO_03.Test_Case))
    # test_suite.addTest(unittest.makeSuite(MD_01.Test_Case))
    # test_suite.addTest(unittest.makeSuite(MD_02.Test_Case))
    # test_suite.addTest(unittest.makeSuite(MD_04.Test_Case))
    # test_suite.addTest(unittest.makeSuite(MD_05.Test_Case))
    # test_suite.addTest(unittest.makeSuite(MO_01.Test_Case))
    # test_suite.addTest(unittest.makeSuite(MO_02.Test_Case))
    # test_suite.addTest(unittest.makeSuite(MO_03.Test_Case))
    # test_suite.addTest(unittest.makeSuite(MO_04.Test_Case))
    # test_suite.addTest(unittest.makeSuite(MO_05.Test_Case))
    # test_suite.addTest(unittest.makeSuite(MV_01.Test_Case))
    # test_suite.addTest(unittest.makeSuite(MV_03.Test_Case))
    # test_suite.addTest(unittest.makeSuite(MV_04.Test_Case))
    # test_suite.addTest(unittest.makeSuite(MV_05.Test_Case))
    test_suite.addTest(unittest.makeSuite(TG_01.Test_Case))

    # test_suite.addTest(unittest.makeSuite(CO_01.Test_Case)) #テーマ変更、途中で失敗して英語表示で終わると後のシナリオが全部失敗するので、最後に実行する

    # test_suite.addTest(unittest.makeSuite(final_data.Test_Case)) #終了後データ削除

    return test_suite


for a in range(0,25):
    #エビデンスフォルダを決める
    #params.jsonを読み込む

    file_o = codecs.open(PARAMS_FILE,"r","utf-8")
    params_j = json.load(file_o)
    file_o.close()

    #年月日時分のsuffixを作ってフォルダ名としてparams.jsonに挿入
    time_now = datetime.now()
    time_stamp = "".join([time_now.strftime('%Y') , time_now.strftime('%m') , time_now.strftime('%d')]) \
            + "_" + "".join([time_now.strftime('%H') , time_now.strftime('%M')])

    params_j["evidence_folder"][1] = time_stamp

    file_o = codecs.open(PARAMS_FILE,"w","utf-8")
    print(json.dumps(params_j, ensure_ascii=False),file=file_o)
    file_o.close()

    #ログファイルの出力先
    log_path = ""
    log_path = os.path.join(log_path,DIR_LOG)

    if os.path.exists(log_path):
        pass
    else:
        os.mkdir(log_path)
    
    if __name__ == "__main__":
        # 作成したテストスイートを呼び出して、TextTestRunnerで実行します
        file_log = codecs.open(os.path.join(log_path, time_stamp+".txt"),"w","utf-8")
        mySuite = suite()
        test_class.PARAMS_FILE = "params_suite.json"
        unittest.TextTestRunner(file_log).run(mySuite)

    #エビデンスフォルダ設定を戻す
    params_j["evidence_folder"][1] = ""
    
    file_o = codecs.open(PARAMS_FILE,"w","utf-8")
    print(json.dumps(params_j, ensure_ascii=False),file=file_o)
    file_o.close()
        