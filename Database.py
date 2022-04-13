import mysql.connector
from mysql.connector import Error
#from fillArrayTest import *

class Database:


    mydb = mysql.connector.connect(
    host="192.168.178.154",
    user="radioaktiv",
    password="8877AktivRadio!8877",
    database="aktiv_radio",
    auth_plugin='mysql_native_password'
    )

    
    def selectSongsDurationDB(self):

        mycursor = self.mydb.cursor()

        mycursor.execute("SELECT duration FROM song LIMIT 6;")

        record = mycursor.fetchall()

        print(record)
        
        return record










    async def selectMinID(self):
        try:
            connection = mysql.connector.connect(host='192.168.178.154', 
                                                database='aktiv_radio',
                                                user='radioaktiv',
                                                password='8877AktivRadio!8877',
                                                auth_plugin='mysql_native_password')
            if connection.is_connected():
                db_Info = connection.get_server_info()
                #print("Connected to MySQL Server version ", db_Info)
                cursor = connection.cursor()
                cursor.execute("SELECT MIN(song_id) as min_id FROM song LIMIT 1;")
                record = cursor.fetchone()
                #print("Your're cnnected to database: ", record)
                return record
        
        except Error as e:
            print("Error while connecting to Database", e)
        
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                #print("MySQL connection is closed")

    async def selectMaxID(self):
        try:
            connection = mysql.connector.connect(host='192.168.178.154', 
                                                database='aktiv_radio',
                                                user='radioaktiv',
                                                password='8877AktivRadio!8877',
                                                auth_plugin='mysql_native_password')
            if connection.is_connected():
                db_Info = connection.get_server_info()
                print("Connected to MySQL Server version ", db_Info)
                cursor = connection.cursor()
                cursor.execute("SELECT MAX(song_id) as max_id FROM song LIMIT 1;")
                record = cursor.fetchone()
                print("Your're cnnected to database: ", record)
        
        except Error as e:
            print("Error while connecting to Database", e)
        
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection is closed")


    def selectSpielzeit(self):
        try:    
            connection = mysql.connector.connect(host='192.168.178.154', 
                                                database='aktiv_radio',
                                                user='radioaktiv',
                                                password='8877AktivRadio!8877',
                                                auth_plugin='mysql_native_password')   
            if connection.is_connected():
                db_Info = connection.get_server_info()
                #print("Connected to MySQL Server version ", db_Info)
                cursor = connection.cursor()
                cursor.execute("select * from spielzeit WHERE spielzeitType = 'SZ' ORDER BY spzeit DESC;")
                record = cursor.fetchone()
                #print("Your're cnnected to database: ", record)
                return record
        
        except Error as e:
            print("Error while connecting to Database", e)
        
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                #print("MySQL connection is closed")


    def selectSong(self, songId):
        try:    
            connection = mysql.connector.connect(host='192.168.178.154', 
                                                database='aktiv_radio',
                                                user='radioaktiv',
                                                password='8877AktivRadio!8877',
                                                auth_plugin='mysql_native_password')    
            if connection.is_connected():
                db_Info = connection.get_server_info()
                print("Connected to MySQL Server version ", db_Info)
                cursor = connection.cursor()
                sqlSelectQuery = """SELECT song_name, artist, title, duration FROM song where song_id = %s"""
                cursor.execute(sqlSelectQuery, (songId,))
                record = cursor.fetchone()
                print("Your're cnnected to database: ", record)
                return record[0]
        
        except Error as e:
            print("Error while connecting to Database", e)
        
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection is closed")


    def selectJingle(self, start, end):
        try:    
            connection = mysql.connector.connect(host='192.168.178.154', 
                                                database='aktiv_radio',
                                                user='radioaktiv',
                                                password='8877AktivRadio!8877',
                                                auth_plugin='mysql_native_password')  
                                                
            if connection.is_connected():
                db_Info = connection.get_server_info()
                #print("Connected to MySQL Server version ", db_Info)
                cursor = connection.cursor()
                sqlSelectQuery = """SELECT * FROM spielzeit WHERE spielzeitType = "Jingle" AND WartenBisFertig = 1 AND spzeit BETWEEN %s AND %s"""
                cursor.execute(sqlSelectQuery, (start, end))
                record = cursor.fetchone()
                #print("Your're cnnected to database: ", record)
                return record
        
        except Error as e:
            print("Error while connecting to Database", e)
        
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                #print("MySQL connection is closed")                 
