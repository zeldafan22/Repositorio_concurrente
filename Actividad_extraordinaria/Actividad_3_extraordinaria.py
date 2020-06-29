from multiprocessing import Pool
import time
import sys
import multiprocessing
from random import randint

#Imports utilizados:
#  - time para calcular el tiempo que tarda el programa en ejecutarse
#  - multiprocessing para calcular el numero de cores


#Variable global
numero_expediente = 2183
NC = multiprocessing.cpu_count()

#Declaración de variables
Users = ["test@gmail.com", "javieralvarezserrano@gmail.com", "admin"]
Passwords = ["1234","uem2020","admin"]
Usernames = ["test", "Javier Álvarez Serrano","admin"]
user_aux = "a"


def main(): #Función que se ejecuta al iniciar el programa
    menu()

#Declaración de la función que verifica si el usuario y contraseña son correctos.
def login(usuario,passw):
    auxiliar = 0;
    global user_aux
    for pos in Users:                              #Recorre el array de usuarios
        if pos == usuario:                         #Si el nombre de usuario coincide con un nombre del array de usuarios,
            if Passwords[auxiliar]==passw:       #se comprueba si la contraseña es correcta.
                user_aux = Usernames[auxiliar]
                print("")
                return 1
        auxiliar+=1
    return 2

def elegir(opcion):         #Función del menú, una vez se ha conectado el usuario, se elige opción a ejecutar.
    if opcion == "A":       #Si se elige la primera opcion se ejecuta el mergesort paralelo
        llamada_mergesort(numero_expediente)
    elif opcion == "B":     #Si se elige la segunda opcion se ejecuta fibonacci 
        llamada_fib(numero_expediente)
    else:                   #Si se introduce cualquier otra cosa te pide que vuelvas  a intentarlo.
        opcion=input("Seleccione el ejercicio que desea ejecutar\n")
        elegir(opcion)

def menu():
    #Variables usadas por el usuario
    usuario=input('Email: ')
    passw = input('Password: ')
    if login(usuario,passw)==1:
        print("*****UNIVERSIDAD EUROPEA DE MADRID *********")
        print("Escuela de Ingeniería, Arquitectura y Diseño")
        print("********************MENU********************")
        print("\n"+ user_aux,"\n")
        print("         A: Ejercicio A")
        print("         B: Ejercicio B\n")
        opcion=input("Seleccione el ejercicio que desea ejecutar\n")
        elegir(opcion)
    else:   
        print('No autorizado.')

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

def mergeSortParallel(array, NC):
    
    
    numproc = 2**(int(NC/2)-1)
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

    #Método con todo lo necesario para ejecutar el ejercico de mergesort al que se llamara desde el menu.
def llamada_mergesort(numero_expediente):

    #A continuación deberíamos leer el número de cores usando multiprocessing.cpu_count()

    array = []                              #creación del array 
    for a in range(0, numero_expediente):   #bucle for que se repite tantas veces como el valor de "numero_expediente"
        b = randint(1,2000000)              #creación de un int aleatorio entre 1 y 2000000
        array.insert(a,b)                   #Inserción de ese número recién creado en el array

    # el código debe ejecutarse en cualquier máquina conforme se especifica en el enunciado, da igual si tienes seis o 300 cores deberás distribuirlos de forma eficiente en relación al problema que estés resolviendo
    print('Array formado por ', numero_expediente, ' numeros aleatorios creado.')
    inicio = time.time()                    #Se guarda el instante de tiempo justo antes de la ejecución del programa para ser usado
    array = mergeSortParallel(array, NC)     #Se ejecuta el MergeSort en paralelo 
    fin = time.time() - inicio              #Se calcula el instante de tiempo que ha pasado entre inicio y fin del programa
    time.sleep(5) #Pausa de cinco segundos para poder apreciar el tamaño del array antes de imprimirse por pantalla
    print('\n Array anterior de forma ordenada;', array)
    time.sleep(2) #Pausa de dos segundos entre la impresión del array y el tiempo que ha tardado en ordenarse el array.
    print('\n El array de ', numero_expediente, 'números ha sido ordenado mediante el uso de MergeSort en paralelo (en función de los ', multiprocessing.cpu_count(), ' cores lógicos de esta máquina) en %f segundos' % (fin))

#Método de fibonacci que se ejecuta de manera secuencial
def fib(n):
    a = 0
    b = 1
    
    for k in range(n):
        c = b+a
        a = b
        b = c
    return a

#Método con todo lo necesario para ejecutar el ejercico de fibonacci al que se llamara desde el menu.
def llamada_fib(n):
    inicio_fib = time.time()
    auxiliar_fib = fib(n)
    fin_fib = time.time()
    print(auxiliar_fib)
    print("Se han tardado ", fin_fib-inicio_fib, " segundos en realizar fibonacci de ", n, "de forma secuencial.")
    #Se ejecuta el main cuando termina el programa
if __name__ == '__main__':
    main()
