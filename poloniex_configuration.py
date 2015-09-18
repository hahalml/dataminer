__author__ = 'force'
import manager
config = {
    "market" : {"short_name" : "poloniex",
                "name" : "poloniex",
                "description" : "US-based cryptocurrency exchange",
                "url" : "https://www.poloniex.com",
                "api_url" : "https://www.poloniex.com/support/api"
                },
    "symbol" : [
                {
                "asset_id_1" : 1,
                "asset_id_2" : 2,
                "name" : "",
                "description" : "",
                "market_id" : 1,
                "timezone" : 10,
                "pricescale" : 0.0001,
                "minmov" : 0.000001,
                "fractional" : False,
                "session" : "24x7",
                "has_intraday" : True,
                "intraday_multipliers" : [1],
                "has_daily" : False,
                "has_weekly" : False,
                "has_weekend_and_monthly": False,
                "has_empty_bars" : False,
                "force_session_rebuild" : False,
                "has_no_volume" : False,
                "volume_precision" : 2,
                "expired" : False,
                "symbol_status_id" : 2
                }
                ]
}
x = manager.Manager()
x.get_tables()