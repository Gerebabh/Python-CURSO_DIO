def linhasep(sinal='-', carac=60):
    """
    Gera uma linha para separação do de blocos conforme formatação e tamanho escolhido
    :param sinal: Caractere que será utilizado para geração da linha.
    :param carac: quantidade de caracteres
    """
    print(sinal * carac)


def titulo(txt='', sinal='='):
    """
    Formatação de titulos.
    :param txt: Texto do titulo.
    :param sinal: Sinal das linhas de borda superior e inferior.
    """
    print(sinal * 60)
    print(txt.center(60))
    print(sinal * 60)


titulo('BEM VINDO AO BANCO XYZ')
menu = ('''    Selecione a opção desejada:
    1 - Sacar
    2 - Depositar
    3 - Extrato
    4 - Sair
    Informe opção: ''')

saldo = 500
LIMITE_QTDE_SAQUE = 3
limite_valor_saque = 500
extrato = list()
saques_realizados = 0

while True:
    opcao = int(input(menu))
    if opcao == 1:
        titulo('SAQUE')
        saque = float(input('Informe o valor do saque: '))
        linhasep()
        saldo_insuficiente = saque > saldo
        excedeu_valor = saque > limite_valor_saque
        excedeu_num_saque = saques_realizados >= LIMITE_QTDE_SAQUE
        if excedeu_valor:
            print(f'*** Valor excede o limite para saque de R$ {limite_valor_saque:.2f} .***.'.center(60))
            linhasep()
        elif saldo_insuficiente:
            print(f'*** Saldo insuficiênte para operação. ***'.center(60))
            linhasep()
        elif excedeu_num_saque:
            print(f'*** Quantidade de saques diário excedida. *** "{LIMITE_QTDE_SAQUE}".'.center(60))
            linhasep()
        elif saque > 0:
            print(f'=== Saque de R$ {saque:.2f} realizado com sucesso. ==='.center(60))
            linhasep()
            saldo -= saque
            saques_realizados += 1
            extrato.append({'tipo': 'SAQUE', 'valor': saque})
    elif opcao == 2:
        titulo('DEPOSITO')
        deposito = float(input('Qual o valor do deposito: '))
        linhasep()
        if deposito > 0:
            print(f'=== Valor de R$ {deposito:.2f} depositado com sucesso. ==='.center(60))
            extrato.append({'tipo': 'DEPÓSITO', 'valor': deposito})
            saldo += deposito
            linhasep()
        else:
            print('*** Informe um valor válido para depósito. ***'.center(60))
    elif opcao == 3:
        titulo('EXTRATO', '=')
        print(f'Saques realizados no dia: {saques_realizados}')
        tot_saque = 0
        tot_deposito = 0
        for transacao in extrato:
            tipo = transacao['tipo']
            valor = transacao['valor']
            if transacao['tipo'] == 'SAQUE':
                tot_saque += transacao['valor']
            else:
                tot_deposito += transacao['valor']
            print(f'*{tipo:<10} -   R${valor:9.2f}')
        linhasep()
        print(f'Total sacado R$ {tot_saque:.2f}. Total depositado R$ {tot_deposito:.2f}.')
        linhasep()
        print(f'Seu saldo atual é de R$ {saldo:.2f}.')
        linhasep()
    elif opcao == 4:
        titulo('ENCERRADO COM SUCESSO. VOLTE SEMPRE')
        break
    else:
        linhasep()
        print('*** Opção inválida. Tente novamente! ***'.center(60))
        linhasep()
