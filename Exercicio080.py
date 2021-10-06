lista = []

for a in range(0, 5):
    n = int(input('Digite um valor inteiro: '))
    if a == 0 or n > lista[-1]:
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                break
            pos += 1

print('')
print(lista)
