
paises=input("Introduce una lista de paises separados por coma""\n")
final=paises.split(",")
listaSinDup=set(final)

listaord=sorted(listaSinDup)
print(listaord)

