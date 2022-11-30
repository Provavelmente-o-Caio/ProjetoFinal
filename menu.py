from videos import Video

listaVideos=[]
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