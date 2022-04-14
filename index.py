from Database import Database as DB
from MusicPlayer import MusicPlayer as MP

myDB = DB()
minID = myDB.selectMinID()
maxID = myDB.selectMaxID()
song = myDB.selectSong(5750)
#firmaname = myDB.selectFirmaname(111111111)
sZeit = myDB.selectSpielzeit("2022-03-24 16:25:00", "2022-04-12 17:29:00")
#myDB.deleteSpielzeit(52821)
jingles = myDB.selectJingle("2022-03-24 16:25:00", "2022-04-12 17:29:00")
#myDB.deleteJingle(52820)
dateiname = myDB.selectDatei(43)


print(minID, maxID)
print(song)
print(sZeit)
print(jingles)
print(dateiname)

x = MP("18 Grease - Megamix Operación Triunfo 2005.mp3", "thaht", "thishaihd", 3, False, "keine")
x.playSong()

