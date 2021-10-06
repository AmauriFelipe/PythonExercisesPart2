frase = str(input('Escreva uma frase pra detectar se ela é um palíndromo: ')).strip().upper()
separa = frase.split()
junto = ''.join(separa)
inverso = junto[::-1]
print('')
#for letra in range(len(junto) - 1, -1, -1):
#    inverso += junto[letra]
print('Você digitou a frase: ', end = (''))
print(junto)
print('Essa frase ao contrário é: ', end = (''))
print(inverso)
print('')
if junto == inverso:
    print('Essa frase é um palíndromo.')
else:
    print('Essa frase não é um palíndromo.')