#pyp install pytube
from pytube import YouTube
import os 

class Video():
    def __init__(self, link):
        self.link=link
        self.objAudio = YouTube(link)


    def downloadVideo(self):
        videodecria = self.objAudio.streams.filter(only_audio = True).first()
        videodecria.download()