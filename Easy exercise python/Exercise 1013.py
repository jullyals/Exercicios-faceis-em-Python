# -*- coding: utf-8 -*-
# O maior valor entre 3 números inteiros usando fórmula
a, b, c= map(int, input().split(" "))
mab=(a+b+abs(a-b))/2.0                  #verifica-se o maior valor entre a e b
mabc=(mab+c+abs(mab-c))/2.0             #verifica-se o maior valor entre o resultado de a e b com o valor de c
print(f"{mabc:.0f} eh o maior")
