 #Para crear las bases de datos con sqlite hay que poner en el comando sqlite nombredelabase.db, 
 # si no lo hacemos asi no se queda guardada => sqlite3 miaplicacion.db

 #poniendo .help nos salen todos los comandos de sqlite3
 #Parar crear una tabla ponemos CREATE TABLE (en mayusculas)y el nombre de la tabla--> CREATE TABLE mibasededatos(),
 #dentro de los parentesis vamos poniendo los campos que queremos que tenga nuestra base de datos, como por ejemplo el id, un username,
 #un password, etc. EJEMPLO

#  CREATE TABLE users(
#     id INTEGER PRIMARY KEY,
#     username TEXT NOT NULL,
#     password TEXT NOT NULL);

#para introducir dentro de la tabla users se hace asi: INSERT INTO users(id, username, password)VALUES(1,"Andres,", "miclave")

import sqlite3

conn=sqlite3.connect("miaplicacion.db")
cursor= conn.cursor()
rows= cursor.execute("SELECT * FROM users WHERE id=1")#esto es una query

for row in rows:
    print(row)



cursor.close()
conn.close
