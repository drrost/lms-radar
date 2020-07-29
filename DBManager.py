import sqlite3
import time
import os

class DBManager:
    database = "lms.db"
    connection = None

    def __init__(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        db_path = dir_path + "/" + self.database
        self.create_connection(db_path)

    def create_connection(self, database):
        try:
            self.connection = sqlite3.connect(database)
        except sqlite3.Error as e:
            print(e)

    def create_seat(self, seat):
        sql = "INSERT INTO seat(workplace, xlogin, date_time) VALUES ('" +\
              seat['workplace'] + "','" +\
              seat['user'] + "', " +\
              str(time.time()) + ")"
        cur = self.connection.cursor()
        cur.execute(sql)
        self.connection.commit()

    def fetch_data(self):
        sql = "SELECT DISTINCT xlogin FROM seat ORDER BY xlogin"
        cur = self.connection.cursor()
        cur.execute(sql)
        return cur.fetchall()
