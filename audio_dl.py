from pytube import YouTube,Playlist
import sys
import os
from moviepy.editor import *

class YTAudioDownload():
    """
    Youtube auto generated playlist do not work, cant extract videos from it
    if 410 error, might need pytube update

    """

    def __init__(self,path="/home/piaxis/Music/"):
        self.path=path

    def _dl_from_yt_object(self,yt):
        file=yt.streams.get_audio_only().download(self.path)
        video = AudioFileClip(file)
        video.write_audiofile(file[:-1]+"3")
        os.remove(file)
  
    
    def dl(self,url):
        yt=YouTube(url)    
        self._dl_from_yt_object(yt)

    def dl_from_playlist(self,url_playlist):
        plist=Playlist(url_playlist)
        print(f"length of playlist: {plist.length}")
        for count,yt in enumerate(plist.videos):
            self._dl_from_yt_object(yt)
            print(f"done video {count+1} ")




if __name__=="__main__":
    """ 
    need to put brackets around url to download "https://www.youtube.com/watch?v=DhU10tZxVuda"  
    
    """
    url=sys.argv[1]

    try:
        path=sys.argv[2]
        YT=YTAudioDownload(path)
    except:
        YT=YTAudioDownload()

    if "list=" in url:
        print("Downloading playlist: " + url)
        YT.dl_from_playlist(url)
        
    else:
        print("Downloading video: "+url)
        YT.dl(url)
