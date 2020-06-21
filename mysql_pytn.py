import os
import datetime
import pymysql

# Get username from Cloud9 workspace
# (modify this variable if running on another environment)
username = os.getenv('C9_USER')

# Connect to the database
# dat is my connection obj to connect to the database using the pymysql connect method
connection = pymysql.connect(host='localhost',
                             user=username,
                             password='',
                             db='Chinook')

try:
    # Run a query
    with connection.cursor(pymysql.cursors.DictCursor) as cursor: # the (pymsql.cursors.DictCursor) is to return the result of the cursr as dict
        sql = "SELECT * FROM Artist;"
        cursor.execute(sql)
        #result = cursor.fetchall()  # fetchall() is getting the data back
        for row in cursor:
            print(row)
 
finally:
    # Close the connection, regardless of whether or not the above was successful
    connection.close()

