total = 0
contador_mais_de_1000 = 0
nome_mais_barato = str('')
menor = 0
contador = 0

while True:

    print('')

    nome_produto = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o preço do produto: '))

    total += preco
    contador += 1

    if preco > 1000:
        contador_mais_de_1000 += 1
    if contador == 1:
        menor = preco
        nome_mais_barato = nome_produto
    else:
        if preco < menor:
            menor = preco
            nome_mais_barato = nome_produto

    while True:
        resposta_continuar = str(input('Deseja continuar? [S/N] '))
        if resposta_continuar in 'SsNn':
            break
    if resposta_continuar in 'Nn':
        break

print('+-'*20)
print('O total gasto na compra foi R${:.2f}.'.format(total))
print('')
print('{} produtos custam mais de R$1000,00.'.format(contador_mais_de_1000))
print('')
print('O produto mais barato é {} que custa R${:.2f}.'.format(nome_mais_barato, menor))
