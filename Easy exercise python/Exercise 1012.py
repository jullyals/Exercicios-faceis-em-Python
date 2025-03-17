# -*- coding: utf-8 -*-
#Cálculo da área de polígonos regulares
pi = 3.14159
a, b, c= map(float, input().split(" "))
st3=a*c/2               #Área do triângulo
cic=pi*c**2             #Área do círculo
st4=(a+b)*c/2           #Área do trapézio
qu=b**2                 #Área do quadrado
ret=a*b                 #Área do retângulo
print("TRIANGULO: %0.3f" %st3) 
print("CIRCULO: %0.3f" %cic) 
print("TRAPEZIO: %0.3f" %st4) 
print("QUADRADO: %0.3f" %qu) 
print("RETANGULO: %0.3f" %ret)
