import functools
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import csv

# --- functions ----

def save_csv():
    
    import listar_Archivos
    global tree1
    tree1=listar_Archivos.tree
    import cargar
    file=cargar.archivo
    with open(file, "w", newline='',encoding="utf8") as myfile:
        csvwriter = csv.writer(myfile, delimiter=',')
        colu=listar_Archivos.columna
        listt=listar_Archivos.lista
        if cod1.get() in colu:
            tkinter.messagebox.showerror("Error","Ya existe el curso")
            for row_id in range(len(((tree1.get_children())))):
                row = listt[row_id]
                csvwriter.writerow(row)
        else:
            if cod1.get().isdigit() and opcion.get() == "1" or opcion.get() == "0": 
                if semestre.get().isdigit(): 
                    if estado.get()=="0" or estado.get()=="1"or estado.get()=="-1":
                        if creditos.get().isdigit() and nombre.get() != "":
                            tree1.insert("", 'end', values=[str(cod1.get()),str(nombre.get()), str(pre.get()),
                            str(opcion.get()),str(semestre.get()),str(creditos.get()),str(estado.get())])
                            listt.append([str(cod1.get()),str(nombre.get()), str(pre.get()),
                            str(opcion.get()),str(semestre.get()),str(creditos.get()),str(estado.get())])
                            colu.append(cod1.get())
                            tkinter.messagebox.showinfo("Informacion","Curso agregado correctamente")
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
            

# --- main ---


def ventana_agregar(master, callback=None, args=(), kwargs={}):
    if callback is not None:
        callback = functools.partial(callback, *args, **kwargs)

    main_frame = Frame(master)

    Label(main_frame,text="ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ").grid(row=0,column=0, columnspan=2, pady=5)
    Label(main_frame,text="ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ").grid(row=9,column=0, columnspan=2, pady=5)
    Label(main_frame,text="ㅤCodigo:").grid(row=1,column=0,sticky=W, pady=5)
    Label(main_frame,text="ㅤNombre:").grid(row=2,column=0,sticky=W, pady=5)
    Label(main_frame,text="ㅤPre-requisito:").grid(row=3,column=0,sticky=W, pady=5)
    Label(main_frame,text="ㅤOpcionalidad:").grid(row=4,column=0,sticky=W, pady=5)
    Label(main_frame,text="ㅤSemestre:").grid(row=5,column=0,sticky=W, pady=5)
    Label(main_frame,text="ㅤCreditos:").grid(row=6,column=0,sticky=W, pady=5)
    Label(main_frame,text="ㅤEstado:").grid(row=7,column=0,sticky=W, pady=5)
    global cod1
    cod1=StringVar()
    Entry(main_frame,textvariable=cod1).grid(row=1,column=1,sticky=W+E, pady=5, padx=20)
    global nombre
    nombre =StringVar() 
    Entry(main_frame,textvariable=nombre).grid(row=2,column=1,sticky=W+E, pady=5, padx=20)
    global pre
    pre =StringVar() 
    Entry(main_frame,textvariable=pre).grid(row=3,column=1,sticky=W+E, pady=5, padx=20)
    global opcion
    opcion = StringVar()
    Entry(main_frame,textvariable=opcion).grid(row=4,column=1,sticky=W+E, pady=5, padx=20)
    global semestre
    semestre = StringVar() 
    Entry(main_frame,textvariable=semestre).grid(row=5,column=1,sticky=W+E, pady=5, padx=20)
    global creditos
    creditos = StringVar()
    Entry(main_frame,textvariable=creditos).grid(row=6,column=1,sticky=W+E, pady=5, padx=20)
    global estado
    estado = StringVar()
    Entry(main_frame,textvariable=estado).grid(row=7,column=1,sticky=W+E, pady=5, padx=20)
    #Boton       
    ttk.Button(main_frame, text="Regresar", command=callback).grid(row=8,column=1,sticky=W+E, pady=5,padx=20)
    ttk.Button(main_frame, text='Agregar', command=save_csv).grid(row=8,column=0,sticky=W+E, pady=5,padx=20)
    return main_frame


           

    