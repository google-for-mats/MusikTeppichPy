import mysql.connector
from mysql.connector import Error

def selectSpielzeit():
    

try:
    connection = mysql.connector.connect(host='localhost', 
                                         database='aktiv_radio',
                                         user='root',
                                         password='123MySql')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select * from datei;")
        record = cursor.fetchall()
        print("Your're cnnected to database: ", record)

except Error as e:
    print("Error while connecting to Database", e)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")