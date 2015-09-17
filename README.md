# Dataminer

## General random stuff
 * the miner has to create a new table for each market
 * each market has a list of symbols that it's/was trading at a certain time
 * a symbol can be terminated but it's history will not be lost
 * the database must have a way to archive information
 * the miner must never stop, and it has to reconnect if internet fails
 
## Desired features
1. each api will be started in it's own thread
2. each api will require the folowing:
..* a config, a name, description

## General structure

Assets are: Bitcoin, US dollar, Apple stock, etc. Each asset has a parity: Bitcoin vs USD, Apple vs USD, Ethereum vs Bitcoin
Markets are: Bitstamp, Poloniex, Nasdaq
A symbol has this name format: MARKET:ASSET. EX: BITSTAMP:BITCOIN or POLONIEX:ETHEREUM

## Database tables

1. Assets: id, short_name, long_name, parity, description
   Ex: 1, BTC, Bitcoin, USD, Bitcoin is a cryptocurency with value expressed in USD
   
2. sdfsdfsdfsdfsdf



