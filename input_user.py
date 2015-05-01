#!/usr/bin/python
# -*- coding: utf-8 -*-
import getpass
import MySQLdb


class UsersData:
    'this class get users credentials and connect to defined DB'
    usersCount = 0

    def __init__(self):
        UsersData.usersCount += 1

        self.host = raw_input(
            "please, enter db host and press \"Return/Enter\": ")
        self.dbuser = raw_input(
            "please, enter login and press \"Return/Enter\": ")

        self.dbpassword = getpass.getpass(
            "please,enter Database password and press \"Return/Enter\": ")
        self.dbname = raw_input(
            "please, enter db name and press \"Return/Enter\": ")

        host = self.host
        user = self.dbuser
        password = self.dbpassword
        name = self.dbname

        print host, user, name, password
        db = MySQLdb.connect(host, user, password, name)
        cur = db.cursor()
        #
        # # Use all the SQL
        cur.execute("SELECT * FROM customers")
        #
        # # print all the first cell of all the rows
        for row in cur.fetchall():
            print row


newUser = UsersData()
newUser.dbconnect()
