# -*- coding: utf-8 -*-
"""
Created on Tue May  5 09:45:16 2020

@author: Carlos Luco Montofré
"""
i = 0
binario = 0
numero = int(input("ingrese decimal\n"))

while numero > 1:
    cuociente = numero // 2
    resto = numero % 2
    binario = (resto * (10**i)) + binario
    numero = cuociente
    i = i + 1

binario = (numero * (10**i)) + binario
   
print("\nEl equivalente binario es  ",binario)
