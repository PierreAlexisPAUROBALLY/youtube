import pandas as pd
from pytube import YouTube
from parameters import Parameters
import pandas

params=Parameters()

yt=YouTube("https://www.youtube.com/watch?v=xcIeh1rpdlA")
streams=yt.streams
streams.get_highest_resolution()

stream=streams[0]

df=pd.DataFrame(columns=["itag","isVideo","isAudio","codecs","extension","bitrate","resolution","fps","audio_bitrate","size"])


for i,stream in enumerate(streams):
    itag=stream.itag
    title=stream.title

    bitrate=stream.bitrate
    audio_bitrate=stream.abr

    codecs= stream.codecs # [videocoder, audiocodec]
    subtype=stream.subtype # extension

    resolution=stream.resolution
    fps=stream.fps
    size=stream.filesize

    video=stream.includes_video_track
    audio=stream.includes_audio_track

    slist=[itag,video,audio,codecs,subtype,bitrate,resolution,fps,audio_bitrate,size]
    df.loc[i]=slist



streams.get_by_itag(22).download(output_path=params.unprocessed,filename="test")