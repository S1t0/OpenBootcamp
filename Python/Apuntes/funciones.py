#Funcion sin parametros
def miFuncion():
    print("nombre")

miFuncion()  

#Funcion con parametros

def saludo(nombre):
    print("Hola,",nombre)
saludo("Andres")
#Hay funciones con funciones a su vez dentro de ellas

def matematicas(a,b):
    def suma(a,b):
        print(a+b)

    def resta(a,b):
        print(a-b)

    suma(a,b)
    resta(a,b)

matematicas(10,20)

  ## Parametros opcionales

def saludando(nombre="Andres"):
    print("Hola",nombre)

saludando()
saludando("Antonio")

def sumando(a=1,b=5,c=6):

    print(a+b+c)
sumando()
sumando(5)#a valdria ahora 5
sumando(c=12)# tambien podemos cambiar el parametro en el orden que queramos

#podemos hacer funciones que no sabemos aun el parametro que lleva, en la zona del parametro se pone * y la palabra args, args es por convencion

def suma(*args):
    resultado=0

    for arg in args:
        resultado+=arg
    print(resultado)
suma(1,5,4,8,9,6,5)

#tambien se puede hacer la funcion con **kwargs, es para nombres, los muestra en diccionarios

def nombres(**kwargs):

    print( kwargs ) 

nombres(vehiculo="coche",transporte="moto")  

#cuando una funcion nos da varios resultados podemos hacerlo de varias formas
#la primera nos da el restultado en forma de tupla
def operaciones(a,b):
    return a+b,a-b,a*b,a/b
print(operaciones(2,4))

#podemos hacer otra cosa que es asignar cada parte de una funcion a una variable
def operaciones(a,b):
    return a+b,a-b,a*b,a/b
    
suma, resta, multi,divi=operaciones(2,4)
print(suma)
print(resta)
print(multi)
print(divi)

#otro ejemplo con kwargs

def sumador(**kwargs):
    inicial= kwargs["inicial"] if "inicial" in kwargs else 0 
    final=kwargs["final"] if "final" in kwargs else 0 #este if in es el operador ternario en python, en JS es el ? :

    resultado=0
    for x in range(inicial,final+1):
        resultado +=x
    return resultado 

print("El sumador con los dos parametros",sumador(inicial=15,final=25))
print("El sumador con un parametro",sumador(inicial=15))
print("El sumador con el ultimo parametro",sumador(final=15))

# funciones anonimas, son las que se asignan a una variable

anonima=lambda:print("hola")
anonima()

anonimaconParametros= lambda nombre:print("Hola",nombre)
anonimaconParametros("pepe")

#las funciones lamda no tienen return, directamente le ponemos lo que queremos que retorne

sumatoria = lambda x,y: x+y
print(sumatoria(2,4))