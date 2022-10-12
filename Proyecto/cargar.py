import functools
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from tkinter import filedialog
def abrirArchivo():
    global archivo
    archivo = filedialog.askopenfilename(title = "Seleccionar Archivo", filetypes = (("CSV Files","*.csv"),("all files","*.*")))
    #indica.configure(text="Archivo cargado correctamente")
    
    try:
        miArchivo = open(archivo, "r")   
        lectura = miArchivo.readlines()
        tkinter.messagebox.showinfo("Informacion","Archivo cargado correctamente")
        
    except ValueError:
        tkinter.messagebox.showerror("Error","Formato incorrecto")
        return None
    except FileNotFoundError:
        tkinter.messagebox.showerror("Error","Archivo dañado \n o no seleccionado")
        return None
        

def ventana_cargar(master, callback=None, args=(), kwargs={}):
    if callback is not None:
        callback = functools.partial(callback, *args, **kwargs)
    
    main_frame = Frame(master)

    Label(main_frame,text="ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ").grid(row=0,column=0, columnspan=3, pady=5)
    Label(main_frame,text="ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ").grid(row=4,column=0, columnspan=3, pady=5)
    """global indica
    indica = Label(main_frame,text = "Cargue su archivo")
    indica.grid(column = 1, row = 2)"""
    ttk.Button(main_frame, text="Seleccionar", command= abrirArchivo).grid(row=1,column=1,sticky=W+E, pady=5)
    ttk.Button(main_frame, text="Regresar", command=callback).grid(row=3,column=1,sticky=W+E, pady=5)
    
    return main_frame

