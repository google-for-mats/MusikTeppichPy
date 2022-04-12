import time
import functools
import os
import mysql.connector
from datetime import datetime, timedelta
from dateutil import parser as dateParse
from clientTest import *


class ArrayXYZ:

    print("top of class")

    mydb = mysql.connector.connect(
    host="192.168.178.154",
    user="radioaktiv",
    password="8877AktivRadio!8877",
    database="aktiv_radio",
    auth_plugin='mysql_native_password'
    )

    
    
    songSP = []
    DatabaseArrayS = []

    def selectSongsDuration(self):

        now = datetime.now()
        dateTimeNow = now.strftime("%Y-%m-%d %H:%M:%S")

        mycursor = self.mydb.cursor()

        mycursor.execute("SELECT duration FROM song LIMIT 6;")

        durationDB = mycursor.fetchall()
        print(durationDB)
        y = 0
        timeSong = 0

        for x in durationDB:
            sec = functools.reduce(lambda sub, ele: sub * 10 + ele, durationDB[y])

            for w in x:
                timeSong += sec

            
            finalDate = now + timedelta(seconds=timeSong)

            self.songSP.append(finalDate)
            y += 1

        self.selectSpielzeit(self.songSP, durationDB)
            


    def selectSpielzeit(self, songSP, durationDB):
        mycursor = self.mydb.cursor()

        mycursor.execute("SELECT spzeit FROM spielzeit ORDER BY spzeit ASC LIMIT 6;")

        DatabaseArraySz = mycursor.fetchall()

        self.calc(DatabaseArraySz, songSP, durationDB)


    """ def query1():
        mycursor = mydb.cursor()

        mycursor.execute("SELECT spzeit FROM spielzeit ORDER BY spzeit ASC LIMIT 6;")

        DatabaseArraySz = mycursor.fetchall() """



    def calc(self, DatabaseArraySz, songSP, durationDB):

        c = 0

        print(songSP)

        date1 = songSP[0]
        date2 = songSP[1]
        date3 = songSP[2]
        date4 = songSP[3]
        date5 = songSP[5]

        print(date1)

        self.DatabaseArrayS = ["dbS1", "dbS2", "dbS3", "dbS4", "dbS5"]

        #clientTest.function2(DatabaseArrayS[1])

        songs = [self.DatabaseArrayS[0], self.DatabaseArrayS[1], self.DatabaseArrayS[2], self.DatabaseArrayS[3],self.DatabaseArrayS[4]]
        testSong = "tstS"

        for u in DatabaseArraySz:
            szDate = functools.reduce(lambda sub, ele: sub * 10 + ele, DatabaseArraySz[c])
            if szDate < date1:
                songs.pop(4)
                songs.insert(0, testSong)

            if szDate < date2 and szDate > date1:
                songs.pop(4)
                songs.insert(1, testSong)

            if szDate > date2  and szDate < date3:
                songs.pop(4)
                songs.insert(2, testSong)

            if szDate > date3 and szDate < date4:
                songs.pop(4)
                songs.insert(3, testSong)

            if szDate > date4 and szDate < date5:
                songs.pop(4)
                songs.insert(4, testSong)
            
            c += 1

        print(songs)



        #duration = functools.reduce(lambda sub, ele: sub * 10 + ele, durationDB[0])

        duration = 2
        f1=1
        f2=2
        f3=3
        z = duration
        y = duration + 1

        for x in range(duration):
            y-=1
            print(y)
            time.sleep(1)
        print("after loop")
        TCPInstanz.startThread(f1, f2, f3)
        
        

print("before instanz")
Instanz = ArrayXYZ()
Instanz.selectSongsDuration()



print("after instanz")

if __name__ == "__main__":
    print("Start")
print("after if main")

