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

#esta versión de returnF devuelve la dirección de memoria de una función
def returnF(nombre):
    if nombre in funciones:
        return funciones[nombre]
    return False

#en una instrucción aparte:
returnF('min')(1,-4,3,4,9)
#ejecuta y devuelve -4

#funciones anónimas



    

