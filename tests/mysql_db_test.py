__author__ = 'force'
import MySQLdb
# test data
data = [
        {"name" : "America/New_York", "description" : "America/New_York"},
        {"name" : "America/Los_Angeles", "description" : "America/Los_Angeles"},
        {"name" : "America/Chicago", "description" : "America/Chicago"},
        {"name" : "America/Toronto", "description" : "America/Toronto"},
        {"name" : "America/Vancouver", "description" : "America/Vancouver"},
        {"name" : "America/Argentina/Buenos_Aires", "description" : "America/Argentina/Buenos_Aires"},
        {"name" : "America/Bogota", "description" : "America/Bogota"},
        {"name" : "America/Sao_Paulo", "description" : "America/Sao_Paulo"},
        {"name" : "Europe/Moscow", "description" : "Europe/Moscow"},
        {"name" : "Europe/Athens", "description" : "Europe/Athens"},
        {"name" : "Europe/Berlin", "description" : "Europe/Berlin"},
        {"name" : "Europe/London", "description" : "Europe/London"},
        {"name" : "Europe/Madrid", "description" : "Europe/Madrid"},
        {"name" : "Europe/Paris", "description" : "Europe/Paris"},
        {"name" : "Europe/Warsaw", "description" : "Europe/Warsaw"},
        {"name" : "Australia/Sydney", "description" : "Australia/Sydney"},
        {"name" : "Asia/Bangkok", "description" : "Asia/Bangkok"},
        {"name" : "Asia/Tokyo", "description" : "Asia/Tokyo"},
        {"name" : "Asia/Taipei", "description" : "Asia/Taipei"},
        {"name" : "Asia/Singapore", "description" : "Asia/Singapore"},
        {"name" : "Asia/Shanghai", "description" : "Asia/Shanghai"},
        {"name" : "Asia/Seoul", "description" : "Asia/Seoul"},
        {"name" : "Asia/Kolkata", "description" : "Asia/Kolkata"},
        {"name" : "Asia/Hong_Kong", "description" : "Asia/Hong_Kong"}
    ]

# sql_multiple_insert = INSERT INTO `dataminer`.`symbol_status` (`id`, `name`, `description`) VALUES (NULL, 'trading', ''), (NULL, 'suspended', 'trading has been temporarily suspended for this symbol')


# create connection
conn = MySQLdb.connect (host = "localhost",
                           user = "root",
                           passwd = "7SwwJ3y8",
                           db = "dataminer")
# create cursor
curs = conn.cursor()

# execute an insert
table = "timezones"
for each in data:
    columns = each.keys()
    values = each.values()
    sql = "INSERT INTO {} ({}) VALUES ({})".format(table, ','.join(columns), ','.join(['%s'] * len(columns)))
    # Generates: INSERT INTO my_table (column1,column2) VALUES (%s,%s)
    curs.execute(sql, values)

# commit data to database
conn.commit()

# execute a select
curs.execute ("SELECT * FROM {}".format(table))
# get the data
rows = curs.fetchall ()

# print the data
for each in rows:
    print ("display results:", each)
# destroy cursor and close connection
curs.close ()
conn.close ()


