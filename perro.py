class Dog():
    def __init__(self):
        self.nombre = ""
        self.edad = None
        self.peso = None
        
    def ladrar(self):
        if self.peso == None:
            print("Soy un fantasma")
            
        if self.peso >=8:
            print("GUAU, GUAU")
        else:
            print("guau, guau")


class Perro():
    def __init__(self, n, e, p):
        self.nombre = n # A esta clase, en el atributo nombre le pones la variable de entrada nombre
        self.edad = e
        self.peso = p
    
    def ladrar(self): # Por convenio ponemos self para que se entienda que el primer parámetro de los métodos de una clase siempre es la propia clase
        if self.peso >=8:
            print("GUAU, GUAU")
        else:
            print("guau, guau")
    
    def __str__(self):
        return "Perro {}, e: {}, p: {}".format(self.nombre, self.edad, self.peso)


class PerroAsistencia(Perro): # Con esto Python ya sabe que PerroAsistencia es una subclase que va a heredar de Perro
    trabajando = False
    def __init__(self, nombre, edad, peso, amo):
        Perro.__init__(self, nombre, edad, peso)
        self.amo = amo
        
    def __str__(self):
        return "Perro de asistencia de {}".format(self.amo) # Sobreescribir un método el __str__ de Perro
    
    def pasear(self):
        print("{} ayudo a mi dueño, {} a pasear".format(self.nombre, self.amo))
        
    def ladrar(self):
        if self.__trabajando:
            print("shhhh, no puedo ladrar")
        else:
            Perro.ladrar(self)
            
    def trabajando(self, valor=None): # Aquí creamos un método trabajando, self lo informamos porque es la instancia, como parámetro utilizamos el valor que si no se informa le doy el valor None(el valor nulo)
        if valor == None:
            return self.__trabajando
        else:
            self.__trabajando = valor
        
        
    
    