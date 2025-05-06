edad =  25
altura = 1.75
nombre = "Ana"
es_estudiante = True

#* Estructuras de control
numero = -5
if numero > 0:
    print('Positivo')
elif numero == 0:
    print('Cero')
else:
    print('Negativo')


#* Bucles

for i in range(5):
     print(i)

contador = 5
while contador < 10:
    #print(contador)  # Uncommented to fix indentation error
    contador += 1

#*  operadores logicos

numero =  (5 > 3) and (2 < 4)
print(numero)
numero1 = (5 > 3) or (1 == 0)
print(numero1)
numero2 = not (2 <= 2)
print(numero2)
