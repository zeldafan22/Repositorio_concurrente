###################################################################
                        # Codigo para calcular el tiempo de fibonacci usando varios cores #
                        ###################################################################
import time

#Iterativo
def fib(n):
    a = 0
    b = 1
    
    for k in range(n):
        c = b+a
        a = b
        b = c
    return a

if __name__ == "__main__":
    n = 21839430
    inicio = time.time()
    print(fib(n))
    fin = time.time()
    print("Tiempo de ejecución SECUENCIAL = ", fin - inicio)