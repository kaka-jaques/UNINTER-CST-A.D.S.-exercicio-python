print('Bem-Vindo a Sorveteria de Kalil Jaques Fakhouri')

valorTotal = 0

print('-------------------------------------------------Cardápio-------------------------------------------------\n'
      '|  Código  |  Descrição              |  Tamanho P (500ml)  |  Tamanho M (1000ml)  |  Tamanho G (2000ml)  |\n'
      '|    TR    |  Sabores Tradicionais   |       R$ 6,00       |        R$ 10,00      |       R$ 18,00       |\n'
      '|    ES    |  Sabores Especiais      |       R$ 7,00       |        R$ 12,00      |       R$ 21,00       |\n'
      '|    PR    |  Sabores Premium        |       R$ 8,00       |        R$ 14,00      |       R$ 24,00       |\n'
      '----------------------------------------------------------------------------------------------------------')

while True:
    try:
        tamanho = input('Entre com o TAMANHO do pote desejado (P/M/G):').upper() # .upper() PARA CAPITALIZAR TUDO EVITANDO ERRO NAS CONDICIONAIS
        codigo = input('Entre com o CÓDIGO do sabor desejado (TR/ES/PR):').upper()

    except ValueError:
        print('Valor inválido! Tente novamente')
        continue

    # ADICIONANDO O VALOR AO TOTAL DE ACORDO COM O CÓDIGO E TAMANHO
    if (tamanho == 'P'):
        if (codigo == 'TR'):
            valorTotal = valorTotal + 6
            print('Você pediu um sorvete sabor TRADICIONAL P de R$ 6,00 \n'
                  '-------------------------------------------------------------------')
        elif (codigo == 'ES'):
            valorTotal = valorTotal + 7
            print('Você pediu um sorvete sabor ESPECIAL P de R$ 7,00  \n'
                  '-------------------------------------------------------------------')
        elif (codigo == 'PR'):
            valorTotal = valorTotal + 8
            print('Você pediu um sorvete sabor PREMIUM P de R$ 8,00  \n'
                  '-------------------------------------------------------------------')
        else:
            print('CÓDIGO INVÁLIDO!')
            continue
    elif (tamanho == 'M'):
        if (codigo == 'TR'):
            valorTotal = valorTotal + 10
            print('Você pediu um sorvete sabor TRADICIONAL M de R$ 10,00  \n'
                  '-------------------------------------------------------------------')
        elif (codigo == 'ES'):
            valorTotal = valorTotal + 12
            print('Você pediu um sorvete sabor ESPECIAL M de R$ 12,00 \n'
                  '-------------------------------------------------------------------')
        elif (codigo == 'PR'):
            valorTotal = valorTotal + 14
            print('Você pediu um sorvete sabor PREMIUM M de R$ 14,00 \n'
                  '-------------------------------------------------------------------')
        else:
            print('CÓDIGO INVÁLIDO!')
            continue
    elif (tamanho == 'G'):
        if (codigo == 'TR'):
            valorTotal = valorTotal + 18
            print('Você pediu um sorvete sabor TRADICIONAL G de R$ 18,00\n'
                  '-------------------------------------------------------------------')
        elif (codigo == 'ES'):
            valorTotal = valorTotal + 21
            print('Você pediu um sorvete sabor ESPECIAL G de R$ 21,00  \n'
                  '-------------------------------------------------------------------')
        elif (codigo == 'PR'):
            valorTotal = valorTotal + 24
            print('Você pediu um sorvete sabor PREMIUM G de R$ 24,00 \n'
                  '-------------------------------------------------------------------')
        else:
            print('CÓDIGO INVÁLIDO!')
            continue
    else:
        print('TAMANHO INVÁLIDO!')
        continue

    resume = input('Deseja pedir mais alguma coisa? (S/N)').upper()

    if(resume == 'S'):
        continue
    else:
        print('Obrigado por comprar aqui! Volte sempre!\n'
              'Valor total final: R$ {:.2f}'.format(valorTotal))
        break