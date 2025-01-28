import random
import jogos


def jogar_adivinhacao():
    print('*'*50,)
    print('Bem vindo ao jogo de adivinhaçao')
    print('*'*50,)

    numero_secreto = random.randrange(1, 100)
    tentativas = 0

    print('Escolha o nivel de dificuldade: ')
    print('(1) facil -- (2) Medio -- (3) Dificil ')

    nivel = int(input('Digite o nivel: '))
    print('*'*50, '\n')

    if nivel == 1:
        tentativas = 20
    elif nivel == 2:
        tentativas = 10
    else:
        tentativas = 5

    '''print('numero secreto', numero_secreto)'''

    for rodadas in range(1, tentativas + 1):
        print(f'tentativas {rodadas} de {tentativas}')
        chute = int(input('Digite um numero: '))
        print('Voce digitou ', chute)
        print('*' * 70)

        if chute < 1:
            print('Digite um numero de 1 a 100')
            if chute > 100:
                print('Digite um numero de 1 a 100')
                continue

        acertou = chute == numero_secreto
        menor = chute < numero_secreto
        maior = chute > numero_secreto
        errou = (menor == maior)

        if acertou:
            print('\n''Voce acertou o numero secreto ''\n')
            print('*' * 70, '\n')
            break

        elif menor:
            print('Voce Errou ! O numero que voce digitou é menor que o numero secreto')
            print('*' * 70, '\n')
        elif maior:
            print('Voce Errou ! o numero que voce digitou é maior que o numero secreto')
            print('*' * 70, '\n')
        else:
            print('0')

    print('== Fim de jogo ==')
    print('\n Digite (1) para continuar (2) para sair ')
    novamente = int(input(''))
    if novamente == 1:
        jogar_adivinhacao()
    else:
        jogos.escolha_APP()


if __name__ == '__main__':
    jogar_adivinhacao()

