from socket import *

HOST = '127.0.0.1'
PORTA = 5000

conexao = socket(AF_INET, SOCK_STREAM)
conexao.connect((HOST, PORTA))
while True:
    login = str(input('Login:')).strip()
    senha = str(input('Senha:')).strip()
    mensagem = f'{login},{senha}'
    conexao.send(mensagem.encode())
    data = conexao.recv(1024)
    mensagem_servidor = data.decode()
    print(mensagem_servidor)
    if mensagem_servidor == 'Sucesso':
        break
while True:
    print('''Digite a opção que deseja realizar:
1 - Depositar
2 - Sacar
3 - Saldo
4 - Sair''')
    opcao = str(input('Opção:')).strip()
    if opcao not in ['1', '2', '3', '4']:
        print('Opção inválida. Tente novamente.')
        continue
    elif opcao == '1':
        depositar = str(input('Quanto deseja depositar:'))
        mensagem_para_servidor = f'{opcao},{depositar}'
    elif opcao == '2':
        sacar = str(input('Quanto deseja sacar:'))
        mensagem_para_servidor = f'{opcao},{sacar}'
    elif opcao == '3':
        mensagem_para_servidor = opcao
    elif opcao == '4':
        mensagem_para_servidor = opcao
    conexao.send(mensagem_para_servidor.encode())
    data = conexao.recv(1024)
    mensagem_servidor = data.decode()
    print(mensagem_servidor)
    if opcao == '4':
        break
conexao.close()