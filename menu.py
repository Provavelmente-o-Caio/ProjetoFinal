from videos import *
#pip install PySimpleGUI
import PySimpleGUI as sg


opt = ['mp3', 'mp4']
layout = [
        [sg.Text('Url de origem:', size=(15,1)), sg.InputText(size=(50,1))], #primeira linha
        [sg.Text('Pasta de destino:', size=(15,1)), sg.InputText(size=(40,1)), sg.FolderBrowse(size=(5,1))], #segunda linha
        [sg.Text('Perfil de Saída:', size=(15,1)), sg.Text('Nome do arquivo', size=(40,1)),sg.DD(opt, size=(5,1))], #terceira linha
        [sg.Button('Cancel', size=(5,1))]
]
janela = sg.Window("C & C DOWNLOADER", layout)

     
while True:
    event, values = janela.read()
    
    # TRATAMENTO DE SAíDA #
    if event == sg.WIN_CLOSED or event == 'Cancel': # se usuário fechar a janela ou pressionar cancel
        break
    #---------------------#
    
    # TRATAMENTO DE ENTRADA #
    
    elink = tratamentolink(values[0])
    epath = tratamentopath(values[1])
    
    #-----------------------#
    
    # TRATAMENTO DE VIDEO #
    if event == 'Download Video':
        if elink == True and epath == True:
            pass
            if "playlist" in values[0]: 
                PlaylistDownload(values[0], values[1]).downloadAllVideos()
                sg.PopupOK('Download completed successfully!!')
            else:
                IndividualDownload(values[0], values[1]).downloadVideo()
                sg.PopupOK('Download completed successfully!!')
    #---------------------#
    
    # TRATAMENTO DE AUDIO #
    elif event == 'Download Audio':
        if elink == True and epath == True:
            pass
            if "playlist" in values[0]: 
                PlaylistDownload(values[0], values[1]).downloadAllTracks()
                conversor(values[1])
                sg.PopupOK('Download completed successfully!!')
            else:
                IndividualDownload(values[0], values[1]).downloadAudio()
                conversor(values[1])
                sg.PopupOK('Download completed successfully!!')
    #---------------------#
janela.close()

'''''
#dados para teste
link = "https://www.youtube.com/watch?v=GJ0mO8P37Eg&list=PL8rzbbiOVga3DXDBO0FdocjPp3r65sgKn&index=1"
linkp = "https://www.youtube.com/playlist?list=PL8rzbbiOVga3DXDBO0FdocjPp3r65sgKn"
path = "Documentos/ProjetoFinal/"
'''''