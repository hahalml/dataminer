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


    def insert(self, table, data):
        # table <string>
        # data <dict> {"market" : "BTC-LTC", "price": 0.00031567}

        # Try to get table structure. If fail create new table with appropiate structure for our data,
        # starting with id and local timestamp

        try:
            self.cursor.execute("""SELECT * FROM {0} LIMIT 1""".format(table))
            desc = self.cursor.description
            t = ()
            for item in desc:
                t += (item[0],)
            print("data = ", data)
            print("data.keys = ", tuple(data.keys()))
            print("data.values = ", tuple(data.values()))
            # sql = """INSERT INTO {0} {1} VALUES {2}""".format(table, tuple(data.keys()), tuple(data.values()))
            sql = """INSERT INTO {0} {1} VALUES {2}""".format(table, tuple(data.keys()), tuple(data.values()))
            print (sql)
            self.cursor.execute(sql, data)
            self.cursor.commit()
        except mysql.connector.errorcode as err:
            print("ERROR: {}".format(err))

        """
        query = ("INSERT INTO ethbtc_OHLC2 "
                                 "(time, open, high, low, close, vwap, volume, count)"
                                 "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")

        try:
            self.cursor.execute(query, data)
            # Commit data to database
            self.cnx.commit()
            print("Success!")
        except mysql.connector.Error as err:
            print("%s--> Insert was not executed" % (err))
        """

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

if __name__ == "__main__":
    db = Database(host='localhost', user='root', password='7SwwJ3y8', database='dataminer')
    #db.insert("ethbtc_OHLC2", {"market" : "BTC-LTC", "price": 0.00031567})
    rezolutii = [
        {"name" : "1", "description" : "data is collected at 1 minutes interval"},
        {"name" : "5", "description" : "data is collected at 5 minutes interval"},
        {"name" : "15", "description" : "data is collected at 15 minutes interval"},
        {"name" : "30", "description" : "data is collected at 30 minutes interval"},
        {"name" : "1h", "description" : "data is collected at 1 hours interval"},
        {"name" : "2h", "description" : "data is collected at 2 hours interval"},
        {"name" : "3h", "description" : "data is collected at 3 hours interval"},
        {"name" : "4h", "description" : "data is collected at 4 hours interval"},
        {"name" : "6h", "description" : "data is collected at 6 hours interval"},
        {"name" : "1d", "description" : "data is collected at 1 days interval"},
        {"name" : "1w", "description" : "data is collected at 1 week interval"},
        {"name" : "1m", "description" : "data is collected at 1 month interval"},
        {"name" : "1y", "description" : "data is collected at 1 year interval"}
    ]
    for each in rezolutii:
        db.insert("data_rezolution", each)
        print("done {}".format(each))

    #print(row)
