import logar


def cadastrar():
    print("*"*60)
    print("Bem vindo ao nosso sistema!")
    print('Vamos realizar seu cadastro! ')
    acesso = int(input('Digite (1) confirmar para CADASTRAR -- Digite (0) para VOLTAR \n'))

    if acesso == 1:
        print("-"*60)
        print('Vamos fazer seu cadastro! ')
        usuario = (input('Digite seu usuario: '))
        senha = (input('Digite sua senha: '))

        a = open('cadastro_usuario.txt', 'a')
        a.write(usuario)
        a.write(';')
        a.write(senha)
        a.write('\n')
        a.close()
        print('Cadastro Realizado com sucesso ')
        logar.acessar()
    if acesso == 0:
        print('Saindo do cadastro! ')
        logar.acessar()
    else:
        print('')


if __name__ == '__main__':
    cadastrar()
