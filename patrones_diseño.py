
#! Singleton
class RobotRey:
    _instancia = None  # Aquí se guarda el único robot rey

    def __new__(cls):
        if not cls._instancia:
            cls._instancia = super().__new__(cls)
        return cls._instancia

# Prueba:
rey1 = RobotRey()
rey2 = RobotRey()
print(rey1 is rey2)  # Salida: True (¡Son el mismo robot rey!)

#! Factory
class RobotGuerrero:
    def accion(self):
        return "¡Atacar con láser! "

class RobotCocinero:
    def accion(self):
        return "¡Cocinar pizza! "

def fabrica_robot(tipo):
    if tipo == "guerrero":
        return RobotGuerrero()
    elif tipo == "cocinero":
        return RobotCocinero()

# Uso:
robot = fabrica_robot("cocinero")
print(robot.accion())  # Salida: ¡Cocinar pizza! 

#! Observer
class SensorDeMovimiento:
    def __init__(self):
        self._observadores = []  # Lista de robots suscritos

    def suscribir(self, observador):
        self._observadores.append(observador)

    def notificar(self, mensaje):
        for robot in self._observadores:
            robot.actualizar(mensaje)

class RobotVigilante:
    def actualizar(self, mensaje):
        print(f"¡Alerta! Mensaje recibido: {mensaje} 🚨")

# Uso:
sensor = SensorDeMovimiento()
robot = RobotVigilante()
sensor.suscribir(robot)
sensor.notificar("Movimiento detectado en la cocina")  # ¡Alerta!...


#! Strategy
class EstrategiaCaminar:
    def caminar(self):
        pass

class CaminarRapido(EstrategiaCaminar):
    def caminar(self):
        return "¡Caminando a 10 km/h! "

class CaminarLento(EstrategiaCaminar):
    def caminar(self):
        return "¡Caminando a 2 km/h... "

class Robot:
    def __init__(self):
        self.estrategia = CaminarRapido()  # Estrategia por defecto

    def cambiar_estrategia(self, estrategia):
        self.estrategia = estrategia

    def caminar(self):
        print(self.estrategia.caminar())

# Uso:
robot = Robot()
robot.caminar()  # ¡Caminando a 10 km/h! 
robot.cambiar_estrategia(CaminarLento())
robot.caminar()  # ¡Caminando a 2 km/h...


#! Decorator
class RobotBasico:
    def funcion(self):
        return "Robot básico: Caminar"

class DecoradorArmadura:
    def __init__(self, robot):
        self._robot = robot

    def funcion(self):
        return self._robot.funcion() + " + Armadura pesada "

class DecoradorLaser:
    def __init__(self, robot):
        self._robot = robot

    def funcion(self):
        return self._robot.funcion() + " + Láser "

# Uso:
robot = RobotBasico()
robot = DecoradorArmadura(robot)
robot = DecoradorLaser(robot)
print(robot.funcion())  # "Robot básico: Caminar + Armadura pesada  + Láser "