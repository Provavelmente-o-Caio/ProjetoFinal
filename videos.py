#pyp install pytube
from pytube import YouTube
import os 

class Video():
    def __init__(self, link):
        self.link=link
        self.objVideo = YouTube(link)


    def downloadAudio(self):
        audiodecria = self.objVideo.streams.filter(only_audio = True).filter(audio_codec= 'mp3').first()
        out_file = audiodecria.download("download/audio")