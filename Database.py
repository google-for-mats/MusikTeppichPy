from colorama import Cursor
import mysql.connector
from mysql.connector import Error
#from fillArrayTest import *

class Database:

    def __connectToDB(self):
        return mysql.connector.connect(host='192.168.178.154', database='aktiv_radio', user='radioaktiv', password='8877AktivRadio!8877', auth_plugin='mysql_native_password')
        #return mysql.connector.connect(host='192.168.178.154', database='aktiv_radio', user='radioaktiv', password='8877AktivRadio!8877', auth_plugin='mysql_native_password')

    #public Methods
    #Select and Delete
    def selectMinID(self):
        try:
            connection = self.__connectToDB()
            if connection.is_connected():
                cursor = connection.cursor()
                cursor.execute("SELECT MIN(song_id) as min_id FROM song LIMIT 1;")
                record = cursor.fetchone()
                return record[0]
        
        except Error as e:
            print("Error while connecting to Database", e)
        
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def selectMaxID(self):
        try:
            connection = self.__connectToDB()
            if connection.is_connected():
                cursor = connection.cursor()
                cursor.execute("SELECT MAX(song_id) as max_id FROM song LIMIT 1;")
                record = cursor.fetchone()
                return record[0]
        
        except Error as e:
            print("Error while connecting to Database", e)
        
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()


    def selectSpielzeit(self, start, end):
        try:    
            connection = self.__connectToDB()    
            if connection.is_connected():
                cursor = connection.cursor()
                sqlSelectQuery = """SELECT * FROM spielzeit WHERE spielzeitType = "SZ" AND spzeit BETWEEN %s AND %s ORDER BY spzeit DESC;"""
                cursor.execute(sqlSelectQuery, (start, end))
                record = cursor.fetchone()
                return record

        except Error as e:
            print("Error while connecting to Database", e)
        
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def deleteSpielzeit(self, sZID):
        try:    
            connection = self.__connectToDB()    
            if connection.is_connected():
                cursor = connection.cursor()
                sqlSelectQuery = """DELETE FROM spielzeit WHERE spielzeitType = "SZ" AND spielzeit_id = %s;"""
                cursor.execute(sqlSelectQuery, (sZID,))

        except Error as e:
            print("Error while connecting to Database", e)
        
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def selectSong(self, songId):
        try:    
            connection = self.__connectToDB()    
            if connection.is_connected():
                cursor = connection.cursor()
                sqlSelectQuery = """SELECT song_name, artist, title, duration FROM song where song_id = %s"""
                cursor.execute(sqlSelectQuery, (songId,))
                record = cursor.fetchone()
                return record
        
        except Error as e:
            print("Error while connecting to Database", e)
        
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def selectJingle(self, start, end):
        try:    
            connection = self.__connectToDB()                             
            if connection.is_connected():
                cursor = connection.cursor()
                sqlSelectQuery = """SELECT * FROM spielzeit WHERE spielzeitType = "Jingle" AND WartenBisFertig = 1 AND spzeit BETWEEN %s AND %s LIMIT 5"""
                cursor.execute(sqlSelectQuery, (start, end))
                record = cursor.fetchall()
                return record

        except Error as e:
            print("Error while connecting to Database", e)
        
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def deleteJingle(self, sZID):
        try:    
            connection = self.__connectToDB()    
            if connection.is_connected():
                cursor = connection.cursor()
                sqlSelectQuery = """DELETE FROM spielzeit WHERE spielzeit_id = %s;"""
                cursor.execute(sqlSelectQuery, (sZID,))

        except Error as e:
            print("Error while connecting to Database", e)
        
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def selectJingleForArray(self, dateiId):
        try:
            connection = self.__connectToDB()
            if connection.is_connected():
                cursor = connection.cursor()
                sqlSelectQuery = """SELECT datei_name, firmaname, datei_name, duration FROM datei JOIN firma ON(datei.firma_id = firma.firma_id) WHERE datei_id = %s;"""
                cursor.execute(sqlSelectQuery, (dateiId,))
                record = cursor.fetchone()
                return record

        except Error as e:
            print("Error while connecting to Database", e)
        
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
    def selectDatei(self, dateiId):
        try:    
            connection = self.__connectToDB()                             
            if connection.is_connected():
                cursor = connection.cursor()
                sqlSelectQuery = """SELECT * FROM datei WHERE datei_id = %s"""
                cursor.execute(sqlSelectQuery, (dateiId,))
                record = cursor.fetchone()
                return record[0], record[1], record[2]
        
        except Error as e:
            print("Error while connecting to Database", e)
        
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
