expressao = str(input('Digite sua expressão: '))
print('')

pilha = list()

for simbolo in expressao:
    if simbolo == '(':
        pilha.append(simbolo)

    elif simbolo == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(simbolo)

if len(pilha) == 0:
    print('Sua expressão está correta.')
else:
    print('Sua expressão está errada.')
