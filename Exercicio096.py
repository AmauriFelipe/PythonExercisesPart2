def area(l, c):
    a = l * c
    print('Um terreno com as dimensões {}m e {}m mede {}m².'.format(l, c, a))


area(int(input('Largura do terreno: ')),
     int(input('Comprimento do terreno: ')))
