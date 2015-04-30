#!/usr/bin/python
# -*- coding: utf-8 -*-
import getpass
class UsersData:
   'this class get users credentials'
   usersCount = 0
   cred=[]

   def __init__(self):
      UsersData.usersCount += 1
           
   def credentials(self):
       self.host=raw_input("please,enter Database host and press \"Return/Enter\": ")
       host = self.host
       print host
       self.dbname=raw_input("please,enter Database name and press \"Return/Enter\": ")
       dbname = self.dbname
       print dbname
#        self.dbpassword=raw_input("please,enter Database password and press \"Return/Enter\": ")
       self.dbpassword=getpass.getpass("please,enter Database password and press \"Return/Enter\": ")
       dbpassword = self.dbpassword
       print dbpassword
newUser=UsersData()
newUser.credentials() 

     