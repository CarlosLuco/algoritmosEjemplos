#Programa ejemplo algoritmos y programación
"""
Created on Tue Apr 21 20:50:25 2020

@author: Carlos Luco
"""

import time

def limpiar_pantalla():
    time.sleep(10)
    print ("\n" * 100)


numero = 0
print("Programa Adivino de números entre 1 y 30")
print("Escoja en su mente un núumero entre 1 y 30\n\n")
limpiar_pantalla()


print("Le mostraré secuencias de números, si su número está, diga si\n")
print("1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31")
print("¿Está su numero?. Responda si/no\n")

respuesta = input()
if respuesta=="si":
    numero = numero + 1
    
print("2, 3, 6, 7, 10, 11, 14, 15, 18, 19, 22, 23, 26, 27, 30, 31")
print("¿Está su numero?. Responda si/no\n")

respuesta = input()
if respuesta=="si":
    numero = numero + 2

print("4, 5, 6, 7, 12, 13, 14, 15, 20, 21, 22, 23, 28, 29, 30, 31")
print("¿Está su numero?. Responda si/no\n")

respuesta = input()
if respuesta=="si":
    numero = numero + 4

print("8, 9, 10, 11, 12, 13, 14, 15, 24, 25, 26, 27, 28, 29, 30, 31")
print("¿Está su numero?. Responda si/no\n")

respuesta = input()
if respuesta=="si":
    numero = numero + 8

print("16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31")
print("¿Está su numero?. Responda si/no\n")

respuesta = input()
if respuesta=="si":
    numero = numero + 16

print("Procesando imagenes mentales telepáticas, espere\n\n")
limpiar_pantalla()

print("Su numero es el ", numero)