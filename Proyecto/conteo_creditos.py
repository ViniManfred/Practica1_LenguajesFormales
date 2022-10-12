import functools
from msilib.schema import ComboBox
from operator import index
from tkinter import *
from tkinter import ttk
import tkinter.messagebox


def sumatorias():
    import listar_Archivos
    from listar_Archivos import load_csv
    load_csv()
    global lista1
    lista1=listar_Archivos.sumas 
    global estado
    estado=[]
    global credit
    credit=[]
    global obligatorio
    obligatorio=[]
    creditos_a=[]
    creditos_c=[]
    creditos_p=[]
    i = 6
    j = 5
    k = 3
    for fila in lista1:
        estado.append(fila[i])
        credit.append(fila[j])
        obligatorio.append(fila[k])
    if "0" in estado:
        aprobados=[indice for indice, dato in enumerate(estado) if dato == "0"]
        for x in aprobados:
            creditos_a.append(credit[x])
    if "1" in estado:
        cursando=[indice for indice, dato in enumerate(estado) if dato == "1"]
        for y in cursando:
            creditos_c.append(credit[y])
    
    for row in range(len(lista1)):
        if estado[row] =="-1" and obligatorio[row] =="1":
            creditos_p.append(credit[row])
    parser1=[int(x) for x in creditos_a]
    parser2=[int(x) for x in creditos_c]
    parser3=[int(x) for x in creditos_p]
    respuesta1=sum(parser1)
    respuesta2=sum(parser2)
    respuesta3=sum(parser3)
    label_1.configure(text=(f"Creditos aprobados: {respuesta1}"))
    label_2.configure(text=(f"Creditos cursando: {respuesta2}"))
    label_3.configure(text=(f"Creditos pendientes: {respuesta3}"))
    

def semestres():
    i=4
    semestre_list=[]
    semes=[]
    lista_1=[]
    lista_2=[]
    lista_3=[]
    lista_4=[]
    lista_5=[]
    lista_6=[]
    for fila in lista1:
        semestre_list.append(fila[i])
    parser1=[int(x) for x in semestre_list]
    for row in parser1:
        if row>0 and row<=int(entry1.get()):
            lista_5.append(row)
            semes=[indice for indice, dato in enumerate(parser1) if dato == row]
            lista_1.append(semes)
    for element in lista_1:
        if element not in lista_2:
            lista_2.append(element)
    for i in range (len(lista_2)):
        lista_3.extend(lista_2[i])
    for y in lista_3:
        lista_4.append(obligatorio[y])
    for z in range(len(lista_4)):
        if lista_4[z]=="0":
            lista_3.remove(z)
    for a in lista_3:
            lista_6.append(credit[a])
    parser=[int(x) for x in lista_6]
    respuesta=sum(parser)
    label_4.configure(text=(f"Creditos obligatorios hasta semestre N: {respuesta}"))

def values():
    i=4
    global combo
    combo=[]
    semestre_list=[]
    for fila in lista1:
        semestre_list.append(fila[i])
    for element in semestre_list:
        if element not in combo:
            combo.append(element)
    parser=[int(x) for x in combo]
    parser.sort()
    text1.configure(values=(parser))
    text2.configure(values=(parser))

def semestre():
    estado1=[]
    credit1=[]
    obligatorio1=[]
    i=4
    semestre_list=[]
    lista_1=[]
    for fila in lista1:
        semestre_list.append(fila[i])
    for row in semestre_list:
        if row==combo1.get():
            numero=[indice for indice, dato in enumerate(semestre_list) if dato == row]
    for a in range(len(numero)):
        lista_1.append(lista1[numero[a]])
    creditos_a=[]
    creditos_c=[]
    creditos_p=[]
    i = 6
    j = 5
    k = 3
    for fila in lista_1:
        estado1.append(fila[i])
        credit1.append(fila[j])
        obligatorio1.append(fila[k])
    if "0" in estado1:
        aprobados=[indice for indice, dato in enumerate(estado1) if dato == "0"]
        for x in aprobados:
            creditos_a.append(credit1[x])
    if "1" in estado1:
        cursando=[indice for indice, dato in enumerate(estado1) if dato == "1"]
        for y in cursando:
            creditos_c.append(credit1[y])
    
    for row in range(len(lista_1)):
        if estado1[row] =="-1" and obligatorio1[row] =="1":
            creditos_p.append(credit1[row])
    parser1=[int(x) for x in creditos_a]
    parser2=[int(x) for x in creditos_c]
    parser3=[int(x) for x in creditos_p]
    respuesta1=sum(parser1)
    respuesta2=sum(parser2)
    respuesta3=sum(parser3)
    label_5.configure(text=(f"Creditos aprobados: {respuesta1}"))
    label_6.configure(text=(f"Creditos cursando: {respuesta2}"))
    label_7.configure(text=(f"Creditos pendientes: {respuesta3}"))


    
def ventana_conteo(master, callback=None, args=(), kwargs={}):
    if callback is not None:
        callback = functools.partial(callback, *args, **kwargs)

    main_frame = Frame(master)
    main_frame.grid(row=0,column=0,columnspan=3,pady=0)
    
    Label(main_frame,text="").grid(row=0,column=0,columnspan=3, pady=5)
    global label_1
    label_1=Label(main_frame,text="Creditos aprobados: ")
    label_1.grid(row=1,column=0,sticky=W, pady=5, padx=25)
    global label_2
    label_2=Label(main_frame,text="Creditos cursando: ")
    label_2.grid(row=1,column=1,sticky=W, pady=5, padx=25)
    global label_3
    label_3=Label(main_frame,text="Creditos pendientes: ")
    label_3.grid(row=1,column=2,sticky=W, pady=5, padx=25)
    global label_4
    label_4=Label(main_frame,text="Creditos obligatorios hasta semestre N: ")
    label_4.grid(row=2,column=0,columnspan=2, sticky=W, pady=5, padx=25)
    Label(main_frame,text="Semestre N: ").grid(row=3,column=0,sticky=W, pady=5, padx=25)
    Label(main_frame,text="Creditos del semestre: ").grid(row=4,column=0,sticky=W, pady=5, padx=25)
    Label(main_frame,text="Semestre: ").grid(row=6,column=0,sticky=W, pady=5, padx=25)
    Label(main_frame,text="").grid(row=8,column=0,columnspan=3, pady=5)
    global label_5
    label_5=Label(main_frame)
    label_5.grid(row=5,column=0,sticky=W, pady=5, padx=25)
    global label_6
    label_6=Label(main_frame)
    label_6.grid(row=5,column=1,sticky=W, pady=5, padx=25)
    global label_7
    label_7=Label(main_frame)
    label_7.grid(row=5,column=2,sticky=W, pady=5, padx=25)

    global entry1
    entry1 = StringVar()
    global text2
    text2=ttk.Combobox(main_frame,textvariable=entry1)
    text2.grid(row=3,column=1,sticky=W+E, pady=5,padx=25)

    global combo1
    combo1 = StringVar()
    global text1
    text1=ttk.Combobox(main_frame,textvariable=combo1)
    text1.grid(row=6,column=1,sticky=W+E, pady=5, padx=25)

    ttk.Button(main_frame,text="Contar", command=semestres).grid(row=3,column=2,sticky=W+E, pady=5, padx=25)
    ttk.Button(main_frame,text="Contar", command=semestre).grid(row=6,column=2,sticky=W+E, pady=5, padx=25)
    ttk.Button(main_frame, text="Regresar", command=callback).grid(row=7,column=2,sticky=W+E, pady=5, padx=25)
    return main_frame