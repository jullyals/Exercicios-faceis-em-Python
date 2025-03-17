# -*- coding: utf-8 -*-
#Cálculo da distância entre dois pontos quaisquer
x1, y1= map(float, input().split(" "))
x2, y2= map(float, input().split(" "))
d=(((x2-x1)**2)+((y2-y1)**2))**0.5 #equação da distância entre dois pontos
print(f"{d:.4f}")
