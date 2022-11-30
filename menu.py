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
        seletorVideo = int
    
    elif seletor==2:
        break