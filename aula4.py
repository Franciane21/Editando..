#  sistema bancario com tuplas -  lista  -  dicionários


def banco():
    banco_dados = {'valores':[]}

    # CADASTRO NO BANCO

    nome = input('Nome:')
    idade = int(input('Idade: '))
    senha = input('Senha: ')
    login = input('e-mail')

    banco_dados['nome']  = nome
    banco_dados['idade'] = idade
    banco_dados['login'] = login
    banco_dados['senha'] = senha

    
    return banco_dados


def sistema_banco(saldo):
  sis = input('Deseja acessar? ')
  while sis == 'sim':  
    banco_dados = banco()
    print('Digite senha e login para acessar: ')
    senha_input = input('Senha: ')
    login_input = input('Login: ')

    if banco_dados['senha'] == senha_input and banco_dados['login'] == login_input:
       print('Logado no banco Z') 

       escolha = input(f'''
                 Olá {banco_dados['nome']}
                 escolha a operação:

                 1 -  Saque
                 2 -  Deposito
                 3 -  Extrato''')


       if escolha == '1':  
          saque = float(input('Saque: '))   
          cal = saldo - saque
          banco_dados['valores'].append(cal)
          soma =  sum(banco_dados['valores'])
          print('R$',saque)
          print('R$',soma)
          sis = input('Deseja continuar? ')

       elif escolha  == '2':
          deposito = float(input('deposito: '))   
          cal = saldo + deposito
          print('R$',cal)  
          sis = input('Deseja continuar? ') 
       elif escolha  == '3':
           print('R$', saldo) 
           sis = input('Deseja continuar? ')                  
       else:
           print('Digite algo válido! ')
    else:
        print('Dados incorretos')



sistema_banco(5000.0)