import pandas as pd

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
                ["2015-08-29 11:26:53", 98, 3]]

header = ["timestamp", "price", "volume"]

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
price = df.resample('6h', how={"price" : "ohlc"})

# second, resample volume
vol = df.resample('6h', how={"volume" : 'sum'})

# create a multiindex for volume
vol.columns = pd.MultiIndex.from_tuples([('volume', 'sum')])

# concatenate price and volume
result = pd.concat([price, vol], axis=1)

print(result)