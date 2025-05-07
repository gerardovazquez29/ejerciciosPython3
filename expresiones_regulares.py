
import re

texto = "El robot tiene una misión: encontrar el código ABC123."

# Buscar si aparece "ABC" seguido de 3 números
if re.search(r"ABC\d{3}", texto):
    print("¡Código encontrado! ")
else:
    print("¡Sigue buscando! ")
# Salida: ¡Código encontrado! 


texto_juguetes = "Los juguetes son: carro12, muñeca34, pelota56."

# Buscar todas las palabras seguidas de 2 números
juguetes = re.findall(r"\w+\d{2}", texto_juguetes)
print("Juguetes con código:", juguetes)
# Salida: ['carro12', 'muñeca34', 'pelota56']


texto = "El robot ganó 3 premios el 25/04/2024."

# Extraer fecha y premios
resultado = re.search(r"(\d+) premios.*(\d{2}/\d{2}/\d{4})", texto)
if resultado:
    print(f"Premios: {resultado.group(1)}, Fecha: {resultado.group(2)}")
# Salida: Premios: 3, Fecha: 25/04/2024 


def validar_correo(correo):
    # Formato: texto@texto.texto
    patron = r"^\w+@\w+\.\w+$"
    return re.match(patron, correo) is not None

print(validar_correo("robot@python.com"))  # True 
print(validar_correo("robot_python"))      # False


texto = "El robot123 necesita reparación. Código: ABC789."

# Cambiar números por "X"
nuevo_texto = re.sub(r"\d", "X", texto)
print(nuevo_texto)  
# Salida: El robotXXX necesita reparación. Código: ABCXXX.



texto = "El tesoro está en (27.5, -15.3). Clave: A1B2C3."

# Buscar coordenadas (números con decimales)
coordenadas = re.findall(r"\((-?\d+\.\d+),\s*(-?\d+\.\d+)\)", texto)
print("Coordenadas:", coordenadas)  # [('27.5', '-15.3')] 🗺️

# Buscar clave (letra + número)
clave = re.search(r"[A-Z]\d+[A-Z]\d+[A-Z]\d+", texto)
print("Clave:", clave.group())  # A1B2C3


"""
Regex = Códigos secretos para buscar patrones.
re.search() = Linterna para encontrar algo. 
re.findall() = Imán para atraer todas las coincidencias. 
re.sub() = Varita para reemplazar texto.


Patrón Útil  	Ejemplo	      Encuentra...
\d{3}-\d{3} 	"123-456"	  Números tipo teléfono. 
[A-Z][a-z]+	    "Robot"      Palabras con mayúscula. 
\b\d{4}\b	    "2024"	     Años de 4 dígitos. 
^[a-z0-9_]+$	"usuario123"	Nombres de usuario válidos. 
"""
