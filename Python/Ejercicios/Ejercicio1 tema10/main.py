import tkinter 
from tkinter import ttk
window=tkinter.Tk()
window.columnconfigure(0,weight=1)
window.columnconfigure(1,weight=3)

def deseleccionar(event):
    window.destroy()

seleccionado=tkinter.StringVar()
r1=ttk.Radiobutton(window, text="hola",value="1",variable=seleccionado)
r2=ttk.Radiobutton(window, text="adios",value="2",variable=seleccionado)
r3=ttk.Radiobutton(window, text="hasta luego",value="3",variable=seleccionado)



boton=tkinter.Button(window,text="Borrar seleccion")
boton.bind("<Button-1>",deseleccionar)

r1.grid(column=0,row=1,pady=5,padx=5)
r2.grid(column=0,row=2,pady=5,padx=5)
r3.grid(column=0,row=3,pady=5,padx=5)

boton.grid(column=2,row=3,pady=5,padx=5)

window.mainloop()