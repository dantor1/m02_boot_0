from functools import reduce

lista = [1, 3, -1, 15, 9]

def doble(x):
    return x + x

listaDobles = map(lambda x: x*2, lista) 
listaDobles1 = map(doble, lista) # es lamisma que listaDobles pero sin meter lambda y definiendo previamente una función


def esPar(x):
    return x % 2 == 0

listaPares = filter(lambda x: x % 2 == 0, lista)
listaPares1 = filter(esPar, lista) # es lamisma que listaPares pero sin meter lambda y definiendo previamente una función


sumatorio = reduce(lambda x, y: x + y, lista) # reduce me va a reducir toda la lista a un solo valor

# Creo una copia de la lista
l = lista[:]
# añado el neutro para la suma en la posición ceco
l.insert(0,0)
sumatorioDobles = reduce(lambda x, y: x + y*2, l) 

suma100 = reduce(lambda x, y: x + y, range(101))

print(list(listaPares))
print(list(listaPares1))

print(sumatorio)
print(sumatorioDobles)

print(suma100)
