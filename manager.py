__author__ = 'force'
import mysql.connector
from mysql.connector import errorcode
from prettytable import PrettyTable

class Manager:
    def __init__(self, host="localhost", database="dataminer", user="root", password="7SwwJ3y8"):
        self.database = database
        try:
            self.connection = mysql.connector.connect (host = host,
                               user = user,
                               passwd = password,
                               db = database)
            self.cursor = self.connection.cursor(buffered=True)
            print("\nConnected")
        except mysql.connector.Error as err:
                    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                        print("Incorrect user name or password")
                    elif err.errno == errorcode.ER_BAD_DB_ERROR:
                        print("Database does not exist")
                    else:
                        print(err)

    def get_tables(self):
        # getting all the tables names
        self.cursor.execute("USE {}".format(self.database))  # select the database
        self.cursor.execute("SHOW TABLES")
        tables = self.cursor.fetchall()
        beautiful_table = PrettyTable(["Table Name"])
        print("\nTABLES IN {}:".format(self.database.upper()))
        for each in tables:
            beautiful_table.add_row(each)
        # print data in a nice table
        print(beautiful_table)

    def get_table_content(self, table):
        # get contents af a table
        self.cursor.execute ("SELECT * FROM {}".format(table))
        # get the data
        rows = self.cursor.fetchall()
        # get the column_names to use as a header for the table
        header = list(self.cursor.column_names)
        # create the prettytable
        beautiful_table = PrettyTable(header)
        # print the data in a for
        print("\nDATA IN TABLE '{}'".format(table.upper()))
        for each in rows:
            beautiful_table.add_row(each)
        # print data in a nice table
        print(beautiful_table)

    def get_data_by_id(self, table, id):
        try:
            self.cursor.execute("SELECT * FROM {} WHERE id={}".format(table, id))
            row = self.cursor.fetchall()
            return row
        except mysql.connector.errorcode as err:
            print(err)

    def add_data(self, table, data):
        # data must come as a list of lists/tuples:
        # [["val1_col1", "val1_col2"],
        #  ["val2_col1", "val2_col2"],
        #  ["val3_col1", "val3_col2"]]

        # get the table header
        self.cursor.execute("SELECT * FROM {}".format(table))
        columns_names = list(self.cursor.column_names)
        columns = tuple(columns_names[1:])
        for each in data:
            values = tuple(each)
            sql = "INSERT INTO {} ({}) VALUES ({})".format(table, ','.join(columns), ','.join(['%s'] * len(columns)))
            # Generates: INSERT INTO my_table (column1,column2) VALUES (%s,%s)
            self.cursor.execute(sql, values)
        # commit data to database
        self.connection.commit()

    def delete_data_by_id(self, table, id):
        try:
            self.cursor.execute("DELETE FROM {} WHERE id={}".format(table, id))
            print("\nDELETED id = {} FROM TABLE {}".format(id, table))
            return True
        except mysql.connector.errorcode as err:
            print(err)
            return False

    def edit_data_by_id(self, table, columns, values, mark):
        # table >> string
        # columns >> tuple containing the columns to update
        # mark >> a tuple (column_name, value) by which to search in the table
        # values >> data to insert into columns
        # self.cursor.execute ("UPDATE tblTableName SET Year=%s, Month=%s, Day=%s, Hour=%s, Minute=%sWHERE Server=%s", (Year, Month, Day, Hour, Minute, ServerID))
        sql = "UPDATE {} SET {} WHERE {}={}".format(table, '=%,'.join(columns)+"=%", mark[0], mark[1])
        try:
            self.cursor.execute(sql, values)
        except:
            print("error updating")

    def __del__(self):
        self.connection.close()
        print("\nConnection closed")

if __name__ == "__main__":
    manager = Manager()
    manager.get_tables()
    test_table = "test_table"
    test_data = [("val1_col1", "val1_col2"),
                 ["val2_col1", "val2_col2"],
                 ("val3_col1", "val3_col2")]
    columns = ("col1", "col2", "col3")
    values = ("val1", "val2", "val3")
    #manager.add_data(table="test_table", data=test_data)
    #manager.delete_data_by_id(table=test_table, id=1)
    manager.edit_data_by_id(table=test_table, mark=("cacat","pisat"), columns=columns, values=values)
    manager.get_table_content("test_table")
    #manager.get_data_by_id(table=test_table, id=2)
