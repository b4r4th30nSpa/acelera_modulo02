#una función recursiva puede invocarse a sí misma

def countDown(entrada):
    print('{}'.format(entrada),",")
    countDown(entrada-1)

#aquí crea un bucle infinito...
    
#la recursividad supone un trade off entre elegancia y eficacia/eficiencia
#las funciones recursivas pueden dar problemas

#corrección para evitar bucle infinito:
    
def countDown(entrada):
    print('{}'.format(entrada),",")
    if entrada > 0:
        countDown(entrada-1)

           
print(countDown(10))

#Nota: un bucle WHILE infinito 'no congela' el ordenador,
#mientras que una funcion recursiva infinita sí

def sumatorio(n): 
    if n > 0:
        return n + sumatorio(n-1)
    else:
        return 0
  

print(sumatorio(4))

def factorial(n):
    if n > 0:
        return n*factorial(n-1)
    else:
        return 1


