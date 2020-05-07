# -*- coding: utf-8 -*-
"""
Created on Fri May  1 15:07:24 2020

@author: Carlos Luco Montofré
"""


def validaEntero():
    
    notValido = True
    
    while notValido:
        entrada =input()
        
        try:
            numero = int(entrada)
            notValido = False
        except ValueError:
            print("Error digitación. Escriba número entero")
    
    return numero


def validaFlotante():
    
    notValido = True
    
    while notValido:
        entrada =input()
        
        try:
            numero = float(entrada)
            notValido = False
        except ValueError:
            print("Error digitación. Escriba número flotante")
    
    return numero


print("programa valida datos entrada")

print("Digite un número entero")
numero = validaEntero()
print("El número es ", numero)

print("Digite un número punto flotante")
numero = validaFlotante()
print("El número es ", numero)