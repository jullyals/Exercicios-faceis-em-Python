# -*- coding: utf-8 -*-
#um programa que leia um valor qualquer e 
#apresente uma mensagem dizendo em qual dos seguintes intervalos
#([0,25], (25,50], (50,75], (75,100]) este valor se encontra
a=float(input())
if 0 <= a <= 25:
    print(f"Intervalo [0,25]")
elif 25 < a <= 50:
    print(f"Intervalo (25,50]")
elif 50 < a <= 75:
    print(f"Intervalo (50,75]")
elif 75 < a <= 100:
    print(f"Intervalo (75,100]")
else:
    print(f"Fora de intervalo")
