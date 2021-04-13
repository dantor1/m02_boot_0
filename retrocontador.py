def retrocontador(e):
    print("{},".format(e), end="")
    if e > 0:
        retrocontador(e-1) # y ahora te digo que te llames a ti misma
    
retrocontador(10)


