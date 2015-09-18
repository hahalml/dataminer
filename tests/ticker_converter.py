from datetime import datetime
from random import randint
import random
import pandas
from pandas import date_range, Series

data = [[1, "2015-08-27 11:27:23", 91, 2],
        [2, "2015-08-27 11:27:33", 82, 5],
        [3, "2015-08-27 11:27:43", 96, 2],
        [4, "2015-08-27 11:27:53", 92, 1],
        [5, "2015-08-27 11:28:23", 79, 1],
        [6, "2015-08-27 11:28:33", 86, 10],
        [7, "2015-08-27 11:28:43", 78, 4],
        [8, "2015-08-27 11:28:53", 94, 3],
        [9, "2015-08-27 11:29:23", 97, 7],
        [10, "2015-08-27 11:29:33", 85, 8],
        [11, "2015-08-27 11:29:43", 90, 9],
        [12, "2015-08-27 11:29:53", 99, 8],
        [13, "2015-08-27 11:30:23", 89, 2],
        [14, "2015-08-27 11:30:33", 84, 5],
        [15, "2015-08-27 11:30:43", 76, 6],
        [16, "2015-08-27 11:31:13", 75, 7],
        [17, "2015-08-27 11:31:23", 87, 2],
        [18, "2015-08-27 11:31:33", 88, 1],
        [19, "2015-08-27 11:31:43", 81, 3],
        [20, "2015-08-27 11:31:53", 95, 10],
        [21, "2015-08-27 11:31:53", 77, 5],
        [22, "2015-08-27 11:32:13", 98, 6],
        [23, "2015-08-27 11:32:23", 80, 4],
        [24, "2015-08-27 11:32:33", 83, 6],
        [25, "2015-08-27 11:32:43", 71, 5],
        [26, "2015-08-27 11:32:53", 98, 3]]
x = datetime.strptime("2015-08-27 11:29:00", "%Y-%m-%d %H:%M:%S")
#print("Example date: {}".format(x))
timestamp = x.timestamp()
print(timestamp, "mod:", timestamp % 5)

def get_1_min(data):
    price = [data[0][2]]
    vol = data[0][3]
    current_minute = (datetime.strptime(data[0][1], "%Y-%m-%d %H:%M:%S")).minute
    # print("First minute = {}".format(current_minute))
    # current_minute = date.minute

    for i in range(1, len(data)):
        row = data[i]
        date_and_time = datetime.strptime(row[1], "%Y-%m-%d %H:%M:%S")
        new_minute = date_and_time.minute
        new_volume = row[3]
        if new_minute > current_minute:
            o = price[0]
            h = max(price)
            l = min(price)
            c = price[-1]
            #print("price", price)
            print(o, h, l, c, vol)
            price = [row[2]]
            vol = new_volume
            current_minute = new_minute
        else:
            price.append(row[2])
            vol = vol + new_volume
    o = price[0]
    h = max(price)
    l = min(price)
    c = price[-1]
    #print("price", price)
    print(o, h, l, c, vol)

def resample_shit(data):
    print("Starting")
    rng = date_range('1/1/2012', periods=100, freq='T')
    ts = Series(1, index=rng)
    #print(ts)
    print(ts.resample('15Min', how='sum'))


if __name__ == "__main__":
    #get_1_min(data)
    resample_shit(data)
