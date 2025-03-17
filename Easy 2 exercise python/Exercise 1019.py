# -*- coding: utf-8 -*-
#tempo de duração em segundos de um determinado evento transformado em horas, minutos e segundos
ts=int(input())
horas = ts // 3600         #tempo em horas
minutos = (ts % 3600)//60  #tempo em minutos
segundos = ts % 60         #tempo em segundos
print(f"{horas}:{minutos}:{segundos}")
