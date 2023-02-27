import datetime
import sqlite3


class DataStorage:

    def __init__(self):
        self.db = sqlite3.connect('data.db')
        self.setup()

    def setup(self):
        cursor = self.db.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS data (
                type, subtype, value, time
            )
            """
        )
        cursor.close()

    def record_value(self, type, subtype, value):
        cursor = self.db.cursor()
        cursor.execute(
            """
            INSERT INTO data 
            VALUES ('%s', '%s', '%s', '%s')
            """ % (type, subtype, value, datetime.datetime.now())
        )
        self.db.commit()
        cursor.close()

    def get_all(self):
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM data")
        response = cursor.fetchall()
        print(response)
        cursor.close()