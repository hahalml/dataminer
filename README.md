# Dataminer

## General random stuff
 * the miner has to create a new table for each market
 * each market has a list of symbols that it's/was trading at a certain time
 * a symbol can be terminated but it's history will not be lost
 * the database must have a way to archive information
 * the miner must never stop, and it has to reconnect if internet fails
 * likeley tables for database: markets [id, name, description, symbol_id]
## Desired features
1. each api will be started in it's own thread
2. each api will require the folowing:
..* a name, description


