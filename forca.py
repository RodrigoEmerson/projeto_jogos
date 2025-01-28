import random

import jogos


def jogar_forca():

    print('*'*36,)
    print('***  Bem vindo ao jogo da Forca  ***')
    print('*'*36,)

    arquivo = open('palavra.txt', 'r')
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()

    letras_acertadas = ['_' for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while not enforcou and not acertou:

        chute = input('Digite uma letra. ')
        chute = chute.strip().upper()

        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if chute == letra:
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if acertou:
        print(' \n Voce ganhou! ')
        print('\n Digite (1) para continuar (2) para sair ')
        novamente = int(input(''))
        if novamente == 1:
            jogar_forca()
        else:
            jogos.escolha_APP()
    else:
        print('\n Voce perdeu! ')
        print("""
                 ___________
                 |        \|
                 ()        |
                /|\        |
                / \        |
             ______________|""")
        print('\n Digite (1) para continuar (2) para sair ')
        novamente = int(input(''))
        if novamente == 1:
            jogar_forca()
        else:
            jogos.escolha_APP()

    print('\n== Fim de jogo ==')


if __name__ == '__main__':
    jogar_forca()
