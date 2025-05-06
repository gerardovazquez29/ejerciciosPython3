

#* bucle for
"""
frutas = ['manzana', 'pera', 'durazno']
for fruta in frutas:
    print(fruta)
"""
"""
#* for con Range()
for i in range(5):
    print(i)
"""
""""
#* for con enumerate()
frutas = ['manzana', 'pera', 'durazno']

for indice, fruta in enumerate(frutas):
    print(f"Indice {indice}: {fruta}")  #Indice 0: manzana, Indice 1: pera, Indice 2: durazno
"""

persona = {'nombre': 'Juan', 'edad': 35, 'ciudad': 'Juadalajara'}

#* for con diccionarios
#iterar sobre claves
#*for clave in persona:
#*    print(clave)  # nombre, edad, ciudad

# Iterar sobre valores
#*for valor in persona.values():
#*    print(valor) # Juan, 35, Juadalajara

# iterar sobre items (clave-valor)
#*for clave,valor in persona.items():
#*    print(f"{clave}: {valor}")  # nombre: Juan, edad: 35, ciudad: Juadalajara

#* for con else
# El else se ejecuta al terminar el bucle ( si no hay break)
#*for i in range(3):
#*    print(i)
#*else :
#*    print("Bucle terminado")    


#!while 
contador = 0
while contador < 5:
#*    print(contador)
    contador += 1  # 0,1,2,3,4

#* while con break
while True:
#*    respuesta = input("Escribe 'salir' para terminar: ")
#*    if respuesta.lower() == 'salir':
        break
#*    print(f"Escribiste: {respuesta}")

#* while con continue
# saltar una iteracion con continue
num = 0
while num < 5:
    num += 1
    if num == 3:
        continue
#*    print(num) #1,2,4,5

# multiples condiciones
x, y = 0, 5
while x < 10 and y > 0:
#     print(x, y)
     x += 1
     y -= 1  # 0 5, 1 4, 2 3, 3 2, 4 1

