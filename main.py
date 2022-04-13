import fillArrayTest
from fillArrayTest import Array_Instanz
#from clientTest import TCPInstanz

class main:
    def startFillArray(self):
        #start fillArray File
        Array_Instanz.selectSongsDuration()
        

mainInstanz = main()

if __name__ == "__main__":
    mainInstanz.startFillArray()