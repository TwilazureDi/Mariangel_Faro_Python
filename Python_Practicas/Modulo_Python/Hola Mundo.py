print("Bienvenido al archivo principal del proyecto!")
print("Aqui encontraras la primera practica a continuacion:")
print(" ")

# 1. Imprime "Hola, mundo"
print("Hola mundo!")

print(" ")

# 2. Imprime "Hola, Valeria" con el nombre en una variable
nombre = "Mariangel"
print("Hola,", nombre ) # con una coma
print("Hola, " + nombre  ) # con un +

print(" ")

# 3. Imprimir "Hola 156" con el numero en una variable
numero = 5
print( "Hola",numero,"!" ) # con una coma
print( "Hola " + str(numero)+"!") #con un + -- este deberia arrojar un error!, corrigelo con conversion

print(" ")

# 4. Imprimir "Me encanta comer tacos y arepas" con las comidas en variables
comida1 = "arroz con huevo"
comida2 = "arepas" #no joke, realmente son las arepas, son mi pan de cada dia
print("Me encanta comer {} y {} - string format version".format(comida1,comida2)) # con .format()
print(f"Me encanta comer {comida1} y {comida2} - string f version" ) # con una cadena f
print("Me encanta comer %s y %s - formating version"%(comida1,comida2))