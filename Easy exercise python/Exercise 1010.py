# -*- coding: utf-8 -*-
#entradas:Código da peça, quantidade e valor. Somar e apresentar o resultado final.
cod1, quant1, v1=map(float, input().split(" "))
cod2, quant2, v2=map(float, input().split(" "))
total=(quant1*v1)+(quant2*v2)
print("VALOR A PAGAR: R$ %0.2f" %total)
