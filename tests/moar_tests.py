
import pandas as pd
import mysql.connector
from mysql.connector import errorcode


try:
    connection = mysql.connector.connect (host = "localhost",
                       user = "root",
                       passwd = "7SwwJ3y8",
                       db = "assets_data")
    print("\nConnected")
except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Incorrect user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)

df = pd.read_sql('select timestamp, last, baseVolume from poloniex_ticker where currencyPair = "BTC_ETH";', con=connection, parse_dates=True, index_col='timestamp')
print('loaded dataframe from MySQL. records:', len(df))
connection.close()

df.set_index(pd.DatetimeIndex(data=df['timestamp']), inplace=True)

print(df)