import time


def carregando():
    for i in range(101):
        print(f"Carregando {i} %")
        time.sleep(0.001)


if __name__ == '__main__':
    carregando()

