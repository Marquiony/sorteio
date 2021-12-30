import random
import streamlit as st

st.write(""" 
# Bem vindo ao gerador de números da mega da virada do coiote
""")


st.header("Escolha as configurações do seu jogo")

jogada_1 = st.slider("Quantos números você quer jogar em cada jogo?", 6, 15)
jogada_2 = st.slider("Quantos jogos você quer fazer?", 1, 20)
y = []
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


j = 0
while j < jogada_2:
    y = []
    lista2 = []
    st.write(main())
    j += 1

st.write("se você ganhar, doe 5% a marquiony :)")
