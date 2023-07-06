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