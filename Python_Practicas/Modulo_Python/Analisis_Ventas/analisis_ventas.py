#---Diccionario de ventas

print("---- Diccionario de ventas ---- ")

ventas = [
    {"fecha":"01-01-2026", "producto":"Sarten", "cantidad":1, "precio":5.2},
    {"fecha":"01-01-2026", "producto":"Olla", "cantidad":3, "precio":7.8},
    {"fecha":"03-01-2026", "producto":"Sarten", "cantidad":2, "precio":5.5},
    {"fecha":"03-01-2026", "producto":"Taza", "cantidad":5, "precio":2.3},
    {"fecha":"04-01-2026", "producto":"Olla", "cantidad":1, "precio":7.6},
]
print(ventas) ; print(" ")


print("---- Ingresos totales ---- ")
def ingresos_totales(diccionario:dict):
    ingreso = 0
    for element in diccionario:
        precioProducto =  element.get("precio")
        cantidadProducto = element.get("cantidad")
        ingreso += precioProducto*cantidadProducto
    return round(ingreso,2)

print("Ingresos Totales:", ingresos_totales(ventas))

print(" ")

print("---- ventas por producto ---- ")

def obtener_total_unidades_vendidas(diccionario:dict):
    uni_olla = 0
    uni_sarten = 0
    uni_taza = 0
    for element in diccionario:
        get_product = element.get("producto")

        if(get_product == "Olla"):
            uni_olla += element.get("cantidad")
        elif(get_product  == "Sarten"):
            uni_sarten += element.get("cantidad")
        elif(get_product  == "Taza"):
            uni_taza += element.get("cantidad")
    return {"Olla":uni_olla, "Sarten":uni_sarten, "Taza":uni_taza}

print("Calculo de items obtenidos: ", obtener_total_unidades_vendidas(ventas))
ventas_por_producto = obtener_total_unidades_vendidas(ventas)
print(" ") 

def producto_mas_vendido(diccionario:dict):
    itemList = list(diccionario.items())
    sortList = sorted(itemList,key=lambda x: x[1], reverse=True) #Como funcionaba esta funcion para este resutlado si tuve que buscarlo.
    print("Lista de productos de mayor a menos por cantidades vendidas:", sortList)
    return sortList[0]

print("producto mas vendido:", producto_mas_vendido(ventas_por_producto))

print(" ")

print("---- Promedio de precio por producto ---- ")

def calculo_unidades_vendidas(diccionario):
    #-- unidades de objetos
    uni_olla = 0
    uni_sarten = 0
    uni_taza = 0

    #-- dinero por venta total
    venta_olla = 0
    venta_sarten = 0
    venta_taza = 0
    for element in diccionario:
        get_product = element.get("producto")
      

        if(get_product == "Olla"):
            uni_del_dia = element.get("cantidad")
            venta_del_dia = element.get("precio")

            uni_olla+= element.get("cantidad")
            venta_olla += uni_del_dia*venta_del_dia
       

        elif(get_product  == "Sarten"):
            uni_del_dia = element.get("cantidad")
            venta_del_dia = element.get("precio")

            uni_sarten += element.get("cantidad")
            venta_sarten += uni_del_dia*venta_del_dia
         


        elif(get_product  == "Taza"):
            uni_del_dia = element.get("cantidad")
            venta_del_dia = element.get("precio")

            uni_taza += element.get("cantidad")
            venta_taza += uni_del_dia*venta_del_dia


    return {"Sarten":(venta_sarten,uni_sarten), "Olla":(venta_olla,uni_olla), "Taza":(venta_taza,uni_taza)}

precios_por_producto = calculo_unidades_vendidas(ventas)
print("precios por productos:", precios_por_producto)

def promedio_venta(diccionario:dict):
    promedio_sarten = 0
    promedio_olla = 0
    promedio_taza = 0
    lista_promedios = []
    for element in diccionario:
        if(element == "Sarten"):
            value = diccionario.get(element)
            promedio_sarten = value[0]/value[1]
           
            
        elif(element == "Olla"):
            value = diccionario.get(element)
            promedio_olla = value[0]/value[1]
          

        elif(element == "Taza"):
            value = diccionario.get(element)
            promedio_taza = value[0]/value[1]
            
    return {"Sarten":round(promedio_sarten,2), "Olla":round(promedio_olla,2), "Taza":round(promedio_taza,2) }

precios_por_producto_promedio = promedio_venta(precios_por_producto)
print("promedio:", precios_por_producto_promedio)

print(" ")


print("---- Ventas por Dia ---- ")

def calcular_ingresos_por_dia(diccionario:dict):
    enero1_ventas = 0
    enero3_ventas = 0
    enero4_ventas = 0

    for element in diccionario:
        get_date = element.get("fecha")

        if(get_date == "01-01-2026"):
            cantidad_dia = element.get("cantidad")
            precio_dia = element.get("precio")
            enero1_ventas += cantidad_dia*precio_dia

        elif(get_date == "03-01-2026"):
            cantidad_dia = element.get("cantidad")
            precio_dia = element.get("precio")
            enero3_ventas += cantidad_dia*precio_dia

        elif(get_date == "04-01-2026"):
            cantidad_dia = element.get("cantidad")
            precio_dia = element.get("precio")
            enero4_ventas += cantidad_dia*precio_dia

    return {"01-01-2026":round(enero1_ventas,2), "03-01-2026":round(enero3_ventas,2), "04-01-2026":round(enero4_ventas,2) }
           

print(calcular_ingresos_por_dia(ventas))

print(" ")
print("---- Representacion de datos ---- ")

def calcular_representacion_datos(precio_por_producto:dict, promedio_venta:dict):
    cantidad = 0
    ingresos = 0
    precio = 0

    resumen = {
        "Sarten":{"cantidad_total":cantidad, "ingresos_totales":ingresos, "precio_promedio":precio},
        "Olla":{"cantidad_total":cantidad, "ingresos_totales":ingresos, "precio_promedio":precio},
        "Taza":{"cantidad_total":cantidad, "ingresos_totales":ingresos, "precio_promedio":precio}
        }

    for element in precios_por_producto:
        if(element == "Sarten"):
            valores = precios_por_producto.get(element)
            resumen["Sarten"]["ingresos_totales"] = valores[0]
            resumen["Sarten"]["cantidad_total"] = valores[1]

        elif(element == "Olla"):
            valores = precios_por_producto.get(element)
            resumen["Olla"]["ingresos_totales"] = valores[0]
            resumen["Olla"]["cantidad_total"] = valores[1]


        elif(element == "Taza"):
            valores = precios_por_producto.get(element)
            resumen["Taza"]["ingresos_totales"] = valores[0]
            resumen["Taza"]["cantidad_total"] = valores[1]
 
    for element in promedio_venta:
        if(element == "Sarten"):
            resumen["Sarten"]["precio_promedio"] = promedio_venta.get(element)
         
        elif(element == "Olla"):
            resumen["Olla"]["precio_promedio"] = promedio_venta.get(element)

        elif(element == "Taza"):
            resumen["Taza"]["precio_promedio"] = promedio_venta.get(element)
        
    return resumen
  

print(calcular_representacion_datos(precios_por_producto, precios_por_producto_promedio))


