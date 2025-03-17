# -*- coding: utf-8 -*-
#cálculo das raízes da equação de Bhaskara
a, b, c = map(float, input().split())
#primeiramente coloca as condições, sendo elas: 
#equação quadratica, não pode ter divisão por 0 e sem raizes negativas
if a == 0:                              #verificar se é uma equação de 2º grau(a diferente de 0)
    print("Impossivel calcular")
else:
    delta = b**2 - 4 * a * c            #sendo quadratica, calcula-se o delta
    if delta < 0:                       #se delta for menor que 0(raiz negativa), não calcular
        print("Impossivel calcular")
    else:                               #após condições aceitas, calcula-se as raizes
        r1 = (-b + (delta**(1/2))) / (2 * a)
        r2 = (-b - (delta**(1/2))) / (2 * a)
        print(f"R1 = {r1:.5f}")
        print(f"R2 = {r2:.5f}")
