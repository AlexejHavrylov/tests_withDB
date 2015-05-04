#!/usr/bin/python
# -*- coding: utf-8 -*-
import getpass
import MySQLdb


class UsersData:
    'This class get users credentials and connect to defined DB'
    usersCount = 0

    def __init__(self):
        UsersData.usersCount += 1
        self.dbhost = raw_input(
            "please, enter db host and press \"Return/Enter\": ")
        self.dbuser = raw_input(
            "please, enter db user and press \"Return/Enter\": ")
        self.dbpassword = getpass.getpass(
            "please, enter password and press \"Return/Enter\": ")      # doesn't work right at eclipse
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
        query_1 = "CREATE TABLE  customers(row_number INT NOT NULL AUTO_INCREMENT, \
        Customer VARCHAR(100) NOT NULL, \
        Customer_ID VARCHAR(100),Date DATE,Comments  VARCHAR(100), \
        PRIMARY KEY ( row_number ));"
        cursor.execute(query_1)
        db.commit()
        print 'New table \'customers\' was created...'
        sql = "INSERT INTO customers(Customer, Customer_ID, Date, Comments)\
        VALUES ('customers1', 'CustomerID10', 'now-', 'Comment1'),\
        ('customers2', 'CustomerID11', '20140413', 'Comment2'),\
        ('customers3', 'CustomerID10', '20140414', 'Comment3'), \
        ('customers4', 'CustomerID11', '20140415', 'Comment4'), \
        ('customers5', 'CustomerID12', '20140415', 'Comment5');"
        try:
            cursor.execute(sql)
            db.commit()
            print 'Datas were added into table...'
        except:
            db.rollback()
#         db.close()
        self.select_all()

    def select_all(self):
        """
        method executes sql query SELECT * FROM customers
        """
        db = self.db
        cursor = db.cursor()
        query = "SELECT * FROM customers;"
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            print row
        db.close()


newUser = UsersData()
