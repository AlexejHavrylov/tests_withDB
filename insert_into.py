#!/usr/bin/python
'''
script executes SQL query INSERT_INTO in table "customers' 
'''
import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","newuser","1234","test" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = """INSERT INTO customers (row_number, Customer, Customer_ID, Date,Comments)
VALUES (1, 'Customer1', '0001','2010-04-11','good customer');"""
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

# disconnect from server
db.close()