
#* Listas
frutas = ["manzana", "banana", "naranja"]
frutas.append("uva") # añade el elemento
print(frutas[1])  # salida: banana

# Lista mutable (puede modificarse)
numeros = [1, 2, 3, 4]
numeros.append(5)  # Añade 5 al final

#* Tuplas
# Tupla inmutable (no puede modificarse)
coordenadas = (4, 5)
colores = ("rojo", "verde", "azul")

# Acceso a elementos
print(coordenadas[0])  # Salida: 4

# Error al intentar modificar
# coordenadas[0] = 10  # ¡Lanzará TypeError!

#* Conjuntos(Sets)
# Colección NO ordenada y SIN elementos duplicados
frutas = {"manzana", "banana", "naranja", "manzana"}
print(frutas)  # Salida: {'banana', 'naranja', 'manzana'} (sin duplicados)

# Operaciones con conjuntos
a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))          # {1, 2, 3, 4, 5}
print(a.intersection(b))   # {3}



# * Diccionarios
persona = {
    "nombre": "Luisa",
    "edad": 30,
    "ciudad": "Madrid"
}
print(persona["edad"])  # Salida: 30

# Pares clave-valor
usuario = {
    "id": 101,
    "nombre": "Laura",
    "activo": True
}

