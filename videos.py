#pyp install pytube
from pytube import YouTube
import os

class Video():
    def __init__(self, link):
        self.link=link
        self.objVideo = YouTube(link)


    def downloadVideo(self):
        video = self.objVideo.streams.get_highest_resolution()
        video.download("download")

    def listaVideo(self):
        titulo = self.objVideo.title()