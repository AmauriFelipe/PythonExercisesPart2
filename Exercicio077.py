lista_palavras = ('Sódio', 'Potássio', 'Magnésio', 'Carbono',
            'Hidrogênio', 'Nitrogênio', 'Oxigênio', 'Cloro',
            'Iodo', 'Enxofre')

for palavra in lista_palavras:
    print('\nNa palavra {} temos: '.format(palavra), end = (''))
    for letra in palavra:
        if letra.lower() in 'aáãâ eé ií oó uú':
            print(letra, end = (' '))
