#!/usr/bin/python
# -*- coding: utf-8 -*-
import getpass
class UsersData:
   'this class get users credentials'
   usersCount = 0
   cred = []

   def __init__(self):
      UsersData.usersCount += 1
           
   def credentials(self):
       self.host = raw_input("please,enter db host and press \"Return/Enter\": ")
       host = self.host
       UsersData.cred.append(host)
        
       self.dbname = raw_input("please,enter db name and press \"Return/Enter\": ")
       name = self.dbname
       UsersData.cred.append(name)

       self.dbpassword=getpass.getpass("please,enter Database password and press \"Return/Enter\": ")
       password = self.dbpassword
       UsersData.cred.append(password)
       cred=UsersData.cred
       for data in cred:
           print data
newUser=UsersData()
newUser.credentials() 

     