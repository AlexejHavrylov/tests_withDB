#!/usr/bin/python
# -*- coding: utf-8 -*-
import getpass
import MySQLdb


class UsersData:
    'this class get users credentials and connect to defined DB'
    usersCount = 0

    def __init__(self):
        UsersData.usersCount += 1
        dbhost = raw_input(
            "please, enter db host and press \"Return/Enter\": ")
        dbuser = raw_input(
            "please, enter db user and press \"Return/Enter\": ")
#         dbpassword = getpass.getpass(
#             "please,enter password and press \"Return/Enter\": ")#doesn't work right at eclipse

        dbpassword = '1234'  # use real password when work at Eclipse
        # should be replaced before publishing
        dbname = self.dbname = raw_input(
            "please, enter db name and press \"Return/Enter\": ")

        db = MySQLdb.connect(
            host=dbhost, user=dbuser, passwd=dbpassword, db=dbname)
        cur = db.cursor()
        #
        # # Use all the SQL
        cur.execute("SELECT * FROM customers")
        #
        # # print all the first cell of all the rows
        for row in cur.fetchall():
            print row


newUser = UsersData()
