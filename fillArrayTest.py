import random
import socket
import time
import functools
import mysql.connector
import math
import socket
import sys
import threading
import time
from datetime import datetime, timedelta
from dateutil import parser as dateParse

from clientTest import TCPInstanz
from Database import Database



class ArrayXYZ():

        print("top of class")

        mydb = mysql.connector.connect(
        host="192.168.178.154",
        user="radioaktiv",
        password="8877AktivRadio!8877",
        database="aktiv_radio",
        auth_plugin='mysql_native_password'
        )

        host = "192.168.178.154"
        port1 = 2041
        port2 = 2040

        songSP = []
        DatabaseArrayS = []
        songArr = []
        songDurationArr = []
        jingleDurationArr = []

        def selectSongsDuration(self):

            while(True):

                DBInstanz = Database()

                

                songArrLength = len(self.songArr)



                
                #print(self.songDurationArr)


                JingleSzArray = []

                #print(self.songSP)

                JingleSzArray = DBInstanz.selectJingle(self.songSP[0], self.songSP[5])
                self.calc(JingleSzArray, self.songSP, self.songDurationArr)

        def calc(self, JingleSzArray, songSP, songDurationArr):

            DBInstanz = Database()

            JingleArr = []

            JingleNameArr = []

            date0 = songSP[0]
            date1 = songSP[1]
            date2 = songSP[2]
            date3 = songSP[3]
            date4 = songSP[4]
            date5 = songSP[5]

            self.DatabaseArrayS = ["dbS1", "dbS2", "dbS3", "dbS4", "dbS5"]

            #clientTest.function2(DatabaseArrayS[1])

            songs = [self.DatabaseArrayS[0], self.DatabaseArrayS[1], self.DatabaseArrayS[2], self.DatabaseArrayS[3],self.DatabaseArrayS[4]]
            testSong = "tstS"

            DatabaseArraySzLength = len(JingleSzArray)

            jingleDateArr = []

            jingleNameArrayLength = len(JingleNameArr)

            for b in range(DatabaseArraySzLength):
                JingleNameArr.append(DBInstanz.selectDatei(JingleSzArray[b][4]))

            print(JingleNameArr, " sssssssssssssSSSSSSSSSSSSSS")

            for a in range(DatabaseArraySzLength):
                JingleArr.append(DBInstanz.selectJingleForArray(JingleNameArr[a][0]))


            print(JingleArr)

            for x in range(DatabaseArraySzLength):
                jingleDateArr.append(JingleSzArray[x][1])

            print(self.songArr[5])

            for u in range(DatabaseArraySzLength):
                szDate = jingleDateArr[u]

                if szDate < date0:
                    self.songArr.pop(0)
                    self.songArr.insert(0, self.songArr[0])

                if szDate < date1:
                    self.songArr.pop(1)
                    #if self.songArr[0] != JingleNameArr[0]:
                    #self.songArr.pop(4)
                    print(len(self.songArr), "ERSTER")
                    self.songArr.insert(1, JingleArr[u])

                if szDate < date2 and szDate > date1:
                    self.songArr.pop(2)
                    #self.songArr.pop(4)
                    print(len(self.songArr), "ZWEITER")
                    self.songArr.insert(2, JingleArr[u])

                if szDate > date2  and szDate < date3:
                    self.songArr.pop(3)
                    #self.songArr.pop(4)
                    print(len(self.songArr), "DRITTER")
                    self.songArr.insert(3, JingleArr[u])

                if szDate > date3 and szDate < date4:
                    self.songArr.pop(4)
                    #self.songArr.pop(4)
                    print(len(self.songArr), "VIERTER")
                    self.songArr.insert(4, JingleArr[u])

                if szDate > date4 and szDate < date5:
                    self.songArr.pop(5)
                    print(len(self.songArr), "FÜNFTER")
                    self.songArr.insert(5, JingleArr[u])

            for e in range(6):
              print(self.songArr[e][1])


            #duration = functools.reduce(lambda sub, ele: sub * 10 + ele, durationDB[0])

            #duration = songDurationArr[0]
            sec = self.songArr[0][3]

           # z = duration
            min = 0
    
            while(sec > 60):
                min += 1
                sec -= 60

            y = self.songArr[0][3] + 1

            print("In function")

            g = 0
            y-=1


            for x in range(y):
                self.tcpConn(sec, min)
                if sec == 0 and min > 0:
                    min -= 1
                    sec += 60
                sec -= 1
                time.sleep(1)

            self.songArr.pop(0)

            self.RandomID = random.randint(self.minID, self.maxID)

            song = DBInstanz.selectSong(self.RandomID)
            self.songArr.insert(5, song)
            #for l in range(6):
               # print(self.songArr[l][0])

            now = datetime.now()
        
            print(len(self.songSP))

          
            self.songSP.clear()

            y = 6

            for x in range(y):

                timeSong = 0
                #sec = functools.reduce(lambda sub, ele: sub * 10 + ele, self.songDurationArr[x])
                sec = self.songArr[x][3]

                timeSong += sec
                                    
                finalDate = now + timedelta(seconds=timeSong)

                songSP.append(finalDate)
            
            
            print(self.songArr)
            
            #for u in range(6):
               # print(songSP[u])

            TCPInstanz.startThread(self.songArr)
                
    
        def tcpConn(self, sec, min):


            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((self.host, self.port1))
            if sec < 10:
                r = ("0" + str(sec))
            if sec > 10:
                r = str(sec)
            if sec == 10:
                r = str(sec)
            s.send(r.encode())
            s.close()


            sMin = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sMin.connect((self.host, self.port2))
            if min < 10:
                rMin = ( "0" + str(min))
            if min > 10:
                rMin = str(min)
            if min == 10:
                rMin = str(min)
            sMin.send(rMin.encode())
            sMin.close()

            print(rMin, ":", r)
    






        DBInstanz = Database()
        TCPInstanz


        y = 6
        for x in range(y):
            minID = DBInstanz.selectMinID()
            maxID = DBInstanz.selectMaxID()

            RandomID = random.randint(minID, maxID)

            song = DBInstanz.selectSong(RandomID)
            songArr.append(song)
       # for t in range(6):
            #print(songArr[t][0])
        print(len(songArr))
        
        
        now = datetime.now()

        timeSong = 0

        for x in range(y):

            
            #sec = functools.reduce(lambda sub, ele: sub * 10 + ele, self.songDurationArr[x])
            sec = songArr[x][3]

            timeSong += sec
                                
            finalDate = now + timedelta(seconds=timeSong)

            songSP.append(finalDate)

        print(songSP)
        TCPInstanz.startThread(songArr)         

            
Array_Instanz = ArrayXYZ()