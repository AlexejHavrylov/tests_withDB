#!/usr/bin/python
# -*- coding: utf-8 -*-
import getpass
import MySQLdb


class UsersData:
    'This class get users credentials and connect to defined DB'

    def __init__(self):
        self.input_data()
        self.perform_task()
        self.show_input()

    def input_data(self):
        self.dbhost = raw_input(
            "please, enter db host and press \"Return/Enter\": ")
        self.dbuser = raw_input(
            "please, enter db user and press \"Return/Enter\": ")
        self.dbpassword = getpass.getpass(
            "please, enter password and press \"Return/Enter\": ")      # doesn't work right at eclipse
        self.dbname = self.dbname = raw_input(
            "please, enter db name and press \"Return/Enter\": ")
        self.table = raw_input(
            "please, enter table name and press \"Return/Enter\": ")
        self.rows_to_add = self.enter_number(
            "Please, enter number of rows to add: ")
        self.bulk_size = self.enter_number(
            "Please, enter bulk size of insert operation: ")
        self.id_column = raw_input("please, enter id column: ")

    def perform_task(self):
        self.db = MySQLdb.connect(
            self.dbhost, self.dbuser, self.dbpassword, self.dbname)
        db = self.db
        cursor = db.cursor()

    def show_input(self):
        print self.dbhost, self.dbpassword, self.dbuser, self.dbname, self.table, self.rows_to_add, self.id_column, self.bulk_size

    def enter_number(self, message):
        """
        Method takes user data and verifies the type('int' or 'str') of entered data.

        """
        i = 4
        while i > 0:
            try:
                entered_data = input(message)
                i = 0
            except NameError:
                print "You have to enter a number!"
                i -= 1
        return entered_data

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
