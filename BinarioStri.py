# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 20:28:24 2020

@author: Carlos Luco Montofré
"""

binario = ""
numero = int(input("ingrese número decimal\n"))

while numero > 1:
    cuociente = numero // 2
    resto = numero % 2
    binario = str(resto) + binario
    numero = cuociente

binario = str(numero) + binario
   
print("\nEl equivalente binario es  " + binario)
