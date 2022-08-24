#map, filter,reduce,zip

numeros=[1,2,3,4,5,6,7,8,9]

#filter(funcion,lista)=> filter funciona pasandole como primer parametro la funcion que queremos que haga, y como segundo la lista

#numero pares de la lista

def miFuncion(x):
    if x%2==0:
        return True

    return False

resultado=filter(miFuncion,numeros)#filter trabaja con True o False, por eso la funcion debe de dar un booleano
print(list(resultado))

lista=["pepe","pepito","antonio","juan","pepillo"]

def miFuncion2(x):#aqui filtramos los nombres que empiezan por pep
    if str(x).startswith("pep"):
        return True

    return False

final=filter(miFuncion2,lista)
print(list(final))

#map, aplica una funcion a todos los elementos de una lista, la estructura es igual que filter

def cuadrado(x):
    return x *x 

resultadoCuadrado=map(cuadrado,[1,2,3,4])
print(list(resultadoCuadrado))

#zip()=> agrega iterables en una tupla


cursos=["java","python","git"]
asistentes=[15,20,4]

demo=zip(cursos, asistentes)
print(list(demo))

#palabras all() y any()=> para verificar que todas(all) o algunas (any) de las condiciones de una lista se cumplan

listaA=[1==1,2==2,3==3,4==5]

res=any(listaA)#si se cumple alguna, da True
print(res)

res2=all(listaA)#tienen que cumplirse todas, si alguna no se cumple da False

print(res2)

#round =>para redondear
#min()=> nos da el minimo de una lista
#pou()=>para elevar
#sorted()=>para ordenar una lista
listaOrd=["w","r","t","a"]
ordenada=sorted(listaOrd)
print(ordenada)
#input=>para que el usuario nos introduzca datos

a=input("como te llamas")
print("hola",a)