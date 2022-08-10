variable=5
print(variable)

globals()["variable"]=6
print(variable)

#para modificar una variable o cualquier cosa desde cualquier parte del codigo, con globals() podemos hacerlo