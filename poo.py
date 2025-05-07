
#! programacion orientada a objetos
class Robot:  
    # Atributos: "Características" del robot  
    def __init__(self, nombre, color):  
        self.nombre = nombre  # ¡Todos los robots tendrán nombre!  
        self.color = color    # Y un color favorito 

    # Métodos: "Acciones" del robot  
    def saludar(self):  
        print(f"¡Hola! Soy {self.nombre} y soy {self.color}.")  

    def bailar(self):  
        print(f"{self.nombre} está bailando.")  

# objetos
# Creamos robots usando la clase "Robot"  
robot1 = Robot("Robo", "azul")  
robot2 = Robot("Bip", "rojo")  

robot1.saludar()  # Salida: ¡Hola! Soy Robo y soy azul.  
robot2.bailar()   # Salida: Bip está bailando. 

#herencia
class RobotNinja(Robot):  # Hereda de "Robot"  
    def atacar(self):  
        print(f"{self.nombre} lanza estrellas ninja!")  

# Creamos un RobotNinja  
ninja = RobotNinja("Kunai", "negro")  
ninja.saludar()  # Método heredado: ¡Hola! Soy Kunai y soy negro.  
ninja.atacar()   # Método nuevo: Kunai lanza estrellas ninja! 

# encapsulamiento

class RobotSeguro:  
    def __init__(self):  
        self.__codigo_secreto = "1234"  # Atributo privado (solo dentro de la clase)  

    def verificar_codigo(self, codigo):  
        if codigo == self.__codigo_secreto:  
            print("¡Acceso permitido! ")  
        else:  
            print("¡Código incorrecto!")  

robo_seguro = RobotSeguro()  
robo_seguro.verificar_codigo("0000")  # Salida: ¡Código incorrecto!  
# robo_seguro.__codigo_secreto  # ¡Error! No puedes verlo desde afuera.  


#poliforfismo

class RobotPerro(Robot):  
    def saludar(self):  # Sobrescribe el método "saludar"  
        print(f"¡Guau! Soy {self.nombre} y soy {self.color}.")  

# Objetos diferentes usando el mismo método  
robot_normal = Robot("Tito", "verde")  
robot_perro = RobotPerro("Max", "marrón")  

robot_normal.saludar()  # ¡Hola! Soy Tito y soy verde.  
robot_perro.saludar()   # ¡Guau! Soy Max y soy marrón. 