import socket
import threading
import time


host = "192.168.178.154"

def function1():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port1 = 2020

    s.connect((host, port1))
    r = "280"
    s.send(r.encode())
    print("Connected 1")
    s.close()

def function2():
    s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port2 = 2021
    s2.connect((host, port2))
    r = ''
    s2.send(r.encode())
    s2.close()
    print("Connected 2")


def function3():
    s3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port3 = 2022
    s3.connect((host, port3))
    r = ''
    s3.send(r.encode())
    s3.close()
    print("Connected 3")

def function4():
    s4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port4 = 2023
    s4.connect((host, port4))
    r = ''
    s4.send(r.encode())
    s4.close()
    print("Connected 4")

def function5():
    s5 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port5 = 2024
    s5.connect((host, port5))
    r = ''
    s5.send(r.encode())
    s5.close()
    print("Connected 5")

def function6():
    s6 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port6 = 2025
    s6.connect((host, port6))
    r = ''
    s6.send(r.encode())
    s6.close()
    print("Connected 6")

def function7():
    s7 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port7 = 2026
    s7.connect((host, port7))
    r = ''
    s7.send(r.encode())
    s7.close()
    print("Connected 7")

def function8():
    s8 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port8 = 2027
    s8.connect((host, port8))
    r = ''
    s8.send(r.encode())
    s8.close()
    print("Connected 8")

def function9():
    s9 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port9 = 2028
    s9.connect((host, port9))
    r = ''
    s9.send(r.encode())
    s9.close()
    print("Connected 9")

def function10():
    s10 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port10 = 2029
    s10.connect((host, port10))
    r = ''
    s10.send(r.encode())
    s10.close()
    print("Connected 10")

def function11():
    s11 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port11 = 2030
    s11.connect((host, port11))
    r = ''
    s11.send(r.encode())
    s11.close()
    print("Connected 11")

def function12():
    s12 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port12 = 2031
    s12.connect((host, port12))
    r = ''
    s12.send(r.encode())
    s12.close()
    print("Connected 12")

def function13():
    s13 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port13 = 2032
    s13.connect((host, port13))
    r = ''
    s13.send(r.encode())
    s13.close()
    print("Connected 13")

def function14():
    s14 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port14 = 2033
    s14.connect((host, port14))
    r = ''
    s14.send(r.encode())
    s14.close()
    print("Connected 14")

def function15():
    s15 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port15 = 2034
    s15.connect((host, port15))
    r = ''
    s15.send(r.encode())
    s15.close()
    print("Connected 15")

def function16():
    s16 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port16 = 2035
    s16.connect((host, port16))
    r = ''
    s16.send(r.encode())
    s16.close()
    print("Connected 16")

def function17():
    s17 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port17 = 2036
    s17.connect((host, port17))
    r = ''
    s17.send(r.encode())
    s17.close()
    print("Connected 17")

def function18():
    s18 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port18 = 2037
    s18.connect((host, port18))
    r = ''
    s18.send(r.encode())
    s18.close()
    print("Connected 18")

def function19():
    s19 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port19 = 2038
    s19.connect((host, port19))
    r = ''
    s19.send(r.encode())
    s19.close()
    print("Connected 19")

def function21():
    s21 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port21 = 2040
    s21.connect((host, port21))
    r = ''
    s21.send(r.encode())
    s21.close()
    print("Connected 21")

def function22():
    s22 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port22 = 2041
    s22.connect((host, port22))
    r = ''
    s22.send(r.encode())
    s22.close()
    print("Connected 22")

def function23():
    s23 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port23 = 2042
    s23.connect((host, port23))
    r = ''
    s23.send(r.encode())
    s23.close()
    print("Connected 23")

def function24():
    s24 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port24 = 2043
    s24.connect((host, port24))
    r = ''
    s24.send(r.encode())
    s24.close()
    print("Connected 24")

def function25():
    s25 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port25 = 2044
    s25.connect((host, port25))
    r = ''
    s25.send(r.encode())
    s25.close()
    print("Connected 25")

t1 = threading.Thread(target=function1)
t2 = threading.Thread(target=function2)
t3 = threading.Thread(target=function3)
t4 = threading.Thread(target=function4)
t5 = threading.Thread(target=function5)
t6 = threading.Thread(target=function6)
t7 = threading.Thread(target=function7)
t8 = threading.Thread(target=function8)
t9 = threading.Thread(target=function9)
t10 = threading.Thread(target=function10)
t11 = threading.Thread(target=function11)
t12 = threading.Thread(target=function12)
t13 = threading.Thread(target=function13)
t14 = threading.Thread(target=function14)
t15 = threading.Thread(target=function15)
t16 = threading.Thread(target=function16)
t17 = threading.Thread(target=function17)
t18 = threading.Thread(target=function18)
t19 = threading.Thread(target=function19)
t21 = threading.Thread(target=function21)
t22 = threading.Thread(target=function22)
t23 = threading.Thread(target=function23)
t24 = threading.Thread(target=function24)
t25 = threading.Thread(target=function25)

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()
t9.start()
t10.start()
t11.start()
t12.start()
t13.start()
t14.start()
t15.start()
t16.start()
t17.start()
t18.start()
t19.start()
t21.start()
t22.start()
t23.start()
t24.start()
t25.start()