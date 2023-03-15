import random
import string
from tkinter import messagebox

class generador():
    def __init__(self,entrynombre,entryAP,entryAM,entryAñoNac,entrycarrera,matricula):
        self.entrynombre=entrynombre
        self.entryAP=entryAP
        self.entryAP=entryAP
        self.entryAM=entryAM
        self.entryAñoNac=entryAñoNac
        self.entrycarrera=entrycarrera
        self.matricula=matricula
    def generar(self):
        
        nombre=self.entrynombre.get()
        AP=self.entryAP.get()
        AM=self.entryAM.get()
        AñoNac=self.entryAñoNac.get()
        carrera=self.entrycarrera.get()
        matricula=self.matricula.get()
        AñoCurso=23
        nombre=nombre.upper()
        AP=AP.upper()
        AM=AM.upper()
        AñoNac=AñoNac.upper()
        carrera=carrera.upper()
        
        digitos=string.digits
        
        Matricula=''.join(AñoCurso+AñoNac[:2]+nombre[1:]+AP[1:]+AM[1:]+random.choice(digitos)+carrera[2:])
        self.matricula.set(Matricula)
        
        messagebox.showinfo("Matricula generada con éxito","La matricula del alumno es:"+Matricula)