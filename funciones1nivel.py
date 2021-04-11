def normal(x):
    return x

def cuadrado(x):
    return x * x

def sumaTodos(limitTo, f): # f va a contener la referencia a la función que quiero realizar
    resultado = 0
    for i in range(limitTo+1):
        resultado += f(i) # A resultado ¿qué le voy a sumar? Respuesta: La aplicación de la función f sobre i
    
    return resultado

print(sumaTodos(100, normal))
print(sumaTodos(3, cuadrado))