#!/usr/bin/python
# -*- coding: utf-8 -*-
import getpass
import MySQLdb
import random
from string import join


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
        self.db = MySQLdb.connect(
            self.dbhost, self.dbuser, self.dbpassword, self.dbname)
        db = self.db
        cursor = db.cursor()
        query = "SELECT " + self.id_column + " FROM " + self.table + ";"
        self.show_query(query)
        cursor.execute(query)
        rows = cursor.fetchall()
        random_row_id = random.choice(rows)[0]

        random_row_query = "SELECT * FROM " + self.table + \
            " WHERE " + self.id_column + " = " + str(random_row_id) + ";"
        self.show_query(random_row_query)
        cursor.execute(random_row_query)
        random_row = cursor.fetchall()
        column_names_query = "SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA ='" + \
            self.dbname + "' AND TABLE_NAME='" + self.table + "';"
        self.show_query(column_names_query)
        cursor.execute(column_names_query)
        row_2 = cursor.fetchall()
        # convert column name from tuple to list
        List_of_columns = []
        for row in row_2:
            List_of_columns.append(row[0])

        for line in List_of_columns:
            if line == self.id_column:
                # Removes column with id
                List_of_columns.remove(line)
                # convert List_of_column to strings for query:
        column_names = join(List_of_columns).replace(" ", ", ")
        insert_query = "INSERT INTO " + self.table + \
            "( " + column_names + ") SELECT " + column_names + " FROM " + self.table + " WHERE " + \
            self.id_column + " = " + str(random_row_id) + ";"
        self.show_query(insert_query)
        cursor.execute(insert_query)
        db.commit()
        self.select_all()

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

    def show_query(self, query):
        """
        Method displayed a SQL query on console.
        """
        print "Now executed SQL query:"
        print "\n" + query + "\n"

    def select_all(self, message="Checking a Data base..."):
        """
        method executes sql query SELECT * FROM customers
        """
        print "\n" + message + "\n"
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
