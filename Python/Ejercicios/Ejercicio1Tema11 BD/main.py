import sqlite3
def main():
    crear_usuario(6,"Pepito","Sanchez")
    buscar_usuario("Andres")

def crear_usuario(identificador,nombre,apellido):
    conn=sqlite3.connect("basededatos.db")
    cursor= conn.cursor()
    query= "INSERT INTO alumnos(id,nombre,apellido) VALUES(identificador,nombre,apellido)";#no me crea los nuevos alumnos desde el codigo, los meto a mano en terminal
    rows=cursor.execute(query)
    print(type(rows))
    conn.commit()

    cursor.close()
    conn.close
    
def buscar_usuario(nombre):
    conn=sqlite3.connect("basededatos.db")
    cursor= conn.cursor()
    rows=cursor.execute("SELECT * FROM users WHERE nombre=nombre")

    cursor.close()
    conn.close