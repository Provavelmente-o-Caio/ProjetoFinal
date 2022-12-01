from videos import Video
import PySimpleGUI as sg
listaVideos=[]
<<<<<<< HEAD
while True:
    print('''1 - cadastrar vídeo
2 - sair''')
    while True:
        seletor = int(input('Escolha a opção que deseja: '))
        if seletor>=1 and seletor<=2:
            break
        else:
            print('Seleção inválida')

    if seletor==1:
        link = input('Digite o link do vídeo que deseja cadastrar: ')
        listaVideos.append(Video(link))
        while True:
            print(f'Maior valor: {len(listaVideos)-1}')
            seletorVideo = int(input('Selecione o video que irá baixar: '))
            if seletorVideo<=len(listaVideos)-1:
                break
        
        while True:
            modo = input('Qual modo deseja selecionar [video/audio]').lower()
            if modo=='video' or modo=='audio':
                break
        
        if modo=='video':
            listaVideos[seletorVideo].downloadVideo()
        else:
            listaVideos[seletorVideo].downloadAudio()
    
    elif seletor==2:
        break
=======

layout = [[sg.Text('Url de origem:'), sg.InputText()], #primeira linha
        [sg.Text('Pasta de destino:'), sg.InputText(), sg.FolderBrowse()], #segunda linha
        [sg.Button('Download Video'), sg.Button('Download Audio'), sg.Button('Cancel')]] #terceira linha
janela = sg.Window("DOWNLOADER DE CRIA", layout)

    
while True:
    event, values = janela.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # se usuário fechar a janela ou pressionar cancel
        break
    elif event == 'Download Video':
        Video(values[0]).downloadVideo(values[1])
        sg.PopupOK('Download efetuado com sucesso!!')
    elif event == 'Download Audio': 
        Video(values[0]).downloadAudio(values[1])
        sg.PopupOK('Download efetuado com sucesso!!')
janela.close()
>>>>>>> testes2
