#----------------------
#función de orden superior 'returnF' 

def maxi(*l):
    if len(l)==0:
        return 0
    m = l[0]
    for i in range(1,len(l)):
        if l[i] > m:
            m = l[i]
    return m


def mini(*l):
    if len(l)==0:
        return 0
    m = l[0]
    for i in range(1,len(l)):
        if l[i] < m:
            m = l[i]
    return m

def media(*l):
    suma=0
    for i in l:
        suma += i
    return suma/len(l)

funciones = {'max':maxi,
    'min':mini,
    'med':media
    }

#returnF devuelve la dirección de memoria de una función

def returnF(nombre):
    if nombre in funciones:
        return funciones[nombre]
    return False

#en una instrucción aparte:
returnF('min')(1,-4,3,4,9)
#ejecuta y devuelve -4


#----------------------------


def normal(x):
    return x


#sumatoria de la sucesión de 0 a 'hasta'
#notar que la función recibe unna función 'f' como parámetro (es de orden superior)

def sumaTodos(hasta, f):
    suma = 0
    for i in range(0,hasta+1):
        suma += f(i)
    return suma

#FUNCIONES ANÓNIMAS pasadas como parámetros (llamadas 'lambdas' en python)
#paso a sumaTodos una lambda (keyword de Python) como parámetro
#(en este caso es una función cúbica):

print(sumaTodos(3, lambda x: x**3))
#notar que tras ':' está, primero, el parámetro (x),
#si son varios se separan con ',', y luego
#el bloque que define la función anónima ('x**3')

#esta función anónima me ahorra tener que definir una función 'cubo'


    
    



    

