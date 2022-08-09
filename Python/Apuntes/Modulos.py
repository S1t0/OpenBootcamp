import Modulos2 as M #El as, es para asignar a Modulos2 la M, asi no hay que escribir toda la palabra
import sys
#Para usar alguan funcion de otro modulo, hay que importarlo
def main():

    res=M.Resta(2,5)
    sum=M.Suma(2,7)

    print("Hola desde el main():",res,sum)
    print(M.Como_me_llamo())#Nos imprime el nombre del modulo M
    
if __name__=="__main__":#aqui le decimos que si el nombre es main, ejecute main, es decir seria el modulo principal

    main()


print(sys.path)#el sys es para acceso a variables del sistema 
  

#Se puede almacenar varios modulos dentro de paquetes, este debe de tener un fichero llamado __init__.py para que python detecte
#que es un paquete, para importarlo se haria: from paquete import modulo
