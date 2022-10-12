from dis import code_info
import functools
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import csv

# --- functions ----

def edit():
    import listar_Archivos
    global tree1
    tree1=listar_Archivos.tree
    import cargar
    file=cargar.archivo
    with open(file, "w", newline='',encoding="utf8") as myfile:
        csvwriter = csv.writer(myfile, delimiter=',')
        listt=listar_Archivos.lista
        if cod.get().isdigit() and opcion.get() == "1" or opcion.get() == "0": 
            if semestre.get().isdigit(): 
                if estado.get()=="0" or estado.get()=="1"or estado.get()=="-1":
                    if creditos.get().isdigit() and nombre.get() != "":
                        busqueda[1]=str(nombre.get())
                        busqueda[2]=str(pre.get())
                        busqueda[3]=str(opcion.get())
                        busqueda[4]=str(semestre.get())
                        busqueda[5]=str(creditos.get())
                        busqueda[6]=str(estado.get())
                        tkinter.messagebox.showinfo("Informacion","Curso editado correctamente")
                    else:
                        tkinter.messagebox.showerror("Error","Datos Ingresados Erroneamente")
                else:
                    tkinter.messagebox.showerror("Error","Datos Ingresados Erroneamente")
            else:
                tkinter.messagebox.showerror("Error","Datos Ingresados Erroneamente")
        else:
            tkinter.messagebox.showerror("Error","Datos Ingresados Erroneamente")
        for row_id in range(len(listt)):
            row = listt[row_id]
            csvwriter.writerow(row)

def obtener():
    import listar_Archivos
    listt=listar_Archivos.lista
    colu=listar_Archivos.columna
    if codigox.get() in colu:
        res = len(colu) - 1 - colu[::-1].index(codigox.get())
        global busqueda
        busqueda = listt[res]
        cod.set(busqueda[0])
        nombre.set(busqueda[1])
        pre.set(busqueda[2])
        opcion.set(busqueda[3])
        semestre.set(busqueda[4])
        creditos.set(busqueda[5])
        estado.set(busqueda[6])
        tkinter.messagebox.showinfo("Informacion","Informacion precargada")
    else:
        tkinter.messagebox.showerror("Error","El código no existe")
    

# --- main ---


def ventana_editar(master, callback=None, args=(), kwargs={}):
    if callback is not None:
        callback = functools.partial(callback, *args, **kwargs)

    main_frame = Frame(master)

    Label(main_frame,text="ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ").grid(row=0,column=0, columnspan=2, pady=5)
    Label(main_frame,text="ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ").grid(row=11,column=0, columnspan=2, pady=5)
    Label(main_frame,text="Codigo del Curso a Editar").grid(row=1,column=0,columnspan=2,pady=5)
    Label(main_frame,text="Codigo:").grid(row=3,column=0,sticky=W, pady=5, padx=20)
    Label(main_frame,text="Nombre:").grid(row=4,column=0,sticky=W, pady=5, padx=20)
    Label(main_frame,text="Pre-requisito:").grid(row=5,column=0,sticky=W, pady=5, padx=20)
    Label(main_frame,text="Opcionalidad:").grid(row=6,column=0,sticky=W, pady=5, padx=20)
    Label(main_frame,text="Semestre:").grid(row=7,column=0,sticky=W, pady=5, padx=20)
    Label(main_frame,text="Creditos:").grid(row=8,column=0,sticky=W, pady=5, padx=20)
    Label(main_frame,text="Estado:").grid(row=9,column=0,sticky=W, pady=5, padx=20)
    global cod
    cod=StringVar()
    Entry(main_frame,textvariable=cod).grid(row=3,column=1,sticky=W+E, pady=5, padx=20)
    global nombre
    nombre =StringVar()
    Entry(main_frame,textvariable=nombre).grid(row=4,column=1,sticky=W+E, pady=5, padx=20)
    global pre
    pre =StringVar()
    Entry(main_frame,textvariable=pre).grid(row=5,column=1,sticky=W+E, pady=5, padx=20)
    global opcion
    opcion = StringVar()
    Entry(main_frame,textvariable=opcion).grid(row=6,column=1,sticky=W+E, pady=5, padx=20)
    global semestre
    semestre = StringVar() 
    Entry(main_frame,textvariable=semestre).grid(row=7,column=1,sticky=W+E, pady=5, padx=20)
    global creditos
    creditos = StringVar()
    Entry(main_frame,textvariable=creditos).grid(row=8,column=1,sticky=W+E, pady=5, padx=20)
    global estado
    estado = StringVar()
    Entry(main_frame,textvariable=estado).grid(row=9,column=1,sticky=W+E, pady=5, padx=20)
    global codigox
    codigox=StringVar()
    Entry(main_frame,textvariable=codigox).grid(row=2,column=0,sticky=W+E, pady=5, padx=20)
    #Boton       
    ttk.Button(main_frame, text="Regresar", command=callback).grid(row=10,column=1,sticky=W+E, pady=5,padx=20)
    ttk.Button(main_frame, text='Editar', command=edit).grid(row=10,column=0,sticky=W+E, pady=5,padx=20)
    ttk.Button(main_frame, text='Get Info', command=obtener).grid(row=2,column=1,sticky=W+E, pady=5,padx=20)
    return main_frame
