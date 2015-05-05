#!/usr/bin/python
'''
script executes SQL query DROP TABLE "customers"
'''
import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost", "newuser", "1234", "test")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = "CREATE TABLE  customers(row_number INT NOT NULL AUTO_INCREMENT, Customer VARCHAR(100) NOT NULL, Customer_ID VARCHAR(100),Date datetime, Comments  VARCHAR(100),PRIMARY KEY ( row_number ));"
cursor.execute(sql)
db.commit()
db.close()
