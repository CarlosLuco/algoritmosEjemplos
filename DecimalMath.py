# -*- coding: utf-8 -*-
"""
Created on Tue May  5 09:45:16 2020

@author: Carlos Luco Montofré
"""
i = 0
decimal = 0
numerostr = input("ingrese binario\n")

largo = len(numerostr)
numero = int(numerostr)

for i in range(largo):
    cuociente = numero // 10
    resto = numero % 10
    decimal = (resto * (2**i)) + decimal
    numero = cuociente
    i = i + 1

decimal = (numero * (2**i)) + decimal
   
print(decimal)
