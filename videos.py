#pip install pytube and moviepy
from pytube import YouTube, Playlist
import os, re, moviepy.editor as mp, PySimpleGUI as sg
class IndividualVideo():
    def __init__(self, link):
        self.link=link
        self.objYT = YouTube(link)
class PlaylistVideo():
    def __init__(self,link):
        self.link = link
        self.objYTPL = Playlist(link)


class IndividualDownload(IndividualVideo):
    def __init__(self, link, path):
        super().__init__(link)
        self.path = path
    
    def downloadVideo(self):
        self.objYT.streams.get_highest_resolution().download(self.path, filename_prefix="video_", skip_existing= True)
        
    
    def downloadAudio(self):
        self.objYT.streams.filter(only_audio = True).first().download(self.path, filename_prefix="audio_", skip_existing= True)
    
    
class PlaylistDownload(PlaylistVideo):
    def __init__(self, link, path):
        super().__init__(link)
        self.path = path
        
    def downloadAllVideos(self):
        for url in self.objYTPL:
            YouTube(url).streams.get_highest_resolution().download(self.path, filename_prefix="video_", skip_existing= True)
    
    
    def downloadAllTracks(self):
        for url in self.objYTPL:
            YouTube(url).streams.filter(only_audio = True).first().download(self.path, filename_prefix="audio_", skip_existing= True)
        
        
    def conversor(path):
        for file in os.listdir(path):                      #For para percorrer dentro da pasta passada anteriormente
                if re.search('mp4', file) and "audio_"in file:                 #If verificando se o arquivo e .MP4                    
                    mp4_path = os.path.join (path, file)   #Cria uma variavel para armazenar o arquivo .MP4
                    mp3_path = os.path.join (path, os.path.splitext(file)[0] + ".mp3") # Variavel que cria o nome do arquivo e adiciona .MP3 ao final
                    new_file = mp.AudioFileClip(mp4_path)  #Cria o arquivo de acordo com o tipo
                    new_file.write_audiofile(mp3_path)     #Renomeia o arquivo, setando o nome criado anteriormente
                    os.remove(mp4_path)                    #Remove o arquivo .MP4; desetivar linha permite salvar o audio e video do mesmo video ao mesmo tempo

    def tratamentolink(link):
        status = False
        if "https://www.youtube.com/" not in link:
            sg.PopupOK("Invalid link! Enter again.")
        else:
            status = True
            return status
        
        
    def tratamentopath(path):
        status = os.path.lexists(path)
        if status == False:
            sg.PopupOK("Invalid Path! Enter again.")
        else:
            return status

# ÁREA TESTES #

link = "https://www.youtube.com/watch?v=GJ0mO8P37Eg&list=PL8rzbbiOVga3DXDBO0FdocjPp3r65sgKn&index=1"
linkp = "https://www.youtube.com/playlist?list=PL8rzbbiOVga3DXDBO0FdocjPp3r65sgKn"
path = "Documentos/ProjetoFinal/"

#IndividualDownload(link,path).downloadVideo()
#IndividualDownload(link,path).downloadAudio()
#conversor(path)
#PlaylistDownload(linkp,path).downloadAllVideos()
#PlaylistDownload(linkp,path).downloadAllTracks()
#conversor(path)