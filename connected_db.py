#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 29 ���. 2015

@author: Oleksii
'''

 
import MySQLdb

db = MySQLdb.connect(host="localhost", # your host, usually localhost
                     user="newuser", # your username
                      passwd="1234", # your password
                      db="test") # name of the data base

# create a Cursor object. It will let
# Cursor executes all the queries you want
cur = db.cursor() 

# Use all the SQL 
cur.execute("SELECT * FROM customers")

# print all the first cell of all the rows
for row in cur.fetchall() :
    print row[0] 
    
    