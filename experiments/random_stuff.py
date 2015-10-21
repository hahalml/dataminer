__author__ = 'force'
import mysql.connector
from mysql.connector import errorcode

table = "test_table"

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


try:
    conn = mysql.connector.connect (host = "localhost",
                               user = "dataminer",
                               passwd = "asd",
                               db = "dataminer")
    curs = conn.cursor()
    print("Connected")
except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Incorrect user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)

for each in data:
    columns = each.keys()
    values = tuple(each.values())
    sql = "INSERT INTO {} ({}) VALUES ({})".format(table, ','.join(columns), ','.join(['%s'] * len(columns)))
    # Generates: INSERT INTO my_table (column1,column2) VALUES (%s,%s)
    try:
        curs.execute(sql, values)
        conn.commit()
    except mysql.connector.Error as err:
        print("NU BUJE INSERTU %s" % (err))

# commit data to database


# execute a select
try:
    curs.execute ("SELECT * FROM {}".format(table))
    # get the data
    rows = curs.fetchall ()

    # print the data
    for each in rows:
        print ("display results:", each)
    # destroy cursor and close connection
    curs.close ()
    conn.close ()
except mysql.connector.Error as err:
    print("NU BUJE SELECTU %s" % (err))
