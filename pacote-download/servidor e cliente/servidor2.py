from socket import *

HOST = '127.0.0.1'
PORTA = 5000

sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.bind((HOST, PORTA))
sockobj.listen(1)

opcao = ''
saldo = 0
logado_menu = False
while True:
#Aceita conexão do cliente
    conexao, endereco = sockobj.accept()
    print('Conectado', endereco)
    logado_menu = False
    saldo = 0
    opcao = ''
    while True:
        #Recebe informação e decodifica para string
        data = conexao.recv(1024)
        mensagem = data.decode()
        print("Cliente: ", mensagem)
        if not logado_menu:
            partes = mensagem.split(",")
            login = partes[0]
            senha = partes[1]
            logado_menu = False
            if login == '1152026200010' and senha == '12345':
                resposta = 'Sucesso'
                logado_menu = True
            else:
                resposta = 'Erro. Login ou senha incompatível.'
        else:
            partes = mensagem.split(",")
            opcao = partes[0]
            if opcao == '1':
                partes[1] = int(partes[1])
                saldo = saldo + partes[1]
                resposta = f'Novo saldo: {saldo}'
            elif opcao == '2':
                partes[1] = int(partes[1])
                if partes[1] > saldo:
                    resposta = 'Saldo insuficiente!'
                elif partes[1] <= saldo:
                    saldo = saldo - partes[1]
                    resposta = f'Novo saldo: {saldo}'
            elif opcao == '3':
                resposta = f'Saldo: {saldo}'
            elif opcao == '4':
                resposta = 'Até mais!'
        conexao.send(resposta.encode())
        if logado_menu and opcao == '4':
            break
    conexao.close()
