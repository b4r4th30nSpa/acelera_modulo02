class Termometro:

    def __init__(self):         
        self.__unidad = 'C'     #atributos privados
        self.__temperatura = 0  #atributos privados

    def __str__(self):
        return '{}º {}'.format(self.__temperatura, self.__unidad)

    def __conversor(self,temperatura,u): #método de apariencia privada (pues en Python realmente no existen los métodos privados)
        if u =='C':
            return '{}º F'.format(temperatura*9/5+32)
        elif u== 'F':
            return '{}º C'.format((temperatura-32)*5/9)
        else:
            return "Unidad incorrecta"

    def unidadMedida(self,uni=None):  #método getter/setter de la unidad de medida
        if uni == None:
            return self.__unidad
        else:
            if uni =='C' or uni =='F':
                self.__unidad = uni
                return self.__unidad 

    def temp(self, temperatura):  #método getter/setter de la temperatura
        if temperatura == None:
            return self.__temperatura
        else:
            self.__temperatura = temperatura
                    

    def medir(self,unidad=None):  
        if unidad == None or unidad == self.__unidad:
            return self.__str__()
        else:
            if unidad == 'C' or unidad == 'F':
                return self.__conversor(self.__temperatura, self.__unidad)
            else:
                return self.__str__()
        
    
                      
            
t = Termometro()



