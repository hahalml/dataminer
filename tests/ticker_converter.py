from datetime import datetime
from pandas import date_range, Series
import re
data = [[1, "2015-08-27 17:53:20", 91, 2],
        [2, "2015-08-27 17:59:11", 82, 5],
        [3, "2015-08-27 18:00:00", 96, 2],
        [4, "2015-08-27 18:00:11", 92, 1],
        [5, "2015-08-27 18:01:23", 79, 1],
        [6, "2015-08-27 18:01:40", 86, 10],
        [7, "2015-08-27 18:02:20", 78, 4],
        [8, "2015-08-27 18:03:59", 94, 3],
        [9, "2015-08-27 18:04:00", 97, 7],
        [10, "2015-08-27 18:04:17", 85, 8],
        [11, "2015-08-27 18:04:32", 90, 9],
        [12, "2015-08-27 18:05:02", 99, 8],
        [13, "2015-08-27 18:05:27", 89, 2],
        [14, "2015-08-27 18:05:49", 84, 5],
        [15, "2015-08-27 18:05:55", 76, 6],
        [16, "2015-08-27 18:06:30", 75, 7],
        [17, "2015-08-27 18:06:42", 87, 2],
        [18, "2015-08-27 18:07:51", 88, 1],
        [19, "2015-08-27 18:07:55", 81, 3],
        [20, "2015-08-27 18:09:20", 95, 10],
        [21, "2015-08-27 18:11:33", 77, 5],
        [22, "2015-08-27 19:15:10", 98, 6],
        [23, "2015-08-27 23:59:23", 80, 4],
        [24, "2015-08-28 01:32:33", 83, 6],
        [25, "2015-08-29 11:12:43", 71, 5],
        [26, "2015-08-29 11:26:53", 98, 3]]

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

def get_timeframe(timeframe="1m"):
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
    print("timestamp = {}, timeframe = {}".format(timestamp, timeframe))
    stop = [datetime.fromtimestamp(i) for i in range(timestamp, timestamp + 3 * timeframe) if i % timeframe == 0]
    print(stop)
    print(min(stop))
    # print(stop, datetime.fromtimestamp(min(stop)))


if __name__ == "__main__":
    # get_1_min(data)
    # resample_shit(data)
    x = datetime.strptime("2015-08-27 18:58:32", "%Y-%m-%d %H:%M:%S")
    timestamp = int(x.timestamp())
    timeframe = get_timeframe("1W")
    get_next_stop(timestamp, timeframe)
