# Desafio 2 - Curso Python - DIO :books:

Atualizar o código do Desafio 1, acrescentando novas funções e alterando forma de construção do código.

###### Objetivos:

- Separar as funções existentes de saque, depósito e extrato em funções modularizadas.
- Criar três novas funções:
  * Cadastrar usuário (cliente)
  * Cadastrar conta bancária e vincular ao usuário.
  * Apresentar lista de contas cadastrastradas

###### Regras

Saque:

- Utilizar argumentos keyword only. (*, saque, saldo, limite_qtde_saque, etc)

Depósito:

* Utilizar argumentos positional only. (saldo, deposito, extrato, /)

  Extrato:

* Utilizar argumentos positional olny e keyword only. (saques_realizados, extrato, saldo=saldo)

###### Novas funções:

* Criar usuário (cliente) :

  * Armazenar os dados em uma lista. (nome, dt_nascimento, cpf e endereço)
  * Não permitir o cadastros de dois usuários com mesmo CPF.

* ###### Nova conta:

  * Armazenar as contas em uma lista (agencia, numero da conta e usuário).
  * Agência fixa em 0001
  * Conta sequencial iniciando em 1
  * O usuário pode ter mais de uma conta e a mesma de titularidade única

* Exibir contas:

  * Exibir as informações armazenadas para as contas criadas.

  

