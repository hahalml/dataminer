import pandas as pd
import mysql.connector
from mysql.connector import errorcode

"""
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
"""
# This is a sample of my data. It can also be a list of tuples, but I think it does not matter
select_result = [["2015-08-27 17:53:20", 91, 2],
                ["2015-08-27 17:59:11", 82, 5],
                ["2015-08-27 18:00:00", 96, 2],
                ["2015-08-27 18:00:11", 92, 1],
                ["2015-08-27 18:01:23", 79, 1],
                ["2015-08-27 18:01:40", 86, 10],
                ["2015-08-27 18:02:20", 78, 4],
                ["2015-08-27 18:03:59", 94, 3],
                ["2015-08-27 18:04:00", 97, 7],
                ["2015-08-27 18:04:17", 85, 8],
                ["2015-08-27 18:04:32", 90, 9],
                ["2015-08-27 18:05:02", 99, 8],
                ["2015-08-27 18:05:27", 89, 2],
                ["2015-08-27 18:05:49", 84, 5],
                ["2015-08-27 18:05:55", 76, 6],
                ["2015-08-27 18:06:30", 75, 7],
                ["2015-08-27 18:06:42", 87, 2],
                ["2015-08-27 18:07:51", 88, 1],
                ["2015-08-27 18:07:55", 81, 3],
                ["2015-08-27 18:09:20", 95, 10],
                ["2015-08-27 18:11:33", 77, 5],
                ["2015-08-27 19:15:10", 98, 6],
                ["2015-08-27 23:59:23", 80, 4],
                ["2015-08-28 01:32:33", 83, 6],
                ["2015-08-29 11:12:43", 71, 5],
                ["2015-08-29 14:26:53", 98, 3],
                ["2015-08-29 15:26:53", 98, 3],
                 ["2015-08-29 23:26:53", 98, 3],
                 ["2015-08-30 01:26:53", 98, 3],
                 ["2015-08-30 23:59:53", 98, 3],
                 ["2015-08-31 11:26:53", 98, 3]]

# B       business day frequency
# C       custom business day frequency (experimental)
# D       calendar day frequency
# W       weekly frequency
# M       month end frequency
# BM      business month end frequency
# CBM     custom business month end frequency
# MS      month start frequency
# BMS     business month start frequency
# CBMS    custom business month start frequency
# Q       quarter end frequency
# BQ      business quarter endfrequency
# QS      quarter start frequency
# BQS     business quarter start frequency
# A       year end frequency
# BA      business year end frequency
# AS      year start frequency
# BAS     business year start frequency
# BH      business hour frequency
# H       hourly frequency
# T       minutely frequency
# S       secondly frequency
# L       milliseonds
# U       microseconds
# N       nanoseconds


header = ["timestamp", "price", "volume"]


def resample_data(data, freq="1Min"):
        # now I create a dataframe
        df = pd.DataFrame(data=select_result, columns=header)

        # set the index
        df.index = pd.to_datetime(df["timestamp"])
        # check the dtype, It is <class 'pandas.tseries.index.DatetimeIndex'>
        print(type(df.index))

        # I still have the timestamp column in the data and it's type is <class 'pandas.core.series.Series'> so I remove it
        df = df[["price", "volume"]]

        # resampling price and volume will not work: price will result in a multiindex and volume in a simple index
        # so I need to create a multiindex for the volume and the concatenate price and volume
        # first lets resample the price
        price = (df.resample(freq, how={"price" : "ohlc"}, label={"right"})).fillna(method={"backfill"})

        # second, resample volume
        vol = (df.resample(freq, how={"volume" : 'sum'}, label={"right"})).fillna(method={"backfill"})

        # create a multiindex for volume
        vol.columns = pd.MultiIndex.from_tuples([('volume', 'sum')])

        # concatenate price and volume
        result = pd.concat([price, vol], axis=1)

        print(result)
        json_result = result.to_json()
        print(json_result)
if __name__ == "__main__":
    resample_data(select_result, "5Min")