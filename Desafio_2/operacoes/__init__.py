from python_developer.Desafio_2.formatacao import linhasep, titulo


titulo('BEM VINDO AO BANCO XYZ')


def menu():
    opc = int(input('''    Selecione a opção desejada:
    1 - Sacar
    2 - Depositar
    3 - Extrato
    4 - Nova conta
    5 - Listar contas
    6 - Novo usuário
    7 - Sair
    Informe opção: '''))
    return opc


def sacar(*, saque, saldo, limite_qtde_saque, limite_valor_saque, extrato, saques_realizados):
    """Função para validar as condições de saque como saldo suficiente e limite de saque diário, atualiza o saldo e
    fornece informação necessária para popular o extrato caso a operação seja realizada com sucesso.
    :param saque: Recebo o valor solicitado para saque.
    :param saldo: Recebo o valor do saldo atual em conta.
    :param limite_qtde_saque: Recebo parâmetro do limite determinado para saques dia.
    :param limite_valor_saque: Recebo parâmetro do valor de saque diário.
    :param extrato: Informação do parâmetro onde será armazenado o valor a ser adicionado a lista extrato.
    :param saques_realizados: Valor de saques realizados no dia. Se dentro do permitido, adiciona mais um.
    :return: Retorna o valor do saldo atulizado já descontando o saque, adiciona um ao limite de saque diário e os
    valores desta operação para serem adicionadas a lista extrato.
    """
    saldo_insuficiente = saque > saldo
    excedeu_valor = saque > limite_valor_saque
    excedeu_num_saque = saques_realizados >= limite_qtde_saque
    if excedeu_valor:
        print(f'*** Valor excede o limite para saque de R$ {limite_valor_saque:.2f} .***.'.center(60))
        linhasep()
    elif saldo_insuficiente:
        print(f'*** Saldo insuficiênte para operação. ***'.center(60))
        linhasep()
    elif excedeu_num_saque:
        print(f'*** Quantidade de saques diário excedida. *** "{limite_qtde_saque}".'.center(60))
        linhasep()
    elif saque > 0:
        print(f'=== Saque de R$ {saque:.2f} realizado com sucesso. ==='.center(60))
        linhasep()
        saldo -= saque
        saques_realizados += 1
        extrato.append({'tipo': 'SAQUE', 'valor': saque})
    return saldo, extrato, saques_realizados


def depositar(saldo, deposito, extrato, /):
    """Função para realizar o depósito em conta. Recebe valor do depósito se positivo, adiciona ao saldo do cliente.
    Retorna o saldo atulizado e informação para popular o extrato caso a operação seja realizada com sucesso.
    :param saldo: Recebe o saldo atual da conta.
    :param deposito: Recebe o valor que está sendo depositado.
    :param extrato: Informação do parâmetro onde será armazenado o valor a ser adicionado a lista extrato.
    :return: Retorna o saldo atualizado e informações para lista extrato.
    """
    if deposito > 0:
        print(f'=== Valor de R$ {deposito:.2f} depositado com sucesso. ==='.center(60))
        extrato.append({'tipo': 'DEPÓSITO', 'valor': deposito})
        saldo += deposito
        linhasep()
    else:
        print('*** Informe um valor válido para depósito. ***'.center(60))
    return saldo, extrato


def exibe_extrato(saques_realizados, extrato, *, saldo):
    """ Exibe as operações de saque, depósito, saldo em conta, total depositado e sacado e número de saques.
    :param saques_realizados: Recebe o valor de saques realizados.
    :param extrato: Informação do parâmetro onde será armazenado o valor a ser adicionado a lista extrato.
    :param saldo: Recebe o valor do saldo para exibição.
    :return: Retorna a impressão da lista extrato com todas as movimentações em conta.
    """
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


