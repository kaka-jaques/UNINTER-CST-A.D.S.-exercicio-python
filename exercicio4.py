print('Bem-vindo ao Controle de Funcionários de Kalil Jaques Fakhouri\n',
      '*'*150)

contador = 0
funcionario = {}
funcionarios = []

def cadastrar_funcionario(id):
    global contador
    print('-' * 80)
    while True:
        try:
            funcionario['id'] = id
            funcionario['nome'] = input('Entre com o NOME:').capitalize()
            funcionario['setor'] = input('Entre com o Setor:').upper()
            funcionario['salario'] = int(input('Entre com o Salário:'))
            funcionarios.append(funcionario.copy())
            contador = contador+1
            break
        except ValueError:
            print('Valor inválido!')
            continue

def consultar_funcionarios():
    print('-' * 80)
    while True:
        print('Como deseja consultar?')
        option = int(input('1 - Consultar todos\n'
                           '2 - Consultar por ID\n'
                           '3 - Consultar por Setor\n'
                           '4 - Retornar'))
        if option == 1:
            print('-'*80)
            for e in funcionarios:
                for i,j in e.items():
                    print('{} : {}'.format(i,j))

        elif option == 2:
            print('-' * 80)
            try:
                id = input('Digite o ID do funcionário:')
                for e in funcionarios:
                    for i in e.values():
                        if i == id:
                            for i, j in e.items():
                                print('{} : {}'.format(i, j))
            except:
                print('ID não existe!')

        elif option == 3:
            print('-' * 80)
            setor = input('Entre com o Setor:')
            for e in funcionarios:
                for i in e.values():
                    if i == setor:
                        for i,j in e.items():
                            print('{} : {}'.format(i, j))
        elif option == 4:
            break




def remover_funcionario(id):
    print('-' * 80)
    funcionarios.remove(id)

while True:
    print('----------------------------------------- MENU PRINCIPAL ----------------------------------------------')

    try:
        option = input('Escolha a opção desejada:\n'
               '1 - Cadastrar Funcionário\n'
               '2 - Consultar Funcionário(s)\n'
               '3 - Remover Funcionário\n'
               '4 - Sair\n'
               '>>')

        if option == '1':
            cadastrar_funcionario(contador)
        elif option == '2':
            consultar_funcionarios()
        elif option == '3':
            remover_funcionario(int(input('Digite o ID do funcionário a ser REMOVIDO: ')))
        elif option == '4':
            break
        else:
            print('Opção Inválida!')
            continue
    except ValueError:
        print('Valor Inválido!')
        continue