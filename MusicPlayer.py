import subprocess
#14. Apr 2022
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
            cmdPlayJingle = "mpg123 --equalizer --2to1 --smooth /media/sf_Produktiv/Firmen/" + "\"" + self.firmaname + "\"/\"" + self.songname + "\"" + " 2>&1 | while read i; do echo $(date): $i >> /media/sf_Produktiv/MusikteppichLog.txt; done"
            process = subprocess.Popen(cmdPlayJingle, stdout=subprocess.PIPE, shell=True)
            output, error = process.communicate()
            print(output, error)
        else:   #"""self.songname"""
            cmdPlaySong = "mpg123 --equalizer --2to1 --smooth /home/matlargro_ubuntu_lap/Documents/musik/\"" + self.songname + "\"" #" 2>&1 | while read i; do echo $(date): $i >> /media/sf_Produktiv/MusikteppichLog.txt; done"
            process = subprocess.Popen(cmdPlaySong, stdout=subprocess.PIPE, shell=True)
            output, error = process.communicate()
            print(output, error)


    def playSZ(self, sZ):
        cmdKill = "pkill -f 'mpg123'"
        process = subprocess.Popen(cmdKill, stdout=subprocess.PIPE, shell=True)
        output, error = process.communicate()
        
        # OBACHT, jingleinname von der Spielzeit
        # if sZ[JingleInname] != "":
            # cmdJingleIn = "sudo mpg123 /media/sf_Produktiv/Jingles/" + "\"" + ele.jinglein_name + "\"" + " 2>&1 | while read i; do echo $(date): $i >> /media/sf_Produktiv/MusikteppichLog.txt; done"
            # process = subprocess.Popen(cmdJingleIn, stdout=subprocess.PIPE)
            # output, error = process.communicate()

        #TODO pfadauflösung korrekt...
        cmdPlaySZ = "mpg123 --equalizer --2to1 --smooth /media/sf_Produktiv/Firmen/" + "\"" + sZ.firmaname + "\"/" + "\"" + sZ.datei_name + "\"" + " 2>&1 | while read i; do echo $(date): $i >> /media/sf_Produktiv/MusikteppichLog.txt; done"
        process = subprocess.Popen(cmdPlaySZ, stdout=subprocess.PIPE, shell=True)
        output, error = process.communicate()

        # OBACHT, jingleOutname von der Spielzeit
        # if sZ[JingleOutname] != "":
            # cmdJingleOut = "sudo mpg123 /media/sf_Produktiv/Jingles/" + "\"" + ele.jingleout_name + "\"" + " 2>&1 | while read i; do echo $(date): $i >> /media/sf_Produktiv/MusikteppichLog.txt; done"
            # process = subprocess.Popen(cmdJingleIn, stdout=subprocess.PIPE)
            # output, error = process.communicate()