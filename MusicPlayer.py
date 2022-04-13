import subprocess

class MusicPlayer:

    def __init__(self, songname, artist, title, duration, isJingle, firmaname):
        self.songname = songname
        self.artist = artist
        self.title = title
        self.duration = duration
        self.isJingle = isJingle
        self.firmaname = firmaname

    def playSong(self):
        if self.isJingle:
            cmdPlayJingle = """sudo mpg123 --equalizer --2to1 --smooth 
            /media/sf_Produktiv/Firmen/" + "\"" + this.firmaname + "\"/\"" + this.songname + "\""
             + " 2>&1 | while read i; do echo $(date): $i >> /media/sf_Produktiv/MusikteppichLog.txt; done"""
            process = subprocess.Popen(cmdPlayJingle, stdout=subprocess.PIPE)
            output, error = process.communicate()
            print(output, error)
        else:
            cmdPlaySong = """sudo mpg123 --equalizer --2to1 --smooth 
            /media/sf_Produktiv/Musikteppich/" + "\"" + self.songname + "\"" 
            + " 2>&1 | while read i; do echo $(date): $i >> /media/sf_Produktiv/MusikteppichLog.txt; done"""
            process = subprocess.Popen(cmdPlaySong, stdout=subprocess.PIPE)
            output, error = process.communicate()
            print(output, error)


    def playSZ(self, sZ):
        cmdKill = "pkill -f 'mpg123'"
        process = subprocess.Popen(cmdKill, stdout=subprocess.PIPE)
        output, error = process.communicate()
        
        # OBACHT, jingleinname von der Spielzeit
        # if sZ[JingleInname] != "":
            # cmdJingleIn = """sudo mpg123 /media/sf_Produktiv/Jingles/" + "\"" + ele.jinglein_name + "\"" + " 2>&1 | while read i; do echo $(date): $i >> /media/sf_Produktiv/MusikteppichLog.txt; done"""
            # process = subprocess.Popen(cmdJingleIn, stdout=subprocess.PIPE)
            # output, error = process.communicate()

        #TODO pfadauflösung korrekt...
        cmdPlaySZ = """sudo mpg123 --equalizer --2to1 --smooth 
        /media/sf_Produktiv/Firmen/" + "\"" + ele.firmaname + "\"/" + "\"" + ele.datei_name + "\"" 
        + " 2>&1 | while read i; do echo $(date): $i >> /media/sf_Produktiv/MusikteppichLog.txt; done"""
        process = subprocess.Popen(cmdPlaySZ, stdout=subprocess.PIPE)
        output, error = process.communicate()

        # OBACHT, jingleOutname von der Spielzeit
        # if sZ[JingleOutname] != "":
            # cmdJingleOut = """sudo mpg123 /media/sf_Produktiv/Jingles/" + "\"" + ele.jingleout_name + "\"" + " 2>&1 | while read i; do echo $(date): $i >> /media/sf_Produktiv/MusikteppichLog.txt; done"""
            # process = subprocess.Popen(cmdJingleIn, stdout=subprocess.PIPE)
            # output, error = process.communicate()



x = MusicPlayer("this", "that", "thisthat", 2, False, "Fanta")
x.playSong()