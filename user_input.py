#!/usr/bin/python
# -*- coding: utf-8 -*-
import getpass
import MySQLdb
import random
import datetime
from string import join


class UsersData:
    "This class get users credentials and connect to defined DB"

    def user_input_data(self):
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

    def connect_to_db(self):
        self.db = MySQLdb.connect(
            self.dbhost, self.dbuser, self.dbpassword, self.dbname)

    def find_id(self):
        self.connect_to_db()
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
        return random_row_id, random_row

    def get_column_names(self):
        self.connect_to_db()
        db = self.db
        cursor = db.cursor()
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
        return column_names

    def insert_value(self):
        self.connect_to_db()
        db = self.db
        cursor = db.cursor()
#       self.print_table(" Started...")
        column_names = self.get_column_names()
        random_row_id = self.find_id()[0]
        i = 0
        insert_query = "INSERT INTO " + self.table + \
            "( " + column_names + ") VALUES "
        while i < self.bulk_size:
            insert_query += "(" + self.get_values_with_replaced_dates() + ") ,"
            if (i == self.bulk_size - 1):
                insert_query = insert_query[:-1] + ";"
            i += 1
        self.show_query(insert_query)
        cursor.execute(insert_query)
        db.commit()
        db.close()

    def perform_task(self):
        """
        Method takes data  from randomly selected row 
        and added it to defined table.
        """
        try:
            i = 0
            while i < self.rows_to_add / self.bulk_size:
                print i
                self.insert_value()
                i += 1
        except:
            print "Can\'t get data from table \'" + self.table + "\'..."
        finally:
            self.print_table("Checking a Data base...")

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

    def print_table(self, message):
        """
        method executes sql query SELECT * FROM customers
        """
        self.connect_to_db()
        print message + "\n"
        db = self.db
        table = self.table
        cursor = db.cursor()
        select_query = "SELECT * FROM " + table + ";"
        cursor.execute(select_query)
        rows = cursor.fetchall()
        for row in rows:
            print row
        db.close()

    def get_columns_with_replaced_dates(self):
        self.connect_to_db()
        db = self.db
        cursor = db.cursor()
        column_names_query = "SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA ='" + \
            self.dbname + "' AND TABLE_NAME='" + self.table + "';"
        self.show_query(column_names_query)
        cursor.execute(column_names_query)
        row_2 = cursor.fetchall()
        # convert column name from tuple to list
        List_of_columns = []
        for row in row_2:
            List_of_columns.append(row[0])
        random_row = self.find_id()[1]

        List_of_values = []
        for line in random_row[0]:

            List_of_values.append(line)
        for i in range(0, len(List_of_values)):
            if(isinstance(List_of_values[i], datetime.datetime)):
                List_of_columns[i] = "now()"

        for line in List_of_columns:
            if line == self.id_column:
                # Removes column with id
                List_of_columns.remove(line)
                # convert List_of_column to strings for query:
        return join(List_of_columns).replace(" ", ", ")

    def get_values_with_replaced_dates(self):
        self.connect_to_db()
        db = self.db
        cursor = db.cursor()
        column_names_query = "SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA ='" + \
            self.dbname + "' AND TABLE_NAME='" + self.table + "';"
        self.show_query(column_names_query)
        cursor.execute(column_names_query)
        row_2 = cursor.fetchall()
        # convert column name from tuple to list
        List_of_columns = []
        for row in row_2:
            List_of_columns.append(row[0])
        random_row = self.find_id()[1]

        List_of_values = []
        for line in random_row[0]:

            List_of_values.append(line)
        i = 0
        while i < len(List_of_values):
            if(isinstance(List_of_values[i], str)):
                List_of_values[i] = "'" + List_of_values[i] + "'"

            elif(isinstance(List_of_values[i], datetime.datetime)):
                # change values of date columns
                List_of_values[i] = "now()"

            elif(List_of_columns[i] == self.id_column):
                del List_of_values[i]
                i = i - 1

            i += 1

        return join(List_of_values).replace(" ", ", ")


newUser = UsersData()
newUser.user_input_data()
newUser.perform_task()
