import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password ='qwerty'
)

# Prepare a cursor object

cursorObject = dataBase.cursor()

# create a database

cursorObject.execute('CREATE DATABASE loic1')

print('well done')

# This file was just a test to test how data base work
