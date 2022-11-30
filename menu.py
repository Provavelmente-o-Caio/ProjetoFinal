from videos import Video
import PySimpleGUI as sg
listaVideos=[]

layout = [[sg.Text('Url de origem:'), sg.InputText()], #primeira linha
        [sg.Button('Download'), sg.Button('Cancel')]] #segunda linha

janela = sg.Window("DOWNLOADER DE CRIA", layout)

    
while True:
    event, values = janela.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # se usuário fechar a janela ou pressionar cancel
        break
    elif event == 'Download': 
        Video.downloadAudio(values[0])
        sg.PopupOK('Download efetuado com sucesso!!')
janela.close()