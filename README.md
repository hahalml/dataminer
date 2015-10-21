Dependencies:
autobahn (0.10.9)
mysql-connector-python (2.0.4)
prettytable (0.7.2)
pusherclient (0.3.0)
websocket-client (0.32.0)

General
This program uses api clients to connect and get ticker data from different bitcoin exchanges.
Data is stored in a mysql database and it is consumed by the tradingview financial charting library via http requests.

Data is collected at the smallest resolution possible. The bitstamp_client is using a pusher client,
poloniex_client a autobahn asyncio implementation.

Some resampling using pandas is done prior to serving the data to the tradingview library.

Most configuration are hard coded at the moment.

Anyone may use any piece of my code for any purpose.



