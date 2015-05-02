#!/usr/bin/python
# -*- coding: utf-8 -*-
import getpass
import MySQLdb


class UsersData:
    'this class get users credentials and connect to defined DB'
    usersCount = 0

    def __init__(self):
        UsersData.usersCount += 1
        self.dbhost = raw_input(
            "please, enter db host and press \"Return/Enter\": ")
        self.dbuser = raw_input(
            "please, enter db user and press \"Return/Enter\": ")
        self.dbpassword = getpass.getpass(
            "please, enter password and press \"Return/Enter\": ")      # doesn't work right at eclipse

        # use real password when work at Eclipse

        self.dbname = self.dbname = raw_input(
            "please, enter db name and press \"Return/Enter\": ")
        dbhost = self.dbhost
        dbuser = self.dbuser
        dbpassword = self.dbpassword
        dbname = self.dbname
        self.db = MySQLdb.connect(dbhost, dbuser, dbpassword, dbname)
        db = self.db
        cursor = db.cursor()
        cursor.execute("DROP TABLE IF EXISTS customers")
        query_1 = "CREATE TABLE customers(row_number INT NOT NULL AUTO_INCREMENT, Customer VARCHAR(100) NOT NULL, Customer_ID INT , Date DATE, Comments  VARCHAR(100),PRIMARY KEY ( row_number ));"
        cursor.execute(query_1)
        query_2 = "INSERT INTO customers (row_number, Customer, Customer_ID, Date,Comments) VALUES (1, 'Customer1', '1','2010-01-11','good customer');"
        cursor.execute(query_2)
        self.select_all()

    def select_all(self):
        """
        method executes sql query SELECT * FROM customers
        """
        db = self.db
        cursor = db.cursor()
        query_3 = "SELECT * FROM customers;"
        cursor.execute(query_3)
        rows = cursor.fetchall()
        for row in rows:
            print row
        db.close()

newUser = UsersData()
# newUser.insert_into(3)
