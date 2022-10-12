import functools
from tkinter import *
from tkinter import ttk
import csv

def ventana_listar(master, callback=None, args=(), kwargs={}):
    if callback is not None:
        callback = functools.partial(callback, *args, **kwargs)

    main_frame = Frame(master)
    global tree           
    tree = ttk.Treeview(main_frame, height=15, selectmode='extended')
    tree.pack()
    tree["columns"] = ("1", "2", "3", "4","5","6","7")
    tree.column("1",   width=75)
    tree.column("2",   width=160)
    tree.column("3", width=100)
    tree.column("4",  width=100)
    tree.column("5",  width=75)
    tree.column("6",  width=75)
    tree.column("7",  width=75)
    tree.heading("1",   text="Código")
    tree.heading("2",   text="Nombre")
    tree.heading("3", text="Pre-requisitos")
    tree.heading("4",  text="Opcionalidad")
    tree.heading("5",  text="Semestre")
    tree.heading("6",  text="Créditos")
    tree.heading("7",  text="Estado")
    tree["show"] = "headings"
    ttk.Button(main_frame, text="Regresar", command=callback).pack()
    return main_frame

def Limpiar():
	tree.delete(*tree.get_children())

def load_csv():
    Limpiar()
    import cargar
    file=cargar.archivo
    with open(file,encoding="utf8") as myfile:     
        csvread = csv.reader(myfile, delimiter=',')
        i = 0
        global columna
        columna = []
        resultado=[]
        global lista
        lista=[]
        global sumas
        sumas=[]
        for fila in csvread:
            columna.append(fila[i])
            lista.append(fila)
        for element in columna:
            res = len(columna) - 1 - columna[::-1].index(element) 
            if res not in resultado:
                resultado.append(res)
                sumas.append(lista[res])
        for r in range(len(resultado)):
            tree.insert("", 'end', values=lista[resultado[r]])
    with open(file, "w", newline='',encoding="utf8") as myfile:
        csvwriter = csv.writer(myfile, delimiter=',')
        for row_id in range(len((lista))):
            row = lista[row_id]
            csvwriter.writerow(row)
    