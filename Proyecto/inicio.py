from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import gestionar_cursos
import conteo_creditos
import cargar


def mostrar_gestionar():
    try:
        principal.grid_forget()
        gestionar_cursos.grid(row=0,column=0,columnspan=3,pady=0)
        from listar_Archivos import load_csv
        load_csv()
    except:
        tkinter.messagebox.showerror("Error","Cargue su archivo")
        return None

def mostrar_cargar():
    principal.grid_forget()
    cargar.grid(row=0,column=0,columnspan=3,pady=0)

def mostrar_conteo():
    try:
        principal.grid_forget()
        conteo_creditos.grid(row=0,column=0,columnspan=3,pady=0)
        from conteo_creditos import sumatorias
        sumatorias()
        from conteo_creditos import values
        values()
    except:
        tkinter.messagebox.showerror("Error","Cargue su archivo")
        return None

def mostrar_principal():
    gestionar_cursos.grid_forget()
    conteo_creditos.grid_forget()       
    cargar.grid_forget()
    principal.grid(row=0,column=0,columnspan=3,pady=0)

ventana=Tk()
ventana.geometry("+800+400")
aplicacion=Menu(ventana)
ventana.title("Practica 1")
principal=Frame(ventana)
principal.grid(row=0,column=0,columnspan=3,pady=0)
gestionar_cursos = gestionar_cursos.ventana_gestionar(ventana, mostrar_principal)
cargar=cargar.ventana_cargar(ventana, mostrar_principal)
conteo_creditos=conteo_creditos.ventana_conteo(ventana, mostrar_principal)
mostrar_principal()   
#Nombre
Label(principal,text="ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ").grid(row=0,column=0, columnspan=3, pady=5)
Label(principal,text="ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ").grid(row=8,column=0, columnspan=3, pady=5)
Label(principal,text="ㅤㅤNombre del curso: Lab. Lenguajes Formales y de Programación").grid(row=1,column=0,sticky=W, columnspan=3, pady=5)
Label(principal,text="ㅤㅤNombre del estudiante: Vinicio Manfredo López Pérez").grid(row=2,column=0, sticky=W, columnspan=3, pady=5)
Label(principal,text="ㅤㅤCarné del estudiante: 202002912").grid(row=3,column=0, sticky=W, columnspan=3, pady=5)


#Boton
ttk.Button(principal,text="Cargar Archivo", command=mostrar_cargar).grid(row=4,column=1,sticky=W+E, pady=5)
ttk.Button(principal,text="Gestionar Cursos", command=mostrar_gestionar).grid(row=5,column=1,sticky=W+E, pady=5)
ttk.Button(principal,text="Conteo de Créditos", command=mostrar_conteo).grid(row=6,column=1,sticky=W+E, pady=6)
ttk.Button(principal,text="Salir",command=ventana.destroy).grid(row=7,column=1,sticky=W+E, pady=5)

ventana.mainloop()






