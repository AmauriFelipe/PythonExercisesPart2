pessoa = {}

pessoa['nome'] = str(input('Nome: '))
pessoa['media'] = float(input('Média: '))

if pessoa['media'] >= 7:

    pessoa['situacao'] = 'aprovado'

else:

    pessoa['situacao'] = 'reprovado'

for c, v in pessoa.items():
    print('{} = {}'.format(c, v))
