#pyp install pytube
from pytube import YouTube

class Video():
    def __init__(self, link):
        self.link=link
        self.objVideo = YouTube(link)


    def downloadVideo(self):
        videodecria = self.objVideo.streams.get_highest_resolution()
        videodecria.download()