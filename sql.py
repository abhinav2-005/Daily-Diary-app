import mysql.connector
import os
class Sql_connection:
    def get_connectoin(self):
        return mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = os.environ.get("password"),
            database = 'dialy_diary_app'
        )
s = Sql_connection()
