import mysql.connector
conn = mysql.connector.connect(host='localhost' , password='Siriana!06110' , user='root')

if conn.is_connected() : 
   print("Connection established...")