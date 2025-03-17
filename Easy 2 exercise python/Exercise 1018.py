# -*- coding: utf-8 -*-
#Calcule o menor número de notas possíveis (cédulas) no qual o valor pode ser decomposto.
n=int(input())
notas = [100, 50, 20, 10, 5, 2, 1] #notas possíveis no qual pode ser decomposto
print(n)
for notas in notas:
    quantidade = n // notas  # Divisão em inteiros para saber a quantidade de notas
    n -= quantidade * notas  # Subtração do valor restante
    print(f"{quantidade} nota(s) de R$ {notas},00")
