#muestra widget

from tkinter import *
from tkinter import ttk


class Muestra: 

    def __init__(self, raiz):
        raiz.title("Muestra Widgets")

        self.nombre = StringVar()
        self.aPaterno =StringVar()
        self.aMaterno = StringVar()
        self.correo = StringVar()
        self.movil = StringVar()

        mainFrame = ttk.Frame(raiz, padding="30 30 30 30") #padding(izquierda, arriba, derecha, abajo)
        mainFrame.grid(column=0, row=0)
        

        secondFrame = ttk.Frame(raiz, padding= "30 30 30 30")
        secondFrame.grid(column=0, row=1)
        
        thirdFrame = ttk.Frame(raiz, padding= "30 30 30 30")
        thirdFrame.grid(column=1, row=0)


        ttk.Label(mainFrame, text="Nombre").grid(column=0, row=0)
        ttk.Label(mainFrame, textvariable=self.nombre).grid(column=1, row=0)
        ttk.Label(mainFrame, text="A. Paterno").grid(column=0, row=2)
        ttk.Label(mainFrame, textvariable=self.aPaterno).grid(column=1, row=2)
        ttk.Label(mainFrame, text="A. Materno").grid(column=0, row=4)
        ttk.Label(mainFrame, textvariable=self.aMaterno).grid(column=1, row=4)
        ttk.Label(mainFrame, text="Correo").grid(column=0, row=6)
        ttk.Label(mainFrame, textvariable=self.correo).grid(column=1, row=6)
        ttk.Label(mainFrame, text="Movil").grid(column=0, row=8)
        ttk.Label(mainFrame, textvariable=self.movil).grid(column=1, row=8)

        nombreEntry = ttk.Entry(mainFrame, width = 12, textvariable = self.nombre)
        nombreEntry.grid(column=1, row=0)

        aPaternoEntry = ttk.Entry(mainFrame, width = 12, textvariable = self.aPaterno)
        aPaternoEntry.grid(column=1, row=2)

        aMaternoEntry = ttk.Entry(mainFrame, width = 12, textvariable = self.aMaterno)
        aMaternoEntry.grid(column=1, row=4)

        correoEntry = ttk.Entry(mainFrame, width = 12, textvariable = self.correo)
        correoEntry.grid(column=1, row=6)

        movilEntry = ttk.Entry(mainFrame, width = 12, textvariable = self.movil)
        movilEntry.grid(column=1, row=8)

        
        ttk.Label(secondFrame, text="Aficiones:").grid(column=1, row=7)
        Leer = ttk.Radiobutton(secondFrame, text= "Leer")
        Leer.grid(column=1, row=8)
        
        Musica = ttk.Radiobutton(secondFrame, text="Musica")
        Musica.grid(column=2, row=8)
        
        Videojuegos = ttk.Radiobutton(secondFrame, text="Videojuegos") 
        Videojuegos.grid(column=3, row=8)

        Estudiante = ttk.Radiobutton(thirdFrame, text= "Estudiante")
        Estudiante.grid(column=3, row=4)
        
        Empleado = ttk.Radiobutton(thirdFrame, text="Empleado")
        Empleado.grid(column=3, row=6)
        
        Desempleado = ttk.Radiobutton(thirdFrame, text="Desesempleado") 
        Desempleado.grid(column=3, row=8)

        estado = StringVar()
        comboEstados = ttk.Combobox(secondFrame, textvariable=estado)
        comboEstados.grid(column=4, row=8)
        comboEstados['values'] = ("Jalisco", "Nayarit", "Colima", "Michoacan")

        guardar = ttk.Button(secondFrame, text= "Guardar")
        guardar.grid(column= 0, row=16)

        cancelar = ttk.Button(secondFrame, text="Cancelar")
        cancelar.grid(column= 1, row=16)

