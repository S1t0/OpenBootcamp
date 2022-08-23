numero=55
texto="quijote"
decimal=1.2

#print("El numero es %d el texto es %s y  decimal es %f"(numero,texto,decimal))//antes se imprimia asi, en python3.6, pero ya no, 
print("El numero es {2} el texto es {0} y  decimal es {1}".format(numero,texto,decimal))#esta es otra forma, a partir de python3.6
#ccon el numero entre los corchetes ponemos el orden que queremos que salga.si no le ponemos nada sale conforme esta en la lista

print("El numero es {n1} el texto es {text} y  decimal es {otro}".format(n1=numero,text=texto,otro=decimal))

#hay otras formas como las f-strings

print(f"El numero es {numero} y el texto es {texto} tiene de decimales {decimal}")


class Juguete:
    nombre:None #None se puede usar para no darle valor a una variable cuando la iniciamos
    precio:0.0

    def __init__(self,nombre,precio):
        self.nombre=nombre
        self.precio=precio

    def __str__(self): #el str nos saca codigo por defecto como lo hace python
        return f"Mi nombre es {self.nombre},y mi precio es {self.precio}"

    def __repr__(self): #con este repr sacamos salidas de codigo tecnicas, no como el str.
        return f"Potato({self.nombre},{self.precio})"

j1=Juguete("Potato",10.15)
print(str(j1))
print(repr(j1)) #si no tenemos la clase def rpr, nos sacaria por pantalla otra cosa.


#import pprint
#pprint.pprint(dir("")) #nos saca todos los metodos de un string ""

cadena="Es una cadena de prueba"
cadena2="      ES OTRA CADENA DE PRUEBA          "
numero="5"
print(cadena.count("a")) #Cuenta cuantas palabras o letras hay en la cadena
print(cadena.upper())
print(numero.isdigit())#nos devuelve true o false si es o no un numero
print(cadena2.strip())#elimina los espacios del principio y del final
print(cadena.split())#convierte un string en un array
print(cadena.split("cadena"))


#para manipular ficheros o abrirlos se hace asi
#f = open("nombre del fichero","permiso")
#persimos o modos
#r:lectura
# a:append, adjuntar
# w:escritura
# x:create
# t:texto
#b:binary
# +

#f=open("/usr/passwrd","r")
#datos=f.read()
#f.close()
#print(datos)