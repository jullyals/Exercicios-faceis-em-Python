# -*- coding: utf-8 -*-
#Código que leia as seguintes condições:
# se B for maior do que C e se D for maior do que A; 
# e a soma de C com D for maior que a soma de A e B e 
# se C e D, ambos, forem positivos e se a variável A for par
a,b,c,d=map(int, input().split(" "))
cd = c + d
ab = a + b
if b>c and d>a and cd>ab and c>0 and d>0 and a%2==0: #condições exigidas
    print(f"Valores aceitos")
else:
    print(f"Valores nao aceitos")
