
#! Fabrica de Robots
# Clase base  
class Juguete:  
    def __init__(self, nombre):  
        self.nombre = nombre  

    def jugar(self):  
        print("¡Juguemos!")  

# Clase heredada  
class Pelota(Juguete):  
    def jugar(self):  # Polimorfismo  
        print(f"¡{self.nombre} está rebotando!")  

# Crear objetos  
juguete1 = Juguete("Tren")  
juguete2 = Pelota("Baloncesto")  

juguete1.jugar()  # Salida: ¡Juguemos!  
juguete2.jugar()  # Salida: ¡Baloncesto está rebotando!  
