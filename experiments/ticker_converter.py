from datetime import datetime
from pandas import date_range, Series
import numpy as np
import re
# Test data.
# Comments are expected result for 5m timeframe
select = [[1, "2015-08-27 17:53:20", 91, 2],
        # 17:55
        [2, "2015-08-27 17:59:11", 82, 5],
        [3, "2015-08-27 18:00:00", 96, 2],
        # 18:00
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

def get_timeframe(timeframe="1m"):
    # Timeframe:
    # 's', 'm', 'h', 'W', 'M', 'Y' stands for: seconds, minutes, hours, weeks, months, years
    # timeframe is a string of the form: <nr_periods><period>
    # example: '5s', '15m', '4h', '1W' etc
    # ! nr_periods must be an int number not a float, and period is a single letter, case matters
    # ! one month is 30 days, one year is 365 days

    number = re.findall(r'^\d+', timeframe)
    letter = re.findall(r'[smhdWMY]{1}', timeframe)
    # tf = re.match(r'^\d+([smhdWMY]){1}', timeframe)
    if len(number) == 1:
        nr_periods = int(number[0])
    else:
        print("Error: timeframe must contain exactly 1 single or multiple digits number")
    if len(letter) == 1:
        period = letter[0]
    else:
        print("Error: timeframe must contain exactly one letter in ['s','m','h','d', 'W','M','Y']")

    def nr_seconds(x):
        return {
            's' : 1,
            'm' : 60,
            'h' : 3600,
            'd' : 86400,
            'W' : 604800,
            'M' : 2592000,
            'Y' : 31536000,

        }.get(x, "Error")    # 9 is default if x not found
    tf = nr_periods * nr_seconds(period)
    return tf

def get_next_stop(timestamp, timeframe):
    # print("timestamp = {} {}, timeframe = {}".format(timestamp, datetime.fromtimestamp(timestamp), timeframe))
    stop = [datetime.fromtimestamp(i) for i in range(timestamp, timestamp + timeframe) if i % timeframe == 0]
    # print(int((min(stop)).timestamp()))
    return int((min(stop)).timestamp())
    # print(stop, datetime.fromtimestamp(min(stop)))

def resample_data(data, tf):
    # TODO improve validation end error handling Ex: 5m is correct but 5mm is not correct
    # TODO buggy on any timeframe where 60 % timeframe != 0 Ex: 7m, 45m
    # TODO also buggy on any timeframe larger than hours: d, W, M, Y
    # Note 1: this works well for seconds, 5m, 10m, 15m, 20m, 30m, 60m / 1h - 45m works but is not perfect
    # Note 2: until bugs are fixed use panda for data resampling
    # Note 3: use this for one way data compression
    # tf is a timeframe like '1m', '5m', '2h', '1d' etc
    # data is a list of lists or tuples
    # a data point is like this: [id, datetime, price, volume]
    current_date = datetime.strptime(data[0][1], "%Y-%m-%d %H:%M:%S")
    current_timestamp = int(current_date.timestamp())
    price = [data[0][2]]
    vol = data[0][3]
    timeframe = get_timeframe(tf)
    next_stop = get_next_stop(current_timestamp, timeframe)

    for i in range(1, len(data)):
        row = data[i]
        new_date = datetime.strptime(row[1], "%Y-%m-%d %H:%M:%S")
        new_timestamp = new_date.timestamp()
        new_price = row[2]
        new_vol = row[3]
        if new_timestamp <= next_stop:
            price.append(new_price)
            vol += new_vol
        else:
            open_price = price[0]
            high_price = max(price)
            low_price = min(price)
            close_price = price[-1]
            print("Date:{}, O:{}, H:{}, L:{}, C:{}, V:{}".format(datetime.fromtimestamp(next_stop),
                                                                 open_price, high_price, low_price, close_price, vol))
            next_stop = get_next_stop(int(new_timestamp), timeframe)
            price = [new_price]
            vol = new_vol
    # last item
    open_price = price[0]
    high_price = max(price)
    low_price = min(price)
    close_price = price[-1]
    print("Date:{}, O:{}, H:{}, L:{}, C:{}, V:{}".format(datetime.fromtimestamp(next_stop),
                                                         open_price, high_price, low_price, close_price, vol))


if __name__ == "__main__":
    # get_1_min(data)
    # x = datetime.strptime("2015-08-27 17:53:20", "%Y-%m-%d %H:%M:%S")
    # timestamp = int(x.timestamp())
    # timeframe = get_timeframe("5m")
    # get_next_stop(timestamp, timeframe)
    # resample_data(data, '5m')
    pass
