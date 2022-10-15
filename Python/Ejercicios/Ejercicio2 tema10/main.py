import tkinter 
from tkinter import Label, ttk
window=tkinter.Tk()
window.columnconfigure(0,weight=1)
window.columnconfigure(1,weight=3)

mi_label=Label(window,text="Selecciona la opcion que quieras")
mi_label.config(bg="white")
mi_label.config(font=('Arial', 44))

seleccionado=tkinter.StringVar()
checkbox1=ttk.Checkbutton(window,text="SELECION 1")
checkbox2=ttk.Checkbutton(window,text="SELECION 2")
checkbox3=ttk.Checkbutton(window,text="SELECION 3")
checkbox4=ttk.Checkbutton(window,text="SELECION 4")


checkbox1.grid(column=0,row=1,pady=5,padx=5)
checkbox2.grid(column=0,row=2,pady=5,padx=5)
checkbox3.grid(column=0,row=3,pady=5,padx=5)
checkbox4.grid(column=0,row=3,pady=5,padx=5)
mi_label.grid(column=0,row=0,pady=5,padx=5)

window.mainloop()