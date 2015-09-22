import pandas as pd
import mysql.connector
from mysql.connector import errorcode
import numpy as np
from datetime import datetime
from numpy.random import randint
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

df_mysql = pd.read_sql('select * from ethbtc_OHLC;', con=connection)
print('loaded dataframe from MySQL. records:', len(df_mysql))
connection.close()


# print(df_mysql)

select = [[1, "2015-08-27 17:53:20", 91, 2],
        # 17:55
        [2, "2015-08-27 17:59:11", 82, 5],
        # 18: 00
        [3, "2015-08-27 18:00:00", 96, 2],
        [4, "2015-08-27 18:00:11", 92, 1],
        [5, "2015-08-27 18:01:23", 79, 1],
        [6, "2015-08-27 18:01:40", 86, 10],
        [7, "2015-08-27 18:02:20", 78, 4],
        [8, "2015-08-27 18:03:59", 94, 3],
        [9, "2015-08-27 18:04:00", 97, 7],
        [10, "2015-08-27 18:04:17", 85, 8],
        [11, "2015-08-27 18:04:32", 90, 9],
        # 18:05
        [12, "2015-08-27 18:05:02", 99, 8],
        [13, "2015-08-27 18:05:27", 89, 2],
        [14, "2015-08-27 18:05:49", 84, 5],
        [15, "2015-08-27 18:05:55", 76, 6],
        [16, "2015-08-27 18:06:30", 75, 7],
        [17, "2015-08-27 18:06:42", 87, 2],
        [18, "2015-08-27 18:07:51", 88, 1],
        [19, "2015-08-27 18:07:55", 81, 3],
        [20, "2015-08-27 18:09:20", 95, 10],
        # 18:10
        [21, "2015-08-27 18:11:33", 77, 5],
        # 18:15
        [22, "2015-08-27 19:15:10", 98, 6],
        # 19:20
        [23, "2015-08-27 23:59:23", 80, 4],
        # 2015-08-28 00:00
        [24, "2015-08-28 01:32:33", 83, 6],
        # 01:35
        [25, "2015-08-29 11:12:43", 71, 5],
        # 11:15
        [26, "2015-08-29 11:26:53", 98, 3]]
        # 11:30

# convert string to datetime
# x = datetime.fromtimestamp(int((datetime.strptime("2015-08-27 17:53:20", "%Y-%m-%d %H:%M:%S")).timestamp()))


# create a list of dates in string
dates = []
for each in select:
    dates.append(each[1])

series_of_datetime = pd.to_datetime(pd.Series(dates))


index = pd.DatetimeIndex(series_of_datetime)


# create a new series
data = np.array(select)
# print(select)
pret = data[:, 2]
print(type(pret))
ts = pd.Series(pret.astype(float), index=index)


print(ts.resample('5Min', how="ohlc"))

