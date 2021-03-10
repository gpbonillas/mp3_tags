import os, glob, eyed3

os.chdir("./")
for file in glob.glob("*.mp3"):

    filename = os.path.basename(file)
    
    artist = filename
    track = filename
	
    audiofile = eyed3.load("./" + filename)
    audiofile.initTag()
    audiofile.tag.artist = str(artist)
    audiofile.tag.title = str(track.split('.mp3')[0]) #+ '_sermon'
    audiofile.tag.save()
    
    os.rename(filename, track)
