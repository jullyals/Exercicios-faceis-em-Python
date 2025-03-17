# -*- coding: utf-8 -*-
# Leia um valor inteiro correspondente à idade de uma pessoa em dias e informe-a em anos, meses e dias
idade_dias = int(input()) 
ano = idade_dias // 365             #idade em anos
mes = (idade_dias % 365) // 30      #idade em meses
dias = (idade_dias % 365) % 30      #idade em dias, que é o resto do resto da divisão dos dias/365 e depois por 30
print(f"{ano:.0f} ano(s)")
print(f"{mes:.0f} mes(es)")
print(f"{dias:.0f} dia(s)")
