

#------de vuelta a 'PerroAsistencia'

class Perro: 

    def __init__(self, nombre, edad, peso): 
        self.nombre = nombre
        self.edad = edad
        self.peso = peso

    def ladrar(self):       
        if self.peso >= 8:
            print('GUAU,GUAU!')
        else:
            print('guau,guau!')

    def __str__(self):
        return "Perro {}, e:{}, p:{}".format(self.nombre, self.edad, self.peso)

#------crear una función 'ocupado' que gestiona este atributo como un método:

class PerroAsistencia(Perro):

    def __init__(self, nombre, edad, peso, amo): 
        Perro.__init__(self, nombre, edad, peso)
        self.amo = amo
        self.__ocupado = False  #redefine el atributo 'ocupado' que pasa a depender de un nuevo método 
#'.__' denota un atributo privado (no acessible desde fuera de la clase). En este caso no es realmente privado, pero Python simula que lo es

    def __str__(self): 
        return "Perro de asistencia de {}".format(self.amo)

    def pasear(self):
        print("Ayudo a mi dueño {} a pasear".format(self.amo))
        
    def ocupado(self, valor=None): #crea nuevo método 'ocupado' (es un método 'getter' en un caso y un método 'setter' en el otro)
        if valor == None:
            return self.__ocupado
        else:
            self.__ocupado = valor
        
    def ladrar(self): 
        if self.__ocupado:
            print("No puedo ladrar ahora")
        else:
            Perro.ladrar(self) 

         
lassie = PerroAsistencia('Lassie', 5, 10, 'Joe')
lassie.ocupado() #al invocarlo así es un método 'getter'
lassie.ocupado(True) #al invocarlo así es un método 'setter'

lassie.__ocupado() #al invocarlo así dirá que no existe el método (ya que Python asume que es un método privado)
lassie._PerroAsistencia__ocupado() #pero al invocarlo así si lo ejecuta, ya que Python realmente NO tiene métodos privados
 




