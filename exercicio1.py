print('Bem-Vindo a Loja do Kalil Jaques Fakhouri')

while True:

    # VALIDAÇÃO DA CAPTURA DE VALOR E QUANTIDADE
    try:
        valorProduto = int(input('Entre com o valor do produto:'))
        quantidadeProduto = int(input('Entre com a quantidade de produtos:'))

    # TRATAMENTO DA EXCEPTION
    except ValueError:
        print('Valor inválido!')
        continue

    # CONDICIONAIS PARA VERIFICAR FRETE DE ACORDO COM QUANTIDADE DE PRODUTO
    if(0 <= quantidadeProduto < 11):
        valorFrete = 30
    elif(11 <= quantidadeProduto < 101):
        valorFrete = 60
    elif(101 <= quantidadeProduto < 1001):
        valorFrete = 120
    else:
        valorFrete = 240

    # VALOR FINAL
    print('O valor sem frete foi de: R${:.2f}'.format(valorProduto*quantidadeProduto))
    print('O valor com o frete foi de: R${:.2f} (frete de R${:.2f})'.format(valorProduto*quantidadeProduto+valorFrete, valorFrete))