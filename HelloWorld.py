import sys;
import threading;

CONST_DEFAULT_THREAD_COUNT = 5                              # Cuenta de hilo predeterminada constante

#inicio clase Panadería
class Bakery:
    #Creación de arreglos/inicialización de variables
    choosing = [] #selecciona 0 o 1
    num = [] #indica el número
    nThreads = 0 #cantidad de hilos
    
    def setup(self):
        for i in range(self.nThreads + 1):                  #número de hilos
            self.choosing.append(0)                         #añade el valor al final de la lista choosing inicializa la lista
            self.num.append(0)                              #añade el valor al final de la lista num inicializa la lista
   
    #Creamos el método tarea
    def task(self, threadID):
        print (str(threadID) + " executing task")           #imprime que hilo esta ejecutando la tarea
       
    # Creamos el método cs que toma un objeto del método tarea y la utiliza en la sección crítica
    def cs(self, threadID):
       
        #Cálcula el número de turno
        try:
            self.choosing[threadID] = 1                     #se asigna a choosing el valor de 1 refiriendose a verdadero
             
            self.num[threadID] = 1 + max(self.num)          #se asigna a la lista num el valor máximo de la misma lista + 1
           
            maxValue = self.num[threadID]                   # se crea la variable maxValue en base al resultado anterior
           
            print ("Thread id " + str(threadID) + " assigned Token: " + str(maxValue))
                   
            self.choosing[threadID] = 0                     #se asigna a choosing el valor de 0 refiriendose a falso

            #Compara con todos los hilos

            for i in range (self.nThreads):              
                if i != threadID:
                    while self.choosing[i] != 0:
                        pass
       
                    while (self.num[i] != 0 and (self.num[threadID] > self.num[i] or (self.num[i] == self.num[threadID] and threadID > i))):
                        pass
           
            print (str(threadID) + " entering CS with Token Number: " + str(self.num[threadID]))
           
            # Sección crítica
            self.task(threadID)

            print (str(threadID) + " exiting CS With Token number: " + str(self.num[threadID])); 

            # Reinicia el valor del ID del Hilo
            self.num[threadID] = 0
           
        except:
            print ("Exception: In class bakery.cs() method")
               
             
    def main(self, threadID):
       
        while True:
            print (str(threadID) + " requesting CS. Token not assigned yet")
            self.cs(threadID)
           
    # Configuración del método que toma el conjunto de todos los objetos de subproceso y el número total de solicitudes
    # e inicializa las variables compartidas por el algoritmo

def setup(nThreads):
   
    bakeryInstance = Bakery()                                   #Crea la instancia de la clase Bakery
    bakeryInstance.nThreads = nThreads
   
    # Call the Bakery setup method
    bakeryInstance.setup()                                      #Inicializa el método setup
   
    print ("Running Lamport's bakery algorithm")
    
   #Realiza la cuenta de hilos a ejecutar en tareas
    try:

        for count in range(nThreads):
            newThread = threading.Thread(target=bakeryInstance.main, args=[count])
            newThread.start()
   
    except:
       print ('Error: unable to start thread')
               
def main():
   
    #Información de las variables usadas
    nThreads = 0; # Cantidad de hilos
   
    # Definir un valor por defecto a la cantidad de hilos y pedidos
    try:
        if len(sys.argv) > 1:
            nThreads = int(sys.argv[1])
        else:
            nThreads = CONST_DEFAULT_THREAD_COUNT
           
    except (ValueError, IndexError):
        nThreads = CONST_DEFAULT_THREAD_COUNT
       
    print (nThreads)

    #Create the threads
    setup(nThreads)

#Call the main method  
main()