import datetime
from typing import List
import sqlite3


class DataStorage:

    def __init__(self):
        self.db = sqlite3.connect('data_' + datetime.datetime.now().strftime('%Y%m%d_%H%M%S') + '.db')
        self.data_to_submit: list = []
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
        self.data_to_submit.append(
            {
                'type': type,
                'subtype': subtype,
                'value': value,
                'when_created': datetime.datetime.now()
            }
        )
        self.record_value_in_db(type, subtype, value)

    def record_value_in_db(self, type, subtype, value):
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

    def submit_data(self):
        print(self.data_to_submit)
        self.data_to_submit = []

if __name__ == '__main__':
    db_name = 'data_' + datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    print(db_name)