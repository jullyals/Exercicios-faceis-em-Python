# -*- coding: utf-8 -*-
#nome do vendedor, salário fixo, total de vendas/mês(comissão de 15%)
n=input()                                        #vendedor
salfixo=float(input())                           #salário fixo
tvendas=float(input())                           #total de vendas em R$
t=salfixo+tvendas*0.15                           #calculo do total a receber, com a comissão 15%
print(f"TOTAL = R$ {t:.2f}")
