from datetime import datetime

cadastrado = {}

cadastrado['nome'] = str(input('Nome: '))

nascimento = int(input('Ano de nascimento: '))

cadastrado['idade'] = datetime.now().year - nascimento

cadastrado['carteira'] = int(input('Carteira de trabalho (0 se não tiver): '))

if cadastrado['carteira'] != 0:
    cadastrado['contratacao'] = int(input('Ano de contratação: '))
    cadastrado['salario'] = int(input('Salário: R$'))
    cadastrado['aposentadoria'] = cadastrado['idade'] + ((cadastrado['contratacao'] + 35) - datetime.now().year)

for a, b in cadastrado.items():
    print('{} = {}'.format(a, b))
