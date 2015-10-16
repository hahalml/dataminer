# https://github.com/ekulyk/PythonPusherClient.git
import sys
sys.path.append('..')
import time
import datetime
import pusherclient

# Add a logging handler so we can see the raw communication data
import logging
#root = logging.getLogger()
#root.setLevel(logging.INFO)
#ch = logging.StreamHandler(sys.stdout)
#root.addHandler(ch)

global pusher

def print_usage(filename):
    print("Usage: python %s <appkey>" % filename)

    print ("ASDASDASDASDASDASD")

def channel_callback(data):
    now = datetime.datetime.now()
    print(now, now.timestamp(), data)


def connect_handler(data):
    # cryptsy channel
    # channel = pusher.subscribe("trade.3")
    # bitstamp channel
    channel = pusher.subscribe("live_trades")
    channel1 = pusher.subscribe("order_book")

    # cryptsy event
    # channel.bind('my_event', channel_callback)
    # bitstamp event
    channel.bind('trade', channel_callback)
    channel1.bind('data', channel_callback)

if __name__ == '__main__':
    # cryptsy appkey
    # appkey = 'cb65d0a7a72cd94adf1f'
    # bitstamp appkey
    appkey = 'de504dc5763aeef9ff52'

    pusher = pusherclient.Pusher(appkey)

    pusher.connection.bind('pusher:connection_established', connect_handler)
    pusher.connect()

    while True:
        pass
