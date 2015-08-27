__author__ = 'force'
import mysql.connector
from mysql.connector import errorcode


class Database:


    def __init__(self, host='localhost', user='root', password='7SwwJ3y8', database='assets_data'):
        self.host = host
        self.user = user
        self.password = password
        self.db = database

        try:
            self.cnx = mysql.connector.connect(user=self.user, password=self.password,
                                               host=self.host, database=self.db, buffered=True)
            self.cursor = self.cnx.cursor()
            print("Connected to database: {}...".format(database))
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("ERROR: Incorrect user name or password!")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("ERROR: Database does not exist!")
            else:
                print(err)


    def insert(self, table, *data):
        # table <string>
        # data <list> or <tuple>

        # Try to get table structure. If fail create new table with same structure as our data, local timestamp, and id


        query = ("INSERT INTO ethbtc_OHLC2 "
                                 "(time, open, high, low, close, vwap, volume, count)"
                                 "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")

        try:
            self.cursor.execute(query, *data)
            # Commit data to database
            self.cnx.commit()
            print("Success!")
        except mysql.connector.Error as err:
            print("%s--> Insert was not executed" % (err))

    def get_last_timestamp(self):
        """
        :param column: string
        :return: last inserted value in column
        """
        sql = ("SELECT time FROM ethbtc_OHLC ORDER BY time DESC LIMIT 1")
        self.cursor.execute(sql)
        try:
            result = self.cursor.fetchone()[0]
        except:
            result = ""
        return result


    def __del__(self):
        self.cnx.commit()
        self.cursor.close()
        self.cnx.close()
        print("Connection closed")