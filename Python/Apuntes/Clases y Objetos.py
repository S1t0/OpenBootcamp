class Dino:#Esta seria una clase dinamica, cada instancia tiene su espacio de memoria
    _encendido=True
    def enciende(self):
        self._encendido=True

    def apaga(self):#la palabra self hace referencia a la variable dentro de mi clase
                    #si no usamos self, crearia una variable en la funcion y no modificaria la de mi clase
        self._encendido=False

    def isEncendido(self):
        return self._encendido

#instanciamos la clase

d=Dino()
d.apaga()
print(d._encendido)

class Estatica:# esta solo tiene un espacio de memoria para todo, ya que no estamos instanciando la clase
    numero=1

    def incrementa():
        Estatica.numero+=1
    
Estatica.incrementa()
print(Estatica.numero)

Estatica.incrementa()
print(Estatica.numero)

Estatica.incrementa()
print(Estatica.numero)

class Opciones:#las clases esticas sirve para opciones, modelos de datos, algo que no vamos a necesitar instancias de ella
    ServidorSeguro=True
    Reiniciar=False

# if Opciones.ServidorSeguro:
    #codigo

#HERENCIA 
#Para herededar de otra clase se pone entre parentesis el nombre de la que hereda

class Juguete(Dino):
    def verTamaño(self):
        pass

    def __init__(self,nombre):#Este es el constructor de la clase, siempre tiene que llamarse __init__
        print("ESTOY EN EL CONSTRUCTOR",nombre)

    def __del__(self):#Este es el destructor 
        print("ESTOY EN EL DESTRUCTOR DE LA CLASE")

j=Juguete("Andres") #Le pasamos parametro ya que tenemos un constructor
                    #Juguete hereda los metodos de Dino y podemos usarlos 
j.apaga()
j.isEncendido()    

#Para ver todo lo que tenemos dentro de una clase, usamos la palabra dir


print(dir(j))

#Clases abstractas
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sonido(self):
        pass

#una clase abstracta no podemos instanciarla, pero si podemos instanciar
#las clases que hereden de ella


#LA COMPOSICION, RELACIOENS HAS-A
#La composicion es que una clase esta compuesta de otras clases.




class Motor:
    tipo="Diesel"
 
class Ventanas:
    cantidad=5

class Ruedas:
    cantidad=4

class Carroceria:
    ventanas=Ventanas()
    ruedas=Ruedas()

class Coche:
    motor=Motor()
    carroceria=Carroceria()


c=Coche()

print(c.motor.tipo)
print(c.carroceria.ventanas.cantidad)


#Tambien podemos hacer otra cosa, que una clase 