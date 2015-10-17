# https://github.com/ekulyk/PythonPusherClient.git
import sys
sys.path.append('..')
import datetime
import pusherclient

# Add a logging handler so we can see the raw communication data
import logging
#root = logging.getLogger()
#root.setLevel(logging.INFO)
#ch = logging.StreamHandler(sys.stdout)
#root.addHandler(ch)

global pusher


def channel_callback(data):
    now = datetime.datetime.now()
    print(now, now.timestamp(), data)


def connect_handler(data):
    channel = pusher.subscribe("live_trades")
    # channel1 = pusher.subscribe("order_book")

    channel.bind('trade', channel_callback)
    # channel1.bind('data', channel_callback)

if __name__ == '__main__':
    appkey = 'de504dc5763aeef9ff52'

    pusher = pusherclient.Pusher(appkey)

    pusher.connection.bind('pusher:connection_established', connect_handler)
    pusher.connect()

    while True:
        pass
