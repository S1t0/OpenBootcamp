
numero=int(input("Introduce el numero entero "))
    
#lo hacemos con un for, y asi recorremos desde el numero 2 hasta el numero que pongamos, probando las divisiones con todos


def esPrimo(numero):
    if numero<2:
        print("El numero",numero,"es primo")
    for i in range(2,numero):
        if numero%i==0:
            return False  
        return True


final= esPrimo(numero)#lo almacenamos en una variable para poder comprobar despues si es True o False

if final==True:
    print("El numero",numero,"es primo")
else:
    print("El numero",numero,"no es primo")


