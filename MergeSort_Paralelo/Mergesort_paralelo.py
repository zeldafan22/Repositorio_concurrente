from multiprocessing import Pool
import time
import sys
import multiprocessing
from random import randint

#Imports utilizados:
#  - time para calcular el tiempo que tarda el programa en ejecutarse
#  - multiprocessing para calcular el numero de cores

def main():

    numero_expediente = 21839430            #numero de elementos que tendrá el array 
    array = []                              #creación del array 
    for a in range(0, numero_expediente):   #bucle for que se repite tantas veces como el valor de "numero_expediente"
        b = randint(1,2000000)              #creación de un int aleatorio entre 1 y 2000000
        array.insert(a,b)                   #Inserción de ese número recién creado en el array

    
    #A continuación deberíamos leer el número de cores usando multiprocessing.cpu_count(), pero en mi caso tengo problemas ya que tengo
    # un n úmero de cores físicos inusual (6 cores, que tienen un total de 12 cores lógicos) así que los he introducido a mano (n= 6)
    n = 6 
   # el código debe ejecutarse en cualquier máquina conforme se especifica en el enunciado, da igual si tienes seis o 300 cores deberás distribuirlos de forma eficiente en relación al problema que estés resolviendo
    print('Array formado por ', numero_expediente, ' numeros aleatorios creado.')
    inicio = time.time()                    #Se guarda el instante de tiempo justo antes de la ejecución del programa para ser usado
    array = mergeSortParallel(array, n)     #Se ejecuta el MergeSort en paralelo 
    fin = time.time() - inicio              #Se calcula el instante de tiempo que ha pasado entre inicio y fin del programa
    time.sleep(5) #Pausa de dos segundos para poder apreciar el tamaño del array antes de imprimirse por pantalla
    print('\n Array anterior de forma ordenada;', array)
    time.sleep(2) #Pausa de dos segundos entre la impresión del array y el tiempo que ha tardado en ordenarse el array.
    print('\n El array de ', numero_expediente, 'números ha sido ordenado mediante el uso de MergeSort en paralelo (en función de los ', multiprocessing.cpu_count(), ' cores lógicos de esta máquina) en %f segundos' % (fin))


def merge(left, right):     #Devuelve el array ya ordenado de las dos mitades del array ya ordenadas
    ret = []
    li = ri = 0             #Índices de los arrays divididos en el método mergesort()
    while li < len(left) and ri < len(right):
        if left[li] <= right[ri]:
            ret.append(left[li])
            li += 1
        else:
            ret.append(right[ri])
            ri += 1
    if li == len(left):
        ret.extend(right[ri:])
    else:
        ret.extend(left[li:])
    return ret

def mergesort(array):           #Método que divide el array en dos mitades con el mismo numero de elementos
    
    if len(array) <= 1:
        return array
    ind = len(array)//2
    return merge(mergesort(array[:ind]), mergesort(array[ind:]))

def mergeWrap(AyB):
    a,b = AyB
    return merge(a,b)

def mergeSortParallel(array, n):
    
    
    numproc = 2**n
    #Se distribuyen de forma equitativa los índices de los diferentes fragmentos del array original
    endpoints = [int(x) for x in linspace(0, len(array), numproc+1)]
    args = [array[endpoints[i]:endpoints[i+1]] for i in range(numproc)]

    #Se crea un pool de procesos con tantos procesos como cores lógicos haya disponibles
    pool = Pool(processes = numproc)
    sortedsublists = pool.map(mergesort, args)
    #Se utiliza mergesort() para ir ordenando cada uno de los fragmentos del array original

    #Se combinan los fragmento del array original por parejas siempre y cuando haya más de un fragmento 
    while len(sortedsublists) > 1:
        args = [(sortedsublists[i], sortedsublists[i+1]) \
                for i in range(0, len(sortedsublists), 2)]
        sortedsublists = pool.map(mergeWrap, args)

    return sortedsublists[0]
    
def linspace(a,b,nsteps):
    
    #returns list of simple linear steps from a to b in nsteps.          Comentario del autor del código que no entiendo del todo.

    ssize = float(b-a)/(nsteps-1)
    return [a + i*ssize for i in range(nsteps)]

    #Se ejecuta el main cuando termina el programa
if __name__ == '__main__':
    main()
