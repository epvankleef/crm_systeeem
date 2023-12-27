import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '',
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE crm_systeem")

print("All done")