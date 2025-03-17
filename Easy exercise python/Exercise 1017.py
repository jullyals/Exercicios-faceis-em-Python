# -*- coding: utf-8 -*-
#calcular quantos litros seriam necessários João precisa colocar, visto que o carro dele gasta 12l/km
t=int(input())
v=int(input())
d=v*t                   #calcula-se a distancia percorrida
quantl=d/12             #obtenção da quantidade de L necessários
print(f"{quantl:.3f}")
