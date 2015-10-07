from autobahn.asyncio.wamp import ApplicationSession
from asyncio import coroutine
from autobahn.asyncio.wamp import ApplicationRunner
from datetime import datetime

class PoloniexComponent(ApplicationSession):
    url="wss://api.poloniex.com:443"
    feed="ticker"
    realm_name="realm1"


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
        runner = ApplicationRunner(self.url, self.realm_name)
        runner.run(PoloniexComponent)

def event_handler(event):
    # currencyPair, last, lowestAsk, highestBid, percentChange, baseVolume, quoteVolume, isFrozen, 24hrHigh, 24hrLow
    print(event)



if __name__ == '__main__':
    poloniex_api = PoloniexComponent()
    poloniex_api.start()


