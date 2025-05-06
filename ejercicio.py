
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