from videos import Video
listaVideos=[]
while True:
    print('''1 - cadastrar vídeo
2 - baixar vídeo
3 - sair''')
    while True:
        seletor = int(input('Escolha a opção que deseja: '))
        if seletor>=1 and seletor<=3:
            break

    if seletor==1:
        link = input('Digite o link do vídeo que deseja cadastrar: ')
        listaVideos.append(Video(link))
        
    elif seletor==2:
        listaVideos[0].downloadAudio()
    
    elif seletor==3:
        break