import forca
import adivinhacao
import calculadora
import logar
import carregar

def escolha_APP():
    print('*'*50,)
    print('Bem vindo ')
    print('*'*50,)
    print('Escolha o seu APP!  ')
    print('(1) Forca -- (2) Adivinhacao -- (3) Calculadora -- (0) SAIR ')

    escolha = int(input('Qual o APP ? '))

    if escolha == 1:
        print('Jogando Forca')
        carregar.carregando()
        forca.jogar_forca()
    elif escolha == 2:
        print('Jogando Adivinhacao')
        carregar.carregando()
        adivinhacao.jogar_adivinhacao()
    elif escolha == 3:
        print('Abrindo Calculadora ')
        carregar.carregando()
        calculadora.calcular()
    elif escolha == 0:
        print('FECHANDO PROGRAMA!! ')
        carregar.carregando()
        logar.acessar()
    else:
        print()


if __name__ == '__main__':
    escolha_APP()

