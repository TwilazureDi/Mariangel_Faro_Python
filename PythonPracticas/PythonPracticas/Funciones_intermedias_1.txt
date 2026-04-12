print("Al ejecutar estre script podra encontrar el ejercicio CORE Funciones Intermedias")
print(" ")
print("Dejare unas variables booleanos para visualizar cada ejercicio en el codigo")
print(" ")

# --- Booleans ----
ejercicio1_actualizar_valores = True
ejercicio2_iterar_list_diccionario = True
ejercicio3_obtener_valores_dict = True
ejercicio4_iterar_diccionario_lista = True



#--- Ejercicio 1
if(ejercicio1_actualizar_valores):
    print("--- Actualizar valores en diccionarios y lista ----")
    matriz = [ [10, 15, 20], [3, 7, 14] ]

    matriz[1][0] = 6
    print("resultado:",matriz)

    print(" ")
    print("----------")
    print(" ")

    cantantes = [
        {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
        {"nombre": "Chayanne", "pais": "Puerto Rico"}
    ]
    cantantes[0]["nombre"] = "Enrique Martin Morales"
    print("Resultado:", cantantes)

    
    print(" ")
    print("----------")
    print(" ")

    ciudades = {
        "Mexico": ["Ciudad de Mexico", "Guadalajara", "Cancun"],
        "Chile": ["Santiago", "Concepcion", "Vina del Mar"]
    }
    ciudades["Mexico"][2] = "Monterrey"
    print("Resultado:", ciudades)
    
    print(" ")
    print("----------")
    print(" ")

    coordenadas = [
        {"latitud": 8.2588997, "longitud": -84.9399704}
    ]
    coordenadas[0]["latitud"] = 9.9355431
    print(coordenadas)

    print(" ")
    print("----------")
    print(" ")

if(ejercicio2_iterar_list_diccionario):
    print("--- Iterar a traves de una lista de diccionarios ----")
    cantantes =  [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "Jose Jose", "pais": "Mexico"},
    {"nombre": "Juan Luis Guerra", "pais": "Republica Dominicana"}
    ]

    def iterarDiccionario(dictionaryList):
        for element in dictionaryList:
            keylist = list(dict.keys(element))
            valueList = list(dict.values(element))
            print(f"{keylist[0]} - {valueList[0]}, {keylist[1]} - {valueList[1]}")
    iterarDiccionario(cantantes)

    print(" ")
    print("----------")
    print(" ")

if(ejercicio3_obtener_valores_dict):
    print("--- Obtener valores de una lista de diccionarios ----")
    cantantes =  [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "Jose Jose", "pais": "Mexico"},
    {"nombre": "Juan Luis Guerra", "pais": "Republica Dominicana"}
    ]

    def iterarDiccionario2(llave:str, dictionaryList:list):
        for element in dictionaryList:
            print(element.get(llave))
    iterarDiccionario2("nombre", cantantes)
    print(" ")
    iterarDiccionario2("pais", cantantes)

    print(" ")
    print("----------")
    print(" ")

if(ejercicio4_iterar_diccionario_lista):
    print("--- Iterar a traves de un diccionario con valores de lista ----")
    costa_rica = {
    "ciudades": ["San Jose", "Limon", "Cartago", "Puntarenas"],
    "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}
    def imprimirInfo(diccionario:dict):
        for element in diccionario:
            key = element
            valuelist = diccionario.get(key)
            print(len(valuelist), key)
            for value in valuelist:
                print(value)
            else:
                print(" ")
    imprimirInfo(costa_rica)