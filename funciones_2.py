 
#operador MAP   ----map(function, iterable,...)
#aplica function a cada item en iterable

lista = [1,4,-5,7,2]

listaDobles = map(lambda x: x*2, lista)

#to print a map object it must be turned into a list or tuple first:
print(list(listaDobles))

#operador FILTER ----filter(function, iterable,...)
#aplica function a cada item en iterable para el cual function(iterable)==TRUE

listaPares = filter(lambda x: x%2==0,lista)

print(list(listaPares))

from functools import reduce #reduce no es una built-in function
#en general 'reduce' colapsa un iterable en un sólo valor
#en particular, aquí reduce  suma manera acumulativa elementos de un iterable
#ojo, en python reduce falla en la primera iteración (pues no aplica la función al primer item),
#de ahí que Van Rossum decidiese que reduce no fuese builtin sino que hay que importarlo


sumatorio = reduce(lambda x,y: x+y, lista)

print(sumatorio)

#para 'clonar' una lista usar copialista=viejalista[:],
#de lo contrario la copia es por referencia (no por valor, o sea, no clona)

a = [1,2]
b = a
b.append(3)
print(b == a)
#True

#en cambio:
c = a[:]
c.append(3)
print(c == a)

