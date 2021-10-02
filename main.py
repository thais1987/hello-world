#Hello world
print("Hello World")

#Con variable
world:str = "World"
print(f"Hello {world}")

'''
TIPOS DE DATOS EN PYTHON
'''
#STR
miCadena: str = "Hola Mundo"
miCadena2: str = '''Hola Mundo'''

primeros_2_caracteres = miCadena[0:2]

print(f'Primeros dos caracteres: {primeros_2_caracteres}')

print(f'Texto Con Mayusculas: {miCadena.upper()}')

'''
BOOL
'''

casado = False

print(f'Casado? {casado}')

'''
Listas
'''

miLista: [str] = ['Martin', 'Juan', ' Ana']
print(*miLista)

#Rango
miRango = range(1, 10, 2)

miRango2 = range(10, 1, -2)

print(*miRango)

print(*miRango2)

'''
Diccionario
'''

persona = {
  "nombre": "Martin",
  "edad": 30,
  "email": "martin@imaginarygroup.com"
}

print(f'La edad de {persona.get("nombre")} es {persona.get("edad")}')

misNumeros = [1,2,3,3,4,5,1,5]
print(*misNumeros)

miSetDeNumeros = set(misNumeros)

print(*miSetDeNumeros)

miSetCongelado = frozenset(misNumeros)

'''
str
int
float
complex
list
tuple
range
dict
set
frozenset
bool
bytes
bytearray
memoryview
'''

'''
RETO 1
Operacion aritmetica que realice
((6-2)/5)^2
'''
operation = (((6-2)/5)**2)
operation2 = round(operation, 4)

print(operation.__round__(4))
print(operation2)


'''
RETO 2
'''
'''
cantidad_a_invertir = 300
interes_anual = 0.05
numero_de_years = 3
capital_obtenido = round(((cantidad_a_invertir*interes_anual)**numero_de_years),2)

print (f'El capital obtenido es de : {capital_obtenido}')
'''

'''
RETO 3

'''
'''
productos_de_temp = int (input ("Cuantos productos de temporada has comprado?: "))
productos_no_temp = int (input ("Cuantos productos fuera de temporada has comprado?: "))
producto:float = 14.99
descuento = 0.30
valor_prod_temp = productos_de_temp * producto
valor_prod_no_temp = (productos_no_temp * 14.99) * 0.70
valor_total = round((valor_prod_temp + valor_prod_no_temp),2)
ahorro = round((valor_prod_no_temp * descuento),2)

print(f'Has gastado: {valor_total}')
print(f'Te has ahorrado: {ahorro}')
'''

'''
RETO 4
'''
'''
year = int (input("Introduzca un año: "))

if ((year%4 == 0 and (year%100 != 0 or year%400 == 0))):
  print (f'El año es bisiesto')
else:
  print ('El año no es bisiesto')
  '''
'''
RETO 5
'''
'''
es_bisiesto = False
while es_bisiesto == False:  
  year = int (input("Introduzca un año: "))
  if (year%4 == 0 and (year%100 != 0 or year%400 == 0)):
    es_bisiesto = True
    print ("Felicitaciones el año es bisiesto")
  ''' 
'''
Tarea
'''
list_gen = {"comedia", "drama", "terror", "accion"}
print("Por favor introduzca los siguientes datos de una peli: ")
nom_peli = input("Nombre: ")
year = int(input("Año: "))
punt = float (input("Puntuación que le da (Introducir valor entre 1 y 5): "))
while punt < 1 or punt > 5:
  punt = float(input("Puntuación que le da (Introducir valor entre 1 y 5): "))
direc = input("Director: ")
gene = input("Género(Comedia, Drama, Terror ó Accion): ")
while gene.lower() not in list_gen:
  gene = input("Género(Comedia, Drama, Terror ó Accion): ")
fav_movie = {
  "Nombre": nom_peli,
  "Año": year,
  "Puntuacion": punt,
  "Director": direc,
  "Genero": gene
}
print(fav_movie.values())
















