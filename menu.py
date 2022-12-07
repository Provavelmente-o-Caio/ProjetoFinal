from videos import Video
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
    if event == sg.WIN_CLOSED or event == 'Cancel': # se usuário fechar a janela ou pressionar cancel
        break
    elif event == 'Download Video':
        Video(values[0]).downloadVideo(values[1])
        sg.PopupOK('Download completed successfully!!')
    elif event == 'Download Audio': 
        Video(values[0]).downloadAudio(values[1])
        sg.PopupOK('Download completed successfully!!')
janela.close()
