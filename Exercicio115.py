from Ex115.Formatacaodetexto import *
from Ex115.arquivo import *


arq = 'cursoemvideo.txt'

if arquivoExiste(arq):
    print('Arquivo encontrado com sucesso.')
else:
    print('Arquivo não encontrado.')

    criarArquivo(arq)

while True:
    op = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])

    if op == 1:
        print('Opção 1')
        lerArquivo(arq)

    elif op == 2:
        print('Opção 2')

    elif op == 3:
        print('Encerrando programa...')

        break

    else:
        print('''\033[1;31;mResposta inválida.
Por favor, escolha uma opcão entre 1 e 3.\033[m''')
