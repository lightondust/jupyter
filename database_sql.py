import pymysql.cursors


class Database():
    """mysqlのqueryをあたえて実行する"""

    def __init__(self):
        self.host = "localhost"
        self.user = "root"
        self.password = ""
        self.database = ""
        self.charset = "utf8"
        self.sql = ""

    def execute(self, sql="", is_display=False):
        """
        insertとupdateの時にだけcommitしている。
        deleteやcreateなどの場合は要対応
        """

        if not sql:
            sql = self.sql

        #接続
        connection = pymysql.connect(host=self.host,
                                    user=self.user,
                                    password=self.password,
                                    db=self.database,
                                    charset=self.charset,
                                    cursorclass=pymysql.cursors.DictCursor)

        # SQLを実行する
        with connection.cursor() as cursor:
            # try:
            #     cursor.execute(sql)
            # except cursor.IntegrityError:
            #     print("error")
            #     connection.close()
            #     return          

            try:
                cursor.execute(sql)
            except Exception as e:
                print(e, "error with: {}".format(sql))
                connection.close()
                return False

            # Select結果を取り出す
            results = cursor.fetchall()
            if is_display:
                for r in results:
                    print(r)

            if sql.startswith("insert") or sql.startswith("update"):
                connection.commit()
                connection.close()
                return True
            else:
                connection.close()
                return results