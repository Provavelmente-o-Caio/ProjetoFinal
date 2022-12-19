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
        conversor(self.path)


class PlaylistDownload(PlaylistVideo, IndividualDownload):
    def __init__(self, link, path):
        super().__init__(link)
        self.name = self.objYTPL.title
        self.path = path+'/'+self.name

    def downloadAudio(self, url):
        YouTube(url).streams.filter(only_audio = True).first().download(self.path, filename_prefix="audio_", skip_existing= True) #removi o conversos para quando for chamar o download audio não chamar a função muitas vezes desnecessariamente
        
    def downloadAllVideos(self, selecionados):
        self.selecionados = selecionados
        for url in self.objYTPL.video_urls:
            if url in self.selecionados:
                IndividualDownload(url, self.path).downloadVideo()
    
    def downloadAllTracks(self, selecionados):
        self.selecionados = selecionados
        for url in self.objYTPL.video_urls:
            if url in self.selecionados:
                self.downloadAudio(url)
        conversor(self.path)

    def setJanela(self):
        layout = [[sg.Text(self.objYTPL.title)]]
        for video in self.objYTPL.videos:
            layout.append([sg.Checkbox(video.title, key=video.video_id, default=True)],)
        layout.append([sg.Button('Voltar'), sg.Button('Ok')])
        return sg.Window("Seleção de vídeos", layout=layout, finalize=True)

        
        
def conversor(path):
    for file in os.listdir(path):                      #For para percorrer dentro da pasta passada anteriormente
            if re.search('mp4', file) and "audio_"in file:                 #If verificando se o arquivo e .MP4                    
                mp4_path = os.path.join (path, file)   #Cria uma variavel para armazenar o arquivo .MP4
                mp3_path = os.path.join (path, os.path.splitext(file)[0] + ".mp3") # Variavel que cria o nome do arquivo e adiciona .MP3 ao final
                new_file = mp.AudioFileClip(mp4_path)  #Cria o arquivo de acordo com o tipo
                new_file.write_audiofile(mp3_path)     #Renomeia o arquivo, setando o nome criado anteriormente
                os.remove(mp4_path)                    #Remove o arquivo .MP4; desetivar linha permite salvar o audio e video do mesmo video ao mesmo tempo

def tratamentolink(link):
    if "playlist" not in link:
        try:
            YouTube(link)
        except:
            sg.PopupOK("Invalid Path! Enter again.")
        else:
            return True
    else:
        p = Playlist(link)
        for url in p.video_urls:
            try:
                YouTube(url)
            except:
                p.remove(url)
        return p
                
    
def tratamentopath(path):
    status = os.path.lexists(path)
    if status == False:
        sg.PopupOK("Invalid Path! Enter again.")
    else:
        return status


#link = "https://www.youtube.com/watch?v=GJ0mO8P37Eg&list=PL8rzbbiOVga3DXDBO0FdocjPp3r65sgKn&index=1"
#linkp = "https://www.youtube.com/playlist?list=PL8rzbbiOVga3DXDBO0FdocjPp3r65sgKn"
#teste = tratamentolink(linkp)
#print(teste)