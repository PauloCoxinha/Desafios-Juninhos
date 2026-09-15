


def cadastro():
    print("Olá, por favor cadastre o seu usuário e sua senha")
    usuario = input("Digite o seu usuário: ")
    senha = input("Digite a sua senha: ")
    return usuario, senha

cadastrar = cadastro()


def login(a, b):
    tentativas = 0
    tentativa_login_user = ''
    tentativa_login_password = ''
    
    while tentativas <= 3:
            print("Por favor realize o login, caso erre 3 vezes o seu login vai ser bloqueado")
            tentativa_login_user = input("usuário: ")
            tentativa_login_password = input("Senha: ")
            
            


            if tentativa_login_user == a and tentativa_login_password == b:
                 print(f"LOGADO COM SUCESSO! SEJA BEM VINDO {tentativa_login_user}")
                 return

            print("Voce errou a senha ou o usuario, tente novamente.")
            tentativas = tentativas + 1

    print("Sua conta foi bloqueada pelo excesso de tentativas")

login(cadastrar[0], cadastrar[1])










            
                


    
        


logar = login()