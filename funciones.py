
def saludar(nombre):
    return f"Hola, {nombre}!"
print(saludar("Gerardo")) #Hola, Gerardo!

#* Funcion con valor por defecto
def potencia(base, exponente=2):
    return base ** exponente
print(potencia(3))  # 9 (3^2)
print(potencia(2,4)) # 16 (2^4)


def hacer_danza():  # Define el hechizo "hacer_danza"
    print(" Girar")
    print(" Saltar")

hacer_danza()  # ¡Ejecuta el hechizo!
# Salida:
# Girar
# Saltar

#* Hechizo para hacer bailar al robot  
def hechizo_bailar(pasos):  
    for i in range(pasos):  
        print(f" Paso {i+1}: ¡Baile robotico!")  

hechizo_bailar(3)  
# Salida:  
#  Paso 1: ¡Baile robotico!  
#  Paso 2: ¡Baile robotico!  
#  Paso 3: ¡Baile robotico!  


#! lambda
sumar = lambda a, b: a + b  

print(sumar(5, 3))  # Salida: 8 

#* Ejemplo con juguetes:  
duplicar_juguetes = lambda juguete: [j * 2 for j in juguete]  
print(duplicar_juguetes(["pelota", "carro"]))  # Salida: ['pelota','pelota' , 'carro', 'carro'] 


def hechizo_cumpleaños(nombre):  
    # Hechizo interno para el pastel  
    def hacer_pastel():  
        return "pan"  

    pastel = hacer_pastel()  
    print(f"¡{nombre}, sopla las velas! {pastel}")  

hechizo_cumpleaños("Robo")  # Salida: ¡Robo, sopla las velas!   


#!Funciones con *args y **kwargs: Hechizos Flexibles
# Hechizo para mezclar juguetes  
def mezclar_juguetes(*args, **kwargs):  
    print("Juguetes normales:", args)  
    print("Juguetes especiales:", kwargs)  

mezclar_juguetes("pelota", "oso", magico="varita", peligroso="dragón")  
# Salida:  
# Juguetes normales: ('pelota', 'oso')  
# Juguetes especiales: {'magico': 'varita', 'peligroso': 'dragón'} 

#!Funciones de Orden Superior
#*map()
numeros = [1, 2, 3]  
duplicar = lambda x: x * 2  
resultado = list(map(duplicar, numeros))  
print(resultado)  # Salida: [2, 4, 6]  

#* filter()
pares = list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4]))  
print(pares)  # Salida: [2, 4] 

#! Decoradores
def decorador_sonido(funcion):  
    def envoltura():  
        print(" ¡Música épica!")  
        funcion()  
        print(" ¡Fin de la música!")  
    return envoltura  

@decorador_sonido  
def hechizo_lanzar():  
    print(" ¡Lanzamiento de cohetes!")  

hechizo_lanzar()  
# Salida:  
#  ¡Música épica!  
#  ¡Lanzamiento de cohetes!  
#  ¡Fin de la música!  