class Perro: #el nombre de una clase siempre ha de comenzar con mayúsculas

    def __init__(self, nombre, edad, peso): #función constructora de la instancia (inicializa el estado del objeto, o sea, sus atributos)
        self.nombre = nombre
        self.edad = edad
        self.peso = peso

    def ladrar(self): #OJO: en Python el primer parámetro de un método siempre es la propia clase (self' ó 'me')       
        if self.peso >= 8:
            print('GUAU,GUAU!')
        else:
            print('guau,guau!')

    def __str__(self):
        return "Perro {}, e:{}, p:{}".format(self.nombre, self.edad, self.peso)

    
#def ladrar():
#    print("No soy un perro!")


bobby = Perro('Bobby',2,8)

#bobby.ladrar()    
#ladrar()

#subclase 'PerroAsistencia' hereda los atributos y métodos de Perro y agrega las suyas':

class PerroAsistencia(Perro):

    def __init__(self, nombre, edad, peso, amo): #constructor de la subclase
        Perro.__init__(self, nombre, edad, peso) #llama al constructor del padre
        self.amo = amo
        self.ocupado = False
        
    def __str__(self): #sobreescribe el método 'str' de Perro
        return "Perro de asistencia de {}".format(self.amo)

    def pasear(self):
        print("Ayudo a mi dueño {} a pasear".format(self.amo))
        

    def ladrar(self): #sobreescribe el método ladrar
        if self.ocupado:
            print("No puedo ladrar ahora")
        else:
            Perro.ladrar(self) #pero invoca condicionalmente al método del padre 
            
        
    
lassie = PerroAsistencia('Lassie', 5, 10, 'Joe')



#------creación de objeto sin atributos por defecto

class Dog():
    def __init__(self):
        self.nombre = ""
        self.edad = None
        self.peso = None

    def ladrar(self):
        if self.peso == None:
            print("Soy un fantasma")
        elif self.peso >= 8:
            print('GUAU,GUAU!')
        else:
            print('guau,guau!') 

tyson = Dog()

