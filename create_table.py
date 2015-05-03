#!/usr/bin/python

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost", "root", "Amadeus1970", "test")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Drop table if it already exist using execute() method.
cursor.execute("DROP TABLE IF EXISTS customers")

# Create table as per requirement
sql = "CREATE TABLE  customers(row_number INT NOT NULL AUTO_INCREMENT, Customer VARCHAR(100) NOT NULL, Customer_ID VARCHAR(100), Date datetime, Comments  VARCHAR(100), PRIMARY KEY ( row_number ));"

cursor.execute(sql)

# disconnect from server
db.close()