def cria_usuario(usuarios):
    titulo('CADASTRO DE USUÁRIO')
    cpf = input('Informe o número do seu CPF (sem pontuação): ')
    linhasep()
    usuario = filtrar_usuarios(cpf, usuarios)
    if usuario:
        print(f'*** Cadastro já existe com este CPF {cpf} ***'.center(60))
        linhasep()
        return
    nome = input('Nome completo: ')
    data_nascimento = input('Data de nascimento dd-mm-aaaa: ')
    endereco = input('Informe o endereço (Logradouro, N.º, Bairro, Cidade, UF): ')
    usuarios.append({'nome': nome, 'cpf': cpf, 'data_nascimento': data_nascimento, 'endereco': endereco})
    linhasep()
    print('=== Usuário cadastrado com sucesso! ==='.center(60))
    linhasep()
    return usuarios


def filtrar_usuarios(cpf, usuarios):
    """Filtra a lista de usuários com base no CPF informado.
    :param cpf: CPF a ser filtrado.
    :param usuarios: Lista de usuários.
    :return: O dicionário de usuário correspondente ao CPF informado, ou None se não encontrado.
    """
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            return usuario
    else:
        return None


def criar_conta(agencia, numero_conta, usuarios, contas):
    """Cria uma nova conta bancária para um usuário.
    :param agencia: Número da agência da conta.
    :param numero_conta: Número da conta.
    :param usuarios: Lista de usuários existentes.
    :param contas: Lista de contas existentes.
    :return: A lista de contas atualizada com a nova conta criada.
    """
    titulo('NOVA CONTA')
    cpf = input('Informe o CPF (sem pontuação): ')
    linhasep()
    usuario = filtrar_usuarios(cpf, usuarios)
    if usuario:
        print('=== Conta criada com sucesso! ==='.center(60))
        linhasep()
        contas.append({'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario})
        return contas
    linhasep()
    print('*** Usuário não encontrado. Criação interrompida! ***'.center(60))
    linhasep()


def listar_contas(contas):
    titulo('CONTAS CADASTRADAS')
    """Exibe as contas cadastradas.
    :param contas: Lista de contas cadastradas.
    """
    if not contas:
        print('*** Nenhuma conta cadastrada! ***'.center(60))
        linhasep()
    else:
        for conta in contas:
            for chave, valor in conta.items():
                if isinstance(valor, dict):  # Verifica se o valor é um dicionário
                    for sub_chave, sub_valor in valor.items():
                        print(f'{sub_chave:<17}{sub_valor:<18}')
                else:
                    print(f'{chave:<17}{valor:<18}')
            print()
            linhasep()


def principal():
    """Função principal que executa o programa do sistema bancário.
    - Inicializa variáveis e configurações iniciais.
    - Exibe um menu de opções para o usuário.
    - Executa as operações de acordo com a opção selecionada.
    - Chama as funções correspondentes a cada operação.
    - Encerra o programa quando a opção de sair é escolhida.
    """
    AGENCIA = '0001'
    saldo = 500
    LIMITE_QTDE_SAQUE = 3
    limite_valor_saque = 500
    extrato = list()
    saques_realizados = 0
    usuarios = list()
    contas = list()

    while True:
        opcao = menu()
        if opcao == 1:
            titulo('SAQUE')
            saque = float(input('Informe o valor do saque: '))
            linhasep()
            saldo, extrato, saques_realizados = sacar(
                saque=saque,
                saldo=saldo,
                limite_qtde_saque=LIMITE_QTDE_SAQUE,
                limite_valor_saque=limite_valor_saque,
                extrato=extrato,
                saques_realizados=saques_realizados)
        elif opcao == 2:
            titulo('DEPOSITO')
            deposito = float(input('Qual o valor do deposito: '))
            linhasep()
            saldo, extrato = depositar(saldo, deposito, extrato)
        elif opcao == 3:
            titulo('EXTRATO', '=')
            exibe_extrato(saques_realizados, extrato, saldo=saldo)
        elif opcao == 4:
            numero_conta = len(contas) + 1
            criar_conta(AGENCIA, numero_conta, usuarios, contas)
        elif opcao == 5:
            listar_contas(contas)
        elif opcao == 6:
            cria_usuario(usuarios)
        elif opcao == 7:
            titulo('ENCERRADO COM SUCESSO. VOLTE SEMPRE')
            break
        else:
            linhasep()
            print('*** Opção inválida. Tente novamente! ***'.center(60))
            linhasep()