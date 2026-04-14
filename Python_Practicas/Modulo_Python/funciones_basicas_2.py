from unicodedata import digit


print("Al ejecutar estre script podra encontrar el ejercicio practica Funciones Basicas 2")
print(" ")
print("Debido a la longitud de los ejercicios, dejare unas variables booleanos para visualizar cada ejercicio en el codigo")
print(" ")

# --- Booleans ----
ejercicio1_multiplica2 = False
ejercicio2_sumaresta = False
ejercicio3_sum_minus_len = True
ejercicio4_val_mul_second = True
ejercicio5_val_mul_len = True

#--- Ejercicio 1
def multiplo_por_2(num:int): #por el ejemplo dado, me imagino que es multiplo y no multiplica
    print(f"- numero ingresado {num}")
    numlist = []
    for i in range(0,num*2+1):
        if(i == 0 or i % 2 == 0 ):
            numlist.append(i)
    return numlist


if(ejercicio1_multiplica2):
    var = multiplo_por_2(5)
    print("--- Multiplos de 2 hasta llegar a la multiplicacion del valor ----")
    print( var )
else:
    print("- ejercicio 1 saltado")

print(" ")

#--- Ejercicio 2
def suma_resta(num1:float, num2:float):
    print(f"- numeros ingresados {num1}, {num2}")
    print(num1 + num2, "suma de valores")
    return(num1 - num2)

if(ejercicio2_sumaresta):
    print("--- Multiplos de 2 ----")
    var = suma_resta(5,4)
    print(var, "resta de valores")
else:
    print("- ejercicio 2 saltado")
    
print(" ")

#--- Ejercicio 3
def sum_minus_len(list:list):
    acumulador = 0

    print(f"- lista escogida: {list}, longitud de lista: {len(list)}") 
    for element in list:
        if(type(element == str) or type(element) == int):
            acumulador += float(element)
        elif(type(element == float)):
            acumulador += element
    return acumulador - len(list)
            

if(ejercicio3_sum_minus_len):
    print("--- Sumatoria menos Longitud ----")
    print("resultado:", sum_minus_len([1,"2",3,4])) #el metodo sirve tanto para strings, como int y floats
else:
    print("- ejercicio 3 saltado")

print(" ")

#--- Ejercicio 4
def valores_multiplicados_segundo(list:list):
    print(f"- lista escogida: {list}, longitud de la lista: {len(list)}, segundo numero: {list[1]}")
    print("- automaticamente volvera int todos los valores")
    new_list = []
    if(len(list) <= 1):
        print("la lista es demasiado corta para proceder")
        return new_list
    
    segundo_valor = int(list[1])
    for element in list:
        if(type(element == str) or type(element) == float):
            new_list.append(int(element) * segundo_valor)
        else:
            new_list.append(element * segundo_valor)
    return new_list

if(ejercicio4_val_mul_second):
    print("--- Valores multiplicados por el segundo ----")
    print("resultado:", valores_multiplicados_segundo([1,3.5,5,7]))

print(" ")

#--- Ejercicio 5
def val_mul_len(valor:int, longitud:int):
    print(f"Valores recibidos: {valor}, {longitud}")
    newlist = []
    for i in range(longitud):
        newlist.append(valor*longitud)
    return newlist

if(ejercicio5_val_mul_len):
    print("--- Valor multiplicado y longitud ----")
    print(val_mul_len(7,5))

  



