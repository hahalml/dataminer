##Dependencies:
1. autobahn (0.10.9)
* pip install autobahn[asyncio]

2. mysql-connector-python (2.0.4)
* pip install mysql-connector-python --allow-external mysql-connector-python

3. prettytable (0.7.2)
* pip install prettytable

4. pusherclient (0.3.0)
* git clone https://github.com/razvanmateid/PythonPusherClient.git
* cd PythonPusherClient
* python setup.py install

5. Flask
* pip install Flask

6. Flask-restful
* pip install flask-restful

General
This program uses api clients to connect and get ticker data from different bitcoin exchanges.
Data is stored in a mysql database and it is consumed by the tradingview financial charting library via http requests.

Data is collected at the smallest resolution possible. The bitstamp_client is using a pusher client,
poloniex_client a autobahn asyncio implementation.

Some resampling using pandas is done prior to serving the data to the tradingview library.

Most configuration are hard coded at the moment.

Licence: Anyone may use any of my code for any purpose.



