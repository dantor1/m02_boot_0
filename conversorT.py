class Termometro():
    def __init__(self):
        self.__unidadM = 'C'
        self.__temperatura = 0

    
    def __str__(self):
        return"{}º {}".format(self.__temperatura, self.__unidadM)
    
    def unidadMedida(self, uniM=None): # Aquí hay un getter y un setter
        if uniM == None:
            return self.__unidadM
        else:
            if uniM == 'F' or uniM == 'C':
                self.__unidadM = uniM

    def temp(self, temperatura=None): # Aquí hay un getter y un setter
        if temperatura == None:
            return self.__temperatura
        else:
            self.__temperatura = temperatura

        
    def __conversor(self, temperatura, unidad): # Este es un método interno que devuelve la conversión
        if unidad == 'C':
            return "{}º F".format(temperatura * 9/5 + 32)
        if unidad == 'F':
            return "{}º C".format((temperatura -32) * 5/9)
        else:
            return "unidad incorrecta"
                        
    def mide(self, uniM=None):
        if uniM == None or uniM == self.unidadM: # Si coincide o no está informado me das lo que ya tengo,
            return self.__str__()
        else:
            if uniM == 'F' or uniM == 'C':
                return self.__conversor(self.__temperatura, self.__unidadM) # y si no coincide me haces la conversión
            else:
                return self.__str__()
            
                                    