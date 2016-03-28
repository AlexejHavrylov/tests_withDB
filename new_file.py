# -*- coding: utf-8 -*-
import sqlalchemy
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey

print "Версия SQLAlchemy:", sqlalchemy.__version__
engine = sqlalchemy.create_engine('mysql://:root@localhost')

metadata = sqlalchemy.MetaData()
users_table = sqlalchemy.Table('users', metadata,
                    Column('id', Integer, primary_key=True),
                    Column('name', String),Column('fullname', String),Column('password', String))