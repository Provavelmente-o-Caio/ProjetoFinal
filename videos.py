#pyp install pytube
from pytube import YouTube
import os
<<<<<<< HEAD
=======
import re
import moviepy.editor as mp
>>>>>>> testes2

class Video():
    def __init__(self, link):
        self.link=link
        self.objYT = YouTube(link)

<<<<<<< HEAD

    def downloadVideo(self):
        video = self.objYT.streams.get_highest_resolution()
        video.download("download/video")

    def downloadAudio(self):
        pass
=======
    def downloadVideo(self, path):
        self.objVideo.streams.get_highest_resolution().download(path)
        
        
    def downloadAudio(self, path):
        self.objVideo.streams.filter(only_audio = True).first().download(path)
        for file in os.listdir(path):                  #For para percorrer dentro da pasta passada anteriormente
            if re.search('mp4', file):                 #If verificando se o arquivo e .MP4                    
                mp4_path = os.path.join (path, file)  #Cria uma variavel para armazenar o arquivo .MP4
                mp3_path = os.path.join (path, os.path.splitext(file)[0] + '.mp3') # Variavel que cria o nome do arquivo e adiciona .MP3 ao final
                new_file = mp.AudioFileClip(mp4_path)  #Cria o arquivo de áudio (.MP3)
                new_file.write_audiofile(mp3_path)     #Renomeia o arquivo, setando o nome criado anteriormente
                #os.remove(mp4_path)                    #Remove o arquivo .MP4; desetivar linha permite salvar o audio e video do mesmo video ao mesmo tempo
>>>>>>> testes2
