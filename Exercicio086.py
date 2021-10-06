#matriz = [[], [], [], [], [], [], [], [], []]
#c = -1
#
#for c1 in range(0, 3):
#    for c2 in range(0, 3):
#        c += 1
#        matriz[c].append(float(input('Digite um valor para {}, {}: '.format(c1, c2))))
#        matriz[:].clear()

matriz = [[0, 0, 0], [0, 0, 0,], [0, 0, 0,]]

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = float(input('Digite um valor para {}, {}: '.format(l, c)))
        matriz[:].clear()

print(matriz[0])
print(matriz[1])
print(matriz[2])
