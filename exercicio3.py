print('Bem-vindo ao Programa de Serviços de Limpeza de Kalil Jaques Fakhouri\n',
      '*'*120)



#Inicio da função metragem_limpeza()
def metragem_limpeza():
    while True:
        try:
            print('---------------------------------------- Menu 1 de 3 - Metragem Limpeza ----------------------------------------')
            metragem = int(input('Entre com a metragem da casa:'))

            if(30 <= metragem < 300):
                print('É necessário contratar 1 pessoa!')
                return 60 + 0.3 * metragem
            elif(300 <= metragem < 700):
                print('É necessário contratar 2 pessoa!')
                return 120 + 0.5 * metragem
            else:
                print('!! Não aceitamos casa com metragem menor de 30m² ou maior de 700m² !!')
                continue

        except ValueError:
            print('Valor inválido! Tente novamente')
            continue
#Fim da função metragem_limpeza()

#Inicio da função tipo_limpeza()
def tipo_limpeza():
    while True:
        print('---------------------------------------- Menu 2 de 3 - Tipo de Limpeza ----------------------------------------')
        tipo = input('Entre com o tipo de limpeza:\n'
                     'B - Básica - Indicada para sujeiras semanais ou quinzenais\n'
                     'C - Completa - Indicada para sujeiras antigas e/ou não rotineiras\n'
                     '>>').upper()
        if(tipo == 'B'):
            return 1.0
        elif(tipo == 'C'):
            return 1.3
        else:
            print('Opção Inválida!')
            continue
#Fim da função tipo_limpeza()

#Inicio da função adicional_limpeza()
def adicional_limpeza():

    valor_adicional = 0

    while True:
        try:
            print('---------------------------------------- Menu 3 de 3 - Adicional Limpeza ----------------------------------------\n')
            adicional = int(input('Deseja mais alguma coisa?\n'
                                        '0 - Encerrar\n'
                                        '1 - Passar 10 peças de roupas - R$ 10.00\n'
                                        '2 - Limpeza de 1 Forno/Micro-ondas - R$ 12,00\n'
                                        '3- Limpeza de 1 Geladeira/Freezer - R$ 20,00\n'
                                        '>>'))
            if(adicional == 0):
                return valor_adicional
            elif(adicional == 1):
                valor_adicional = valor_adicional + 10
            elif(adicional == 2):
                valor_adicional = valor_adicional + 12
            elif(adicional == 3):
                valor_adicional = valor_adicional + 20
            else:
                print('Opção Inválida!')
                continue

        except ValueError:
            print('Valor inválido!')

# Fim da função adicional_limpeza()

# Inicio da Main
valor_metro = metragem_limpeza()

valor_tipo = tipo_limpeza()

valor_adicional = adicional_limpeza()

print('*'*120,
      '\nTOTAL: R$',(valor_adicional + valor_metro * valor_tipo),'(metragem: R$',valor_metro,' * tipo:',valor_tipo,' + adicional: R$',valor_adicional,')\n',
      '*'*120)