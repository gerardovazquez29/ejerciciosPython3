
#! programa que verifica si un numero es primo

numero = int(input("teclea un numero para saber si es primo: "))

def es_primo(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
        return True
    
print(f"{numero} es primo: {es_primo(numero)}") 

print('--------------------------------------')


#! Sistema de etiquetas únicas para artículos
articulo = {
    "titulo": "Python Basics",
    "tags": {"programacion", "tutorial", "python"}
}
#* Añadir nueva etiqueta (no se repiten)
articulo["tags"].add("programacion") # no cambia ya existe
articulo["tags"].add("beginners") # 

print(articulo["tags"]) # Salida: {'programación', 'tutorial', 'python', 'beginners'}

#* Coordenadas fijas (usando tupla)
punto = (10, 20)
print(f"X: {punto[0]}, Y: {punto[1]}")  # X: 10, Y: 20

print('--------------------------------------')

#!Juego Adivina el Número

import random

numero_secreto = random.randint(1, 5) # numero magico entre 1 y 5
intento = int(input("Adivina el numero(1-5)"))
if intento == numero_secreto:
    print("Ganaste")
else: 
    print(f"Perdiste El numero era: {numero_secreto}")
    
print('--------------------------------------')


#! Adivina el Color del Robot

color_secreto = "azul"  
intento = input("Adivina mi color (rojo/verde/azul): ")  

if intento == color_secreto:  
    print("¡Correcto! Soy azul como el cielo")  
elif intento in ["rojo", "verde"]:  # elif al rescate  
    print("Casi... ¡pero no!")  
else:  
    print("Ese color no existe en mi lista.")  

print('--------------------------------------')

#! El Robot Chef

# Función normal con lambda y map  
def hacer_pizza(ingredientes):  
    preparar = lambda i: f" Añadir {i}"  
    pasos = list(map(preparar, ingredientes))  
    for paso in pasos:  
        print(paso)  

hacer_pizza(["queso", "tomate", "champiñones"])  
# Salida:  
# Añadir queso  
# Añadir tomate  
# Añadir champiñones 