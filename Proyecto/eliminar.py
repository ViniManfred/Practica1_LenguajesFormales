import functools
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import csv

# --- functions ----


# --- main ---
def eliminar():
    import listar_Archivos
    global tree1
    tree1=listar_Archivos.tree
    listt=listar_Archivos.lista
    colu=listar_Archivos.columna
    import cargar
    file=cargar.archivo
    with open(file, "w", newline='',encoding="utf8") as myfile:
        csvwriter = csv.writer(myfile, delimiter=',')
        if cod1.get() in colu:
            rola=[indice for indice, dato in enumerate(colu) if dato == cod1.get()]
            contador=0
            for x in rola:               
                busqueda = listt[x-contador]
                listt.remove(busqueda) 
                contador=contador+1
            for row_id in range(len(listt)):
                row = listt[row_id]
                csvwriter.writerow(row)
            tkinter.messagebox.showinfo("Informacion","Curso eliminado correctamente")
        else:
            for row_id in range(len(tree1.get_children())):
                row = listt[row_id] 
                csvwriter.writerow(row)
            tkinter.messagebox.showerror("Error","No existe el curso")  

def ventana_eliminar(master, callback=None, args=(), kwargs={}):
    if callback is not None:
        callback = functools.partial(callback, *args, **kwargs)

    main_frame = Frame(master)

    Label(main_frame,text="ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ").grid(row=0,column=0, columnspan=2, pady=5)
    Label(main_frame,text="ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ").grid(row=3,column=0, columnspan=2, pady=5)
    Label(main_frame,text="ㅤCodigo del Curso:").grid(row=1,column=0,sticky=W, pady=5,padx=20)
    global cod1
    cod1=StringVar()
    Entry(main_frame,textvariable=cod1).grid(row=1,column=1,sticky=W+E, pady=5, padx=20)
    #Boton       
    ttk.Button(main_frame, text="Regresar", command=callback).grid(row=2,column=1,sticky=W+E, pady=5,padx=20)
    ttk.Button(main_frame, text='Eliminar', command=eliminar).grid(row=2,column=0,sticky=W+E, pady=5,padx=20)
    return main_frame
