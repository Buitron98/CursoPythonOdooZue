from tkinter import *

#Crear ventana
ventana = Tk()
#Propiedades ventana
ventana.geometry("750x450")
ventana.title("Curso Python TKINTER")
ventana.resizable(1,1)
#Agregar Texto
texto = Label(ventana,text="Hola Mundo!!")
texto.config(
    fg = "white",
    bg = "black",
    font=("Arial",30),
    padx=20,
    pady=20,
)
texto.grid(row=0,column=0)
texto = Label(ventana,text="CURSO PYTHON")
texto.config(
    fg = "white",
    bg = "red",
    font=("Arial",30),
    padx=20,
    pady=20,
)
texto.grid(row=0,column=1)
#Caja de texto
texto = Label(ventana,text="Nombre")
texto.grid(row=1,column=0)
caja_texto = Entry(ventana)
caja_texto.config(
    width=30,
)
caja_texto.grid(row=1,column=1)
#TextArea
texto = Label(ventana,text="Descripción")
texto.grid(row=2,column=0)
caja_textarea = Text(ventana)
caja_textarea.config(
    width=30,
    height=10,
)
caja_textarea.grid(row=2,column=1)
#Botones
boton = Button(ventana, text="Guardar")
boton.grid(row=3,column=1)

#Ejecutar ventana
ventana.mainloop()