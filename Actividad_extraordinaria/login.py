#Declaración de variables
Users = ["test@gmail.com", "javieralvarezserrano@gmail.com", "admin"]
Passwords = ["1234","uem2020","admin"]
Usernames = ["test", "Javier Álvarez Serrano","admin"]
user_aux = "a"

#Variables usadas por el usuario
usuario=input('Email: ')
passw = input('Password: ')

#Declaración de la función que verifica si el usuario y contraseña son correctos.
def login(usuario,passw):
    auxiliar = 0;
    global user_aux
    for x in Users:
        if x == usuario:
            if Passwords[auxiliar]==passw:
                user_aux = Usernames[auxiliar]
                print("")
                return 1
        auxiliar+=1
    return 2

def elegir(opcion):
    if opcion == "A":
        #mergesort()
        print("merge")
    elif opcion == "B":
        #fibonacci()
        print("fibo")
    else:
        opcion=input("Seleccione el ejercicio que desea ejecutar")
        elegir(opcion)




if login(usuario,passw)==1:
    print("*****UNIVERSIDAD EUROPEA DE MADRID *********")
    print("Escuela de Ingeniería, Arquitectura y Diseño")
    print("********************MENU********************")
    print("\n"+ user_aux,"\n")
    print("         A: Ejercicio A")
    print("         B: Ejercicio B\n")
    opcion=input("Seleccione el ejercicio que desea ejecutar")
    elegir(opcion)
else:   
    print('No autorizado.')