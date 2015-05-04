#!/usr/bin/python
# -*- coding: utf-8 -*-
import getpass
import MySQLdb
import random


class UsersData:
    'This class get users credentials and connect to defined DB'

    def input_data(self, dbhost, dbuser, dbpassword, dbname, table, rows_to_add, bulk_size, id_column):
        self.dbhost = dbhost
        self.dbuser = dbuser
        self.dbpassword = dbpassword
        self.dbname = dbname
        self.table = table
        self.rows_to_add = rows_to_add
        self.bulk_size = bulk_size
        self.id_column = id_column

    def visual_input_data(self):
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
        db = MySQLdb.connect(
            self.dbhost, self.dbuser, self.dbpassword, self.dbname)
        cursor = db.cursor()
        query = "SELECT " + self.id_column + " FROM " + self.table + ";"
        cursor.execute(query)
        rows = cursor.fetchall()
        random_row_id = random.choice(rows)[0]
        print random_row_id
        random_row_query = "SELECT * FROM " + self.table + \
            " WHERE " + self.id_column + " = " + str(random_row_id) + ";"
        cursor.execute(random_row_query)
        row = cursor.fetchall()
        print row
        db.close()

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
        table = self.table
        cursor = db.cursor()

        query = "SELECT * FROM " + table + ";"
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            print row
        db.close()


newUser = UsersData()
# newUser.visual_input_data()
newUser.input_data(
    "localhost", "newuser", "1234", "test", "customers", 12, 4, "row_number")
newUser.perform_task()
newUser.show_input()
