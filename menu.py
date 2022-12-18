from videos import *
#pip install PySimpleGUI
import PySimpleGUI as sg

layout = [[sg.Text('Url de origem:'), sg.InputText()], #primeira linha
        [sg.Text('Pasta de destino:'), sg.InputText(), sg.FolderBrowse()], #segunda linha
        [sg.Button('Download Video'), sg.Button('Download Audio'), sg.Button('Cancel')]] #terceira linha
janela = sg.Window("MEDIA DOWNLOADER", layout)

     
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
                sg.PopupOK('Download completed successfully!!')
            else:
                IndividualDownload(values[0], values[1]).downloadAudio()
                sg.PopupOK('Download completed successfully!!')
    #---------------------#
janela.close()

'''''
#dados para teste
link = "https://www.youtube.com/watch?v=GJ0mO8P37Eg&list=PL8rzbbiOVga3DXDBO0FdocjPp3r65sgKn&index=1"
linkp = "https://www.youtube.com/playlist?list=PL8rzbbiOVga3DXDBO0FdocjPp3r65sgKn"
path = "Documentos/ProjetoFinal/"
'''''