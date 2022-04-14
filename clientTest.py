import socket
import sys
import threading
import time
#from main import mainInstanz
#import fillArrayTest 
#from fillArrayTest import *
# -*- coding: utf-8 -*-
#sys.setlocale("LC_ALL", "de_DE.UTF-8")

host = "192.168.178.154"

print("Client")

class TCPServer:

    def function1(self, crntDuration):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        port1 = 2020
        s.connect((host, port1))
        print("Connected 1")
        r = str(crntDuration) #str(crntDuration)
        s.send(r.encode())
        s.close()

    def function2(self, crntTitle):
        #ArrayXYZ().selectSpielzeit()

        #song2 = ArrayXYZ().songs
        s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        port2 = 2021
        s2.connect((host, port2))
        print("Connected 2")
        r = str(crntTitle)
        s2.send(r.encode())
        s2.close()
        #print(Instanz.DatabaseArrayS[0])

        


    def function3(self, crnArtist):
        s3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        port3 = 2022
        s3.connect((host, port3))
        print("Connected 3")
        r = str(crnArtist)
        s3.send(r.encode())
        s3.close()

    def function4(self):
        s4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        port4 = 2023
        s4.connect((host, port4))
        print("Connected 4")
        r = ''
        s4.send(r.encode())
        s4.close()

    def function5(self, duration1):
        s5 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        port5 = 2024
        s5.connect((host, port5))
        print("Connected 5")
        r = str(duration1)
        s5.send(r.encode())
        s5.close()

    def function6(self, title1):
        s6 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        port6 = 2025
        s6.connect((host, port6))
        print("Connected 6")
        r = str(title1)
        s6.send(r.encode())
        s6.close()

    def function7(self, artist1):
        s7 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        port7 = 2026
        s7.connect((host, port7))
        print("Connected 7")
        r = str(artist1)
        s7.send(r.encode())
        s7.close()

    def function8(self, duration2):
        s8 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        port8 = 2027
        s8.connect((host, port8))
        print("Connected 8")
        r = str(duration2)
        s8.send(r.encode())
        s8.close()

    def function9(self, title2):
        s9 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        port9 = 2028
        s9.connect((host, port9))
        print("Connected 9")
        r = str(title2)
        s9.send(r.encode())
        s9.close()

    def function10(self, artist2):
        s10 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        port10 = 2029
        s10.connect((host, port10))
        print("Connected 10")
        r = str(artist2)
        s10.send(r.encode())
        s10.close()

    def function11(self, duration3):
        s11 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        port11 = 2030
        s11.connect((host, port11))
        print("Connected 11")
        r = str(duration3)
        s11.send(r.encode())
        s11.close()

    def function12(self, title3):
        s12 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        port12 = 2031
        s12.connect((host, port12))
        print("Connected 12")
        r = str(title3)
        s12.send(r.encode())
        s12.close()

    def function13(self, artist3):
        s13 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        port13 = 2032
        s13.connect((host, port13))
        print("Connected 13")
        r = str(artist3)
        s13.send(r.encode())
        s13.close()

    def function14(self, duration4):
        s14 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        port14 = 2033
        s14.connect((host, port14))
        print("Connected 14")
        r = str(duration4)
        s14.send(r.encode())
        s14.close()

    def function15(self, title4):
        s15 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        port15 = 2034
        s15.connect((host, port15))
        print("Connected 15")
        r = str(title4)
        s15.send(r.encode())
        s15.close()

    def function16(self, artist4):
        s16 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        port16 = 2035
        s16.connect((host, port16))
        print("Connected 16")
        r = str(artist4)
        s16.send(r.encode())
        s16.close()

    def function17(self, duration5):
        s17 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        port17 = 2036
        s17.connect((host, port17))
        print("Connected 17")
        r = str(duration5)
        s17.send(r.encode())
        s17.close()

    def function18(self, title5):
        s18 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        port18 = 2037
        s18.connect((host, port18))
        print("Connected 18")
        r = str(title5)
        s18.send(r.encode())
        s18.close()

    def function19(self, artist5):
        s19 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        port19 = 2038
        s19.connect((host, port19))
        print("Connected 19")
        r = str(artist5)
        s19.send(r.encode())
        s19.close()

    def function21(self):
        s21 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        port21 = 2040
        s21.connect((host, port21))
        print("Connected 21")
        r = ''
        s21.send(r.encode())
        s21.close()

    def function22(self):
        s22 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        port22 = 2041
        s22.connect((host, port22))
        print("Connected 22")
        r = ''
        s22.send(r.encode())
        s22.close()

    def function23(self):
        s23 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        port23 = 2042
        s23.connect((host, port23))
        print("Connected 23")
        r = ''
        s23.send(r.encode())
        s23.close()

    def function24(self):
        s24 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        port24 = 2043
        s24.connect((host, port24))
        print("Connected 24")
        r = ''
        s24.send(r.encode())
        s24.close()

    def function25(self):
        s25 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        port25 = 2044
        s25.connect((host, port25))
        print("Connected 25")
        r = ''
        s25.send(r.encode())
        s25.close()

    def startThread(self, songArr):

        #mainInstanz.startFillArray()

        print("In start thread")
        
        print("Th1 initialzed")
        self.t1 = threading.Thread(target=self.function1(songArr[0][3]))
        self.t2 = threading.Thread(target=self.function2(songArr[0][2]))
        self.t3 = threading.Thread(target=self.function3(songArr[0][1]))
        self.t4 = threading.Thread(target=self.function4)
        self.t5 = threading.Thread(target=self.function5(songArr[1][3]))
        self.t6 = threading.Thread(target=self.function6(songArr[1][2]))
        self.t7 = threading.Thread(target=self.function7(songArr[1][1]))
        self.t8 = threading.Thread(target=self.function8(songArr[2][3]))
        self.t9 = threading.Thread(target=self.function9(songArr[2][2]))
        self.t10 = threading.Thread(target=self.function10(songArr[2][1]))
        self.t11 = threading.Thread(target=self.function11(songArr[3][3]))
        self.t12 = threading.Thread(target=self.function12(songArr[3][2]))
        self.t13 = threading.Thread(target=self.function13(songArr[3][1]))
        self.t14 = threading.Thread(target=self.function14(songArr[4][3]))
        self.t15 = threading.Thread(target=self.function15(songArr[4][2]))
        self.t16 = threading.Thread(target=self.function16(songArr[4][1]))
        self.t17 = threading.Thread(target=self.function17(songArr[5][3]))
        self.t18 = threading.Thread(target=self.function18(songArr[5][2]))
        self.t19 = threading.Thread(target=self.function19(songArr[5][1]))
        #self.t21 = threading.Thread(target=self.function21)
        #self.t22 = threading.Thread(target=self.function22)
        self.t23 = threading.Thread(target=self.function23)
        self.t24 = threading.Thread(target=self.function24)
        self.t25 = threading.Thread(target=self.function25)

        self.t1.start()
        self.t2.start()
        self.t3.start()
        self.t4.start()
        self.t5.start()
        self.t6.start()
        self.t7.start()
        self.t8.start()
        self.t9.start()
        self.t10.start()
        self.t11.start()
        self.t12.start()
        self.t13.start()
        self.t14.start()
        self.t15.start()
        self.t16.start()
        self.t17.start()
        self.t18.start()
        self.t19.start()
        #self.t21.start()
        #self.t22.start()
        self.t23.start()
        self.t24.start()
        self.t25.start()

TCPInstanz = TCPServer()


