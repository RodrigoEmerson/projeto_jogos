import time

import cadastro
import jogos
import carregar


def acessar():
    print("="*80)
    print("Bem vindo ao nosso sistema de login!")
    acesso = int(input('Digite (1) para acessar -- Digite (2) para cadastrar -- Digite (0) para SAIR  \n'))

    if acesso == 1:
        arquivo = open('cadastro_usuario.txt')

        lista_usuario_senha = arquivo.readlines()

        tentativa_usuario = input("Digite seu usuario: ")
        tentativa_senha = input("Digite sua senha: ")

        for usuario_senha in lista_usuario_senha:
            usuario, senha = usuario_senha.strip().split(';')
            if tentativa_usuario == usuario and tentativa_senha == senha:
                print("Autenticacao bem sucedida!")
                carregar.carregando()
                jogos.escolha_APP()
                break
        else:
            print("""Usuario ou senha invalidos!
            """)
            acessar()

        arquivo.close()
    if acesso == 2:
        print('Abrindo cadastro! ')
        cadastro.cadastrar()

    if acesso == 0:
        print(' Finalizando App!')
        time.sleep(3)
        carregar.carregando()
        print("")
        print("""
        =============================================
        ==    APP encerrado. Obrigado por usar!    ==
        =============================================""")


if __name__ == '__main__':
    acessar()

