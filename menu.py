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
    
   
    
    #-----------------------#
    
    # TRATAMENTO DE VIDEO #
    match event:
            case "Download Video":
                if "playlist" in values[0]:
                    validatorlinkp, validatorpath = Validators(values[0], values[1]).validator_playlistlink(), Validators(values[0], values[1]).validator_path()
                    if validatorlinkp == True and validatorpath == True:
                        PlaylistDownload(values[0], values[1]).downloadAllVideos()
                        sg.PopupOK('Download completed successfully!!')
                else:
                    validatorlinkI, validatorpath = Validators(values[0], values[1]).validator_individuallink(), Validators(values[0], values[1]).validator_path()
                    if validatorlinkI == True and validatorpath == True:    
                        IndividualDownload(values[0], values[1]).downloadVideo()
                        sg.PopupOK('Download completed successfully!!')
    #---------------------#
    
    # TRATAMENTO DE AUDIO #
            case "Download Audio":
                if "playlist" in values[0]:
                    validatorlinkp, validatorpath = Validators(values[0], values[1]).validator_playlistlink(), Validators(values[0], values[1]).validator_path()
                    if validatorlinkp == True and validatorpath == True:
                        PlaylistDownload(values[0], values[1]).downloadAllTracks()
                        sg.PopupOK('Download completed successfully!!')
                else:
                    validatorlinkI, validatorpath = Validators(values[0], values[1]).validator_individuallink(), Validators(values[0], values[1]).validator_path()
                    if validatorlinkI == True and validatorpath == True:
                        IndividualDownload(values[0], values[1]).downloadAudio()
                        sg.PopupOK('Download completed successfully!!')
    #---------------------#
janela.close()