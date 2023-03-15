import tkinter as tk
from tkinter import messagebox
from tkinter import *
from generador import *

ventana = tk.Tk()

ventana.title("Examen 2 parcial")

nombre=StringVar()
etiquetanombre=tk.Label(ventana,text="Nombre ")
etiquetanombre.pack()
entrynombre=tk.Entry(ventana, textvariable=nombre)
entrynombre.pack()

AP=StringVar()
etiquetaAP=tk.Label(ventana,text="Apellido Paterno ")
etiquetaAP.pack()
entryAP=tk.Entry(ventana, textvariable=AP)
entryAP.pack()

AM=StringVar()
etiquetaAM=tk.Label(ventana,text="Apellido Materno ")
etiquetaAM.pack()
entryAM=tk.Entry(ventana, textvariable=AM)
entryAM.pack()

AñoNac=IntVar()
etiquetaAñoNac=tk.Label(ventana,text="Año de Nacimiento \n INgresar Año en Formato: AAAA")
etiquetaAñoNac.pack()
entryAñoNac=tk.Entry(ventana, textvariable=AñoNac)
entryAñoNac.pack()

carrera=StringVar()
etiquetacarrera=tk.Label(ventana,text="Carrera ")
etiquetacarrera.pack()
entrycarrera=tk.Entry(ventana, textvariable=carrera)
entrycarrera.pack()
"""
generador=generador(nombre,AP,AM,AñoNac,carrera)
generar=tk.Button(ventana,text="Generar Matricula :D",comand=generador.generar)
generar.pack()"""
ventana.mainloop()