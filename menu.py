from videos import *
#pip install PySimpleGUI
import PySimpleGUI as sg

layout = [[sg.Text('Url de origem:'), sg.InputText()], #primeira linha
        [sg.Text('Pasta de destino:'), sg.InputText(), sg.FolderBrowse()], #segunda linha
        [sg.Button('Download Video'), sg.Button('Download Audio'), sg.Button('Cancel')]] #terceira linha
janela = sg.Window("MEDIA DOWNLOADER", layout=layout, finalize=True)
janela2 = None

     
while True:
    window, event, values = sg.read_all_windows()
    
    # TRATAMENTO DE SAíDA #
    if event == sg.WIN_CLOSED or event == 'Cancel': # se usuário fechar a janela ou pressionar cancel
        break
    #---------------------#
    
    # TRATAMENTO DE VIDEO #
    if window==janela:

        elink = tratamentolink(values[0])
        epath = tratamentopath(values[1])

        audio=False
        video=False

        if event == 'Download Video':
            if elink == True and epath == True:
                if "playlist" in values[0]:
                    link=values[0]
                    path=values[1]
                    print(values[0], values[1])
                    janela2 = PlaylistDownload(values[0], values[1]).setJanela()
                    janela.hide()
                    video=True
                else:
                    IndividualDownload(values[0], values[1]).downloadVideo()
                    sg.PopupOK('Download completed successfully!!')
                    values[0]=''
                    values[1]=''
    #---------------------#
        
    # TRATAMENTO DE AUDIO #
        if event == 'Download Audio':
            if elink == True and epath == True:
                if "playlist" in values[0]:
                    link=values[0]
                    path=values[1]
                    janela2 = PlaylistDownload(values[0], values[1]).setJanela()
                    janela.hide()
                    audio=True
                else:
                    IndividualDownload(values[0], values[1]).downloadAudio()
                    sg.PopupOK('Download completed successfully!!')
                    values[0]=''
                    values[1]=''
    #---------------------#

    # JANELA DE SELEÇÃO #
    if window==janela2:
        if event=='Voltar':
            janela2.hide()
            janela2=None
            audio=False
            video=False
            janela.un_hide()

        if event=='Ok':
            selecionados=[]
            for chave, valor in values.items():
                if valor==True:
                    selecionados.append("https://www.youtube.com/watch?v="+chave)
            print(selecionados)
            if audio:
                PlaylistDownload(link, path).downloadAllTracks(selecionados)
            elif video:
                PlaylistDownload(link, path).downloadAllVideos(selecionados)
            janela2.hide()
            janela2=None
            audio=False
            video=False
            sg.PopupOK('Download completed successfully!!')
            janela.un_hide()
janela.close()