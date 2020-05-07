# -*- coding: utf-8 -*-
"""
Created on Wed May  6 11:59:10 2020

@author: Carlos Luco Montofré
"""
sumatemp = 0
sanos = 0
contatemp = 0
enfermas = 0

for i in range(3):

    nombre = input("Ingrese su nombre")
       
    while nombre == "":
        print("Error digitación, Escriba nombre correcto")
        nombre = input()
    
    notValido = True
    
    while notValido:
        
        lectura = input("Ingrese su temperatura")
        
        try:
            temperatura = float(lectura)
            notValido = False
        except ValueError:
            print("Error digitación. Escriba temperatura correcta")
    
   
    if temperatura >= 37.5:
        enfermas = enfermas + 1
        print(nombre, "Parece que estas enfermo, visite a un médico")
        
    if temperatura <= 37.0:
        sanos = sanos + 1
        
    if temperatura > 37 and temperatura < 37.5:
        sumatemp = sumatemp + temperatura
        contatemp = contatemp + 1
        
        
print ("Los clientes sanos son ",sanos)

resultado = (enfermas / 3) * 100
print("El porcentaje de enfermos es ", resultado)

if contatemp > 0:
    promedio = sumatemp / contatemp
    print("El promedio de temperatura asintomaticos es ", promedio)
else:
    print("No hay clientes asintomaticos")