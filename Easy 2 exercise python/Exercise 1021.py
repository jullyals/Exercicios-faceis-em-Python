# -*- coding: utf-8 -*-
n=float(input())
centavos = round(n * 100) #convertendo todos os valores para centavo, para facilitar
notas=[10000, 5000, 2000, 1000, 500, 200]
moedas=[100, 50, 25, 10, 5, 1]
print(f"n")
print("Notas:")
for nota in notas:
    quantidade = centavos // notas  # Divisão em inteiros para saber a quantidade de notas
    centavos -= quantidade * notas  # Subtração do valor restante
    print(f"{quantidade} nota(s) de R$ {notas},00")
print("Moedas:")
for moeda in moedas:
    quantidade = n // moedas  # Divisão em inteiros para saber a quantidade de notas
    n -= quantidade * moedas  # Subtração do valor restante
    print(f"{quantidade} moeda(s) de R$ {moedas},00")
