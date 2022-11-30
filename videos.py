#pyp install pytube
from pytube import YouTube
import os

class Video():
    def __init__(self, link):
        self.link=link
        self.objYT = YouTube(link)


    def downloadVideo(self):
        video = self.objYT.streams.get_highest_resolution()
        video.download("download/video")

    def listaVideo(self):
        titulo = self.objYT.title()