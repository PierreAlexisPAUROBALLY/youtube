from pytube import YouTube,Playlist
import sys
import os
from moviepy.editor import *

class YTAudioDownload():
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
        for yt in plist.videos:
            self._dl_from_yt_object(yt)
            
        
