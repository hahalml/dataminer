from autobahn.asyncio.wamp import ApplicationSession
from asyncio import coroutine
from autobahn.asyncio.wamp import ApplicationRunner
# from datetime import datetime
import configparser


class PoloniexComponent(ApplicationSession):
    url = "wss://api.poloniex.com:443"
    feed = "ticker"
    realm_name = "realm1"
    client_config = configparser.ConfigParser()
    try:
        client_config.read("config/poloniex_client.conf")
    except:
        print("##### ERROR: Config format is incorect! #####")

    def config_mapper(self, section):
        dict = {}
        options = self.client_config.options(section)
        for option in options:
            try:
                dict[option] = self.client_config.get(section, option)
                if dict[option] == -1:
                    print("skip: %s" % option)
            except:
                print("exception on %s!" % option)
                dict[option] = None
        return dict

    def onConnect(self):
        self.join(self.config.realm)


    @coroutine
    def onJoin(self, details):
        print("session started")

        def onEvent(*args):
            event = list(args)
            #event_handler(event)
            event_handler(event)

        try:
            yield from self.subscribe(onEvent, self.feed)
        except Exception as e:
            print("Could not subscribe to topic: {0}\n".format(self.feed), e)


    def start(self):
        # print(self.client_config.sections(), self.client_config.options("market"), self.client_config.get("market", "name",vars=list()))
        market_name = self.config_mapper("market")["name"]
        symbols = self.config_mapper("symbols")

        print(market_name, symbols)
        #runner = ApplicationRunner(self.url, self.realm_name)
        #runner.run(PoloniexComponent)

def event_handler(event):
    # currencyPair, last, lowestAsk, highestBid, percentChange, baseVolume, quoteVolume, isFrozen, 24hrHigh, 24hrLow
    print(event)



if __name__ == '__main__':
    poloniex_api = PoloniexComponent()
    poloniex_api.start()



