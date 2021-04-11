
# creamos una función que nos devuelva el máximo de los parámetros de entrada
def maxi(*l): # Cuando poníamos esta forma de poner los parámetros lo que estabamos diciendo es, coge todos los parametros que yo te meta separados por comas y me los procesas como si fuera un array, es decir, l es un array.
    if len(l) == 0:
        return 0

    m = l[0]

    for ix in range(1, len(l)):
        if l[ix] > m:
            m = l[ix]
    
    return m


def mini(*l):
    if len(l) == 0:
        return 0
    
    m = l[0]
    
    for ix in range(1, len(l)):
        if l[ix] < m:
            m = l[ix]
    return m


def media(*l):
    if len(l) == 0:
        return 0
    suma = 0
    for valor in l:
        suma += valor
        
    return suma / len(l)

funciones = {
    'max': maxi,
    'min': mini,
    'med': media
}


def returnF(nombre):
    nombre = nombre.lower()
    if nombre.lower() in funciones.keys():
        return funciones[nombre]
    return None
    