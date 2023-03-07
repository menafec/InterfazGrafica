#inicio de sesion
#ximena carolina fernandez cardenas


from tkinter import *
from tkinter import ttk

class Log: 

    def __init__(self, raiz):
        raiz.title("Inicio de Sesion")

        self.usuario = StringVar()
        self.contraseña = StringVar()

        mainFrame = ttk.Frame(raiz, padding="30 30 30 30") #padding(izquierda, arriba, derecha, abajo)
        mainFrame.grid(column=0, row=0)

        UsuarioEntry = ttk.Entry(mainFrame, width= 30, textvariable=self.usuario)
        ContraseñaEntry = ttk.Entry(mainFrame, width= 30, textvariable=self.contraseña)
        UsuarioEntry.grid(column=2, row=0, sticky=(W, E))
        ContraseñaEntry.grid(column=2, row= 1 )

        ttk.Label(mainFrame, text="Usuario").grid(column=1, row=0)
        ttk.Label(mainFrame, textvariable=self.usuario).grid(column=2, row=1)
        ttk.Label(mainFrame, text="Contraseña").grid(column=1, row=1)
        ttk.Label(mainFrame, textvariable=self.contraseña).grid(column=2, row=2)

        ttk.Button(mainFrame, text="Inicio").grid(column=2, row=2, sticky=(E))

    