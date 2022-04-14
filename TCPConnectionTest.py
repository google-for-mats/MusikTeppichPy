import socket
import time


host = "192.168.43.226"
port1 = 2041
port2 = 2040




""" s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port1))
print("Connected 1")
r = 'ewrewewr'
s.send(r.encode())
s.close() """




def conn1(sec, min):
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port1))
    print("Connected 1 sec")
    if sec < 10:
        r = ("0" + str(sec))
    if sec > 10:
        r = str(sec)
    if sec == 10:
        r = str(sec)
    s.send(r.encode())
    s.close()


    sMin = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sMin.connect((host, port2))
    print("Connected 1 min")
    if min < 10:
        rMin = ( "0" + str(min))
    if min > 10:
        rMin = str(min)
    if min == 10:
        rMin = str(min)
    sMin.send(rMin.encode())
    sMin.close()
    



    """ 
    if sec > -1 and min > -1:
        conn2(sec, min) """

def alert(count):
    print("ALERT")
    count += 1
    print(count)

def conn2(sec, min):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port1))
    print("Connected 2 sec")
    if sec < 10:
        r = ("0" + str(sec))
    if sec > 10:
        r = str(sec)
    if sec == 10:
        r = str(sec)
    s.send(r.encode())
    s.close()
    

    sMin = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sMin.connect((host, port2))
    print("Connected 2 min")
    if min < 10:
        rMin = ("0" +str(min))
    if min > 10:
        rMin = str(min)
    if min == 10:
        rMin = str(min)
    sMin.send(rMin.encode())
    sMin.close()

    
    if sec == 0 and min > 0:
        min -= 1
        sec += 60

    sec -= 1

    time.sleep(1)

    if sec > -1 and min > -1:
        conn1(sec, min)
    
    
    print("done2")


duration = 100
sec = duration
min = 0


while(sec > 60):
    min += 1
    sec -= 60


for x in range(duration):
    conn1(sec, min)
    if sec == 0 and min > 0:
        min -= 1
        sec += 60
    sec -= 1
    time.sleep(1)