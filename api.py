from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
import json

app = Flask(__name__)
api = Api(app)

#
# DATA = {
#     'ID1': {'data1': 'data pentru data 1'},
#     'ID2': {'data2': 'data pentru data 2'},
#     'ID3': {'data3': 'data pentru data 3'},
# }
#
#
# def abort_if_id_doesnt_exist(id):
#     if id not in DATA:
#         abort(404, message="DATA {} doesn't exist".format(id))


# DataList
# shows a list of all data


class Example(Resource):
    def get(self):
        # Add parameters
        parser = reqparse.RequestParser()
        parser.add_argument('key1', type=str)
        parser.add_argument('key2', type=str)
        parser.add_argument('key3', type=str)
        params = parser.parse_args()
        return params


class Config(Resource):
    """ Will return Configuration """
    # GET /config
    def get(self):
        response_obj = {
                        "supports_search": True,
                        "supports_group_request": False,
                        "supported_resolutions": ["1", "5", "15", "30", "60", "1D", "1W", "1M"],
                        "supports_marks": False}
        response_json = (json.dumps(response_obj, ensure_ascii=False))
        response = Flask.response_class(response=response_json)
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET')

        return response


class Symbol_info(Resource):
    # GET /symbol_info?group=<group_name>
    def get(self):
        # Add parameters
        parser = reqparse.RequestParser()
        parser.add_argument('group', type=str)
        # get parameters
        params = parser.parse_args()
        response_obj = {
                        "symbol": ["AA", "BTCUSD", "SPX"],
                        "description": ["Apple Inc", "Microsoft corp", "S&P 500 index"],
                        "exchange-listed": "NYSE",
                        "exchange-traded": "NYSE",
                        "minmov": 1,
                        "minmov2": 0,
                        "pricescale": [1, 1, 100],
                        "has-dwm": True,
                        "has-intraday": True,
                        "has-no-volume": [False, False, True],
                        "type": ["stock", "stock", "index"],
                        "ticker": ["AA", "BTCUSD", "SPX"],
                        "timezone": "America/New_York",
                        "session-regular": "0900-1600"}
        response_json = (json.dumps(response_obj, ensure_ascii=False))
        response = Flask.response_class(response=response_json)
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET')
        return response


class Symbols(Resource):
    # GET /symbols?symbol=<symbol>
    def get(self):
        # Add parameters
        parser = reqparse.RequestParser()
        parser.add_argument('symbol', type=str)
        # get parameters
        params = parser.parse_args()
        response_obj = {
                        "symbol": ["BTCUSD"],
                        "description": ["Bitcoin USD Bitstamp"],
                        "exchange-listed": "Bitstamp",
                        "exchange-traded": "Bitstamp",
                        "minmov": 1,
                        "minmov2": 0,
                        "pricescale": [1],
                        "has-dwm": True,
                        "has-intraday": True,
                        "has-no-volume": [False],
                        "type": ["stock"],
                        "ticker": ["BTCUSD"],
                        "timezone": "America/New_York",
                        "session-regular": "0900-1600"}
        response_json = (json.dumps(response_obj, ensure_ascii=False))
        response = Flask.response_class(response=response_json)
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET')
        return response



class Search(Resource):
    # GET /search?query=<query>&type=<type>&exchange=<exchange>&limit=<limit>
    def get(self):
        # Add parameters
        parser = reqparse.RequestParser()
        parser.add_argument('query', type=str)
        parser.add_argument('type', type=str)
        parser.add_argument('exchange', type=str)
        parser.add_argument('limit', type=int)
        # get parameters
        params = parser.parse_args()
        response_obj = [
                {
                "symbol": "AA",
                "full_name": "Bitcoin USD",
                "description": "Bitcoin desc",
                "exchange": "Bitstamp",
                "ticker": "",
                "type": "bitcoin"},
            {
                "symbol": "BTCUSD",
                "full_name": "Bitcoin USD",
                "description": "Bitcoin desc",
                "exchange": "Bitstamp",
                "ticker": "BTCUSD",
                "type": "bitcoin"},
            {
                "symbol": "SPX",
                "full_name": "Bitcoin USD",
                "description": "Bitcoin desc",
                "exchange": "Bitstamp",
                "ticker": "",
                "type": "bitcoin"}
            ]
        response_json = (json.dumps(response_obj, ensure_ascii=False))
        response = Flask.response_class(response=response_json)
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET')
        return response


class History(Resource):
    # GET /history?symbol=<ticker_name>&from=<unix_timestamp>&to=<unix_timestamp>&resolution=<resolution>
    def get(self):
        # Add parameters
        parser = reqparse.RequestParser()
        parser.add_argument('symbol', type=str)
        parser.add_argument('from', type=int)
        parser.add_argument('to', type=int)
        parser.add_argument('resolution', type=str)
        # get parameters
        params = parser.parse_args()
        response_obj = {
                        "s": "ok",
                        "t": [1386493512, 1386493572, 1386493632, 1386493692],
                        "c": [42.1, 43.4, 44.3, 42.8]
                        }
        response_json = (json.dumps(response_obj, ensure_ascii=False))
        response = Flask.response_class(response=response_json)
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET')
        return response


class Marks(Resource):
    # GET /marks?symbol=<ticker_name>&from=<unix_timestamp>&to=<unix_timestamp>&resolution=<resolution>
    def get(self):
        # Add parameters
        parser = reqparse.RequestParser()
        parser.add_argument('symbol', type=str)
        parser.add_argument('from', type=int)
        parser.add_argument('to', type=int)
        parser.add_argument('resolution', type=str)
        # get parameters
        params = parser.parse_args()
        return "marks {}".format(params)


class Quotes(Resource):
    # GET /quotes?symbols=<ticker_name_1>,<ticker_name_2>,...,<ticker_name_n>
    # Example: GET /quotes?symbols=NYSE%3AAA%2CNYSE%3AF%2CNasdaqNM%3AAAPL
    def get(self):
        # Add parameters
        parser = reqparse.RequestParser()
        parser.add_argument('symbols', type=str)
        # get parameters
        params = parser.parse_args()
        return "quotes {}".format(params)
##
## Actually setup the Api resource routing here
##
api.add_resource(Example, '/example')
api.add_resource(Config, '/config')
api.add_resource(Symbol_info, '/symbol_info')
api.add_resource(Symbols, '/symbols')
api.add_resource(Search, '/search')
api.add_resource(History, '/history')
api.add_resource(Marks, '/marks')
api.add_resource(Quotes, '/quotes')


if __name__ == '__main__':
    app.run(debug=True)
