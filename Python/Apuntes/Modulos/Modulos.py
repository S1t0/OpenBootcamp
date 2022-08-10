import math
import Modulos2 as M #El as, es para asignar a Modulos2 la M, asi no hay que escribir toda la palabra
#Para usar alguan funcion de otro modulo, hay que importarlo
import sys
import pprint
def main():

    res=M.Resta(2,5)
    sum=M.Suma(2,7)

    print("Hola desde el main():",res,sum)
    print(M.Como_me_llamo())#Nos imprime el nombre del modulo M

    
 

    
if __name__=="__main__":#aqui le decimos que si el nombre es main, ejecute main, es decir seria el modulo principal

    main()


print(sys.path)#el sys es para acceso a variables del sistema 
#pprint.pprint(dir(math))#aqui vemos todos lo que trae math, con dir podemos ver las funciones de cada modulo


#Se puede almacenar varios modulos dentro de paquetes, este debe de tener un fichero llamado __init__.py para que python detecte
#que es un paquete, para importarlo se haria: from paquete import modulo

#si queremos importar mas de un paquete, en lugar de escribirlos uno a uno, en el modulo __init__.py, dentro escribimos
#__all__=["nombre del paquete","nombre del paquete"], asi al hacer un from paquete import *, el * importa todos los paquetes 
#que tengamos definidos en la lista de all.
