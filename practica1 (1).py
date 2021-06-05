# Crear un programa que utilizando lo aprendido de python, permita crear un menu de opciones y
# seleccionar la deseada.

# MENU:
# 1. Calcular el área de un círculo
# 2. Calcular los días transcurridos de una fecha
# 3. Ordenar un diccionario de datos

# Tips:

# - Saber como leer desde teclado:
#   input("Mensaje") # python 3.6
#   raw_input("Mensaje") # python 2.7

# - Calcular fechas:
#   import datetime
#   datetime.datetime.now()

def calcularAreaCirculo():
    # area = pi * radio ** 2
    radio = float( input("Ingresa el radio del círculo: ") )
    area = 3.1416 * radio ** 2
    print("El área del círculo es: " + str(area))

def calcularDiasTranscurridos():
    from datetime import datetime
    fecha_actual = datetime.now()
    fecha_evaluar = datetime.strptime( input("Ingrese una fecha (ej. 1900-12-31): "), '%Y-%m-%d' )
    dias = fecha_actual - fecha_evaluar
    print("Dias transcurridos: " + str(dias))

def calcularDiasTranscurridos2():
    import datetime
    fecha_actual = datetime.datetime.now()
    fecha_ano = int( input("Ingrese el año de una fecha: ") )
    fecha_mes = int( input("Ingrese el mes de una fecha: ") )
    fecha_dia = int( input("Ingrese el dia de una fecha: ") )
    fecha_evaluar = datetime.datetime(fecha_ano,fecha_mes,fecha_dia)
    dias = fecha_actual - fecha_evaluar
    print("Dias transcurridos: " + str(dias))

def ordenarDiccionarioEtiqueta():
    calificaciones = {
        "Noe": 8.7,
        "Candelario": 9,
        "Alba": 9.3,
        "Wendy": 8.5,
        "Jose": 9,
        "Andrea": 8.9
    }
    print(calificaciones)

    etiquetas = sorted(calificaciones.items())
    print(etiquetas)

    calificaciones_ord = {}
    for x in etiquetas:
        calificaciones_ord.update( {x[0]: x[1]} )
    print(calificaciones_ord)

def ordenarDiccionarioValor():
    calificaciones = {
        "Noe": 8.7,
        "Candelario": 9,
        "Alba": 9.3,
        "Wendy": 8.5,
        "Jose": 9,
        "Andrea": 8.9
    }
    print(calificaciones)

    lista = []
    for x in calificaciones:
        lista.append( (calificaciones[x], x) )
    lista.sort()
    print(lista)

    calificaciones_ord = {}
    for x in lista:
        calificaciones_ord.update( {x[1]: x[0]} )
    print(calificaciones_ord)

print("MENU:")
print("1. Calcular el área de un círculo")
print("2. Calcular los días transcurridos de una fecha")
print("3. Ordenar un diccionario de datos")
opc = int( input("Opción: ") )

#if opc==1:
#    calcularAreaCirculo()
#else:
#    if opc==2:
#        calcularDiasTranscurridos()
#    else:
#        if opc==3:
#            ordenarDiccionario()
#        else:
#            print("Opción incorrecta.")

if opc==1:
    calcularAreaCirculo()
if opc==2:
    calcularDiasTranscurridos()
if opc==3:
    ordenarDiccionarioEtiqueta()
    ordenarDiccionarioValor()
if opc<1 or opc>3:
    print("Opción incorrecta.")
