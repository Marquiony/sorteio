import random

print("***********************************************************")
print("Bem vindo ao gerador de números da mega da virada do coiote")
print("***********************************************************")

jogada_1 = int(input("Quantos números você quer jogar em cada jogo? "))
jogada_2 = int(input("Quantos jogos você quer fazer? "))
y = []
j = 0
lista2 = []

def remove_repetidos():
    for x in y:
        if x not in lista2:
            lista2.append(x)

        else:
            pass

    lista2.sort()
    return lista2

def main():
    while len(remove_repetidos()) < jogada_1:
        y.append(random.randint(1, 60))
        remove_repetidos()

    return remove_repetidos()

while j < jogada_2:
    y = []
    lista2 = []
    print(main())
    j += 1

print("se você ganhar, doe 5% a marquiony :)")

input()