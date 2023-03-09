#etiquetas

from tkinter import *
from tkinter import ttk

raiz = Tk()
etqTexto = ttk.Label(raiz, text="Etiqueta solo texto")
etqTexto.grid()

imagen = PhotoImage(file="bob.png")

etqImagen = ttk.Label(raiz)
etqImagen.grid()
etqImagen['image'] = imagen

etqCombinada = ttk.Label(raiz, text='EtqCombinada', compound ='center')
etqCombinada.grid()
etqCombinada['image'] = imagen

raiz.mainloop()
