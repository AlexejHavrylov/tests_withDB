'''
Script executes the following operations:
create table
if already created -> drop and create it again
afterwards insert test values.
'''
import MySQLdb


def create_table(db):
    cursor = db.cursor()
    sql = ("CREATE TABLE customers(row_number INT NOT NULL AUTO_INCREMENT, "
           "Customer VARCHAR(100) NOT NULL, Customer_ID VARCHAR(100),"
           "Date datetime, Comments  VARCHAR(100),PRIMARY KEY ( row_number ));")
    cursor.execute(sql)


def drop_table(db):

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Prepare SQL query to INSERT a record into the database.
    sql = "DROP TABLE customers;"
    cursor.execute(sql)


def insert_values(db):
    cursor = db.cursor()
    insert_query = "INSERT INTO customers (row_number, Customer, Customer_ID, Date,Comments) VALUES (1, 'Customer1', 'CustomerID1','20150312','Comment1');INSERT INTO customers (row_number, Customer, Customer_ID, Date,Comments) VALUES (2, 'Customer2', 'CustomerID2','20140412','Comment2');INSERT INTO customers (row_number, Customer, Customer_ID, Date,Comments) VALUES (3, 'Customer3', 'CustomerID3','20140211','Comment3');"
    cursor.execute(insert_query)

db = MySQLdb.connect("localhost", "root", "1234", "MyDB_1")
db.autocommit(True)

try:
    create_table(db)
except:
    drop_table(db)
    create_table(db)
    insert_values(db)
finally:
    db.close
