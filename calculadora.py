import time

import jogos


def calcular():
    def soma(a, b):
        s = a + b
        print(f'A Soma de {a} + {b} = {s}')


    def subtracao(a, b):
        s = a - b
        print(f'A Subtração de {a} - {b} = {s}')


    def multiplicacao(a, b):
        s = a * b
        print(f'A Multiplicação de {a} * {b} = {s}')


    def divisao(a, b):
        s = a // b
        print(f'A Divisão de {a} / {b} = {s}')

    calc = '0'
    while calc in calc:
        print('*********************')
        print('Escolha a operação Matemática ! ')
        print('(1)-SOMA -- (2)-Subtracao -- (3)-Multiplicação -- (4)-Divisão -- (0)-SAIR')

        print('**********************')
        operacao = int(input('Digite um numero ! '))
        print('*' * 70)

        if operacao < 0 or operacao > 4:
            print('Digite um numero de 0 a 4''\n')


        #if operacao < 0:
            #print('Digite um numero de 1 a 4''\n')
        #if operacao > 4:
            #print('Digite um numero de 1 a 4''\n')
            #continue

        elif operacao == 1:
            print('Soma')
            a = int(input('Digite o primeiro numero '))
            b = int(input('Digite o segundo numero '))
            print("="*40)
            print(soma(a, b))
            print("=" * 40)
            time.sleep(2)
        elif operacao == 2:
            print('subtracao')
            a = int(input('Digite o primeiro numero '))
            b = int(input('Digite o segundo numero '))
            print("=" * 40)
            print(subtracao(a, b))
            print("=" * 40)
            time.sleep(2)
        elif operacao == 3:
            print('multiplicacao')
            a = float(input('Digite o primeiro numero '))
            b = float(input('Digite o segundo numero '))
            print("=" * 40)
            print(multiplicacao(a, b))
            print("=" * 40)
            time.sleep(2)
        elif operacao == 4:
            print('Divisão')
            a = int(input('Digite o primeiro numero '))
            b = int(input('Digite o segundo numero '))
            print("=" * 40)
            print(divisao(a, b))
            print("=" * 40)
            time.sleep(2)
        elif operacao == 0:
            print(' Fechando a Calculadora ')
            jogos.escolha_APP()
            break
        else:
            print(' ')


if __name__ == '__main__':
    calcular()
