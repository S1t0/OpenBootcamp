import tkinter #con la version de python 3.10.6 no me funciona, con la 3.9.13 si 
from tkinter import ttk
window=tkinter.Tk()

# label_saludo=tkinter.Label(window,text="Hola",bg="yellow",fg="blue") #geometria pack  
# label_saludo.pack(ipadx=50, ipady=50,fill="y", expand=True ) 

# label_adios=tkinter.Label(window,text="Adios",bg="red",fg="white")
# label_adios.pack()


#geometria mediante grid  
#grid se entiende como una matriz con filas y columnas y se interpreta de la siguiente forma
#(0,0) (1,0) (2,0)
#(0,1) (1,1) (2,1)
#(0,2) (1,2) (2,2)

# window.columnconfigure(1,weight=1)
# window.columnconfigure(1,weight=3)

# username_label=ttk.Label(window, text="username")
# username_label.grid(column=0,row=0,sticky=tkinter.W,padx=5, pady=5)#STICKY=ES PARA FIJAR LA LABEL EN UN LUGAR, W=WEST, S=SOUTH,N=NORTH, SE BASA EN POLOS

# #COLUMN=posicion en la columna, ROW=posicion en la fila 0, padx=tamaño en x, pady=tamaño en y
# username_entry=ttk.Entry(window)
# username_entry.grid(column=1,row=0,sticky=tkinter.E,padx=5,pady=5)

# password_label=ttk.Label(window, text="password")
# password_label.grid(column=0,row=1,sticky=tkinter.W,padx=5, pady=5)

# password_entry=ttk.Entry(window,show="*")
# password_entry.grid(column=1,row=1,sticky=tkinter.E,padx=5,pady=5)

# login_button=ttk.Button(window,text="Iniciar sesion")
# login_button.grid(column=1,row=3, sticky=tkinter.E, padx=5, pady=5)

#POSICIONAMIENTO MEDIANTE PLACE=posiciona de forma absoluta o relativa

label1=tkinter.Label(window, text="Posicionamiento absoluto",bg="blue",fg="white")
label1.place(x=10, y=50)

label2=tkinter.Label(window, text="otro mas",bg="red",fg="yellow")
label2.place(relx=0.10, rely=0.15,relwidth=0.5,anchor="ne")




window.mainloop() #nos genera la ventana
