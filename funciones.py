
def saludar(nombre):
    return f"Hola, {nombre}!"
print(saludar("Gerardo")) #Hola, Gerardo!

#* Funcion con valor por defecto
def potencia(base, exponente=2):
    return base ** exponente
print(potencia(3))  # 9 (3^2)
print(potencia(2,4)) # 16 (2^4)


