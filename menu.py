from videos import Video
import PySimpleGUI as sg

layout = [[sg.Text('Url de origem:'), sg.InputText()], #primeira linha
        [sg.Text('Pasta de destino:'), sg.InputText(), sg.FolderBrowse()], #segunda linha
        [sg.Button('Download Video'), sg.Button('Download Audio'), sg.Button('Cancel')]] #terceira linha
janela = sg.Window("MEDIA DOWNLOADER", layout)

    
while True:
    event, values = janela.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # se usuário fechar a janela ou pressionar cancel
        break
    elif event == 'Download Video':
        Video(values[0]).downloadVideo(values[1])
        sg.PopupOK('Download completed successfully!!')
    elif event == 'Download Audio': 
        Video(values[0]).downloadAudio(values[1])
        sg.PopupOK('Download completed successfully!!')
janela.close()
