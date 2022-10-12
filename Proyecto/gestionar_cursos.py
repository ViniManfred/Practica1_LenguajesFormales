import functools
from tkinter import *
from tkinter import ttk

def ventana_gestionar(master, callback=None, args=(), kwargs={}):
    if callback is not None:
        callback = functools.partial(callback, *args, **kwargs)
    
    def mostrar_listar():
        main_frame.grid_forget()
        listar_Archivos.pack()
        from listar_Archivos import load_csv
        load_csv()

    def mostrar_agregar():
        main_frame.grid_forget()
        agregar.grid(row=0,column=0,columnspan=3,pady=0)

    def mostrar_editar():
        main_frame.grid_forget()
        editar.grid(row=0,column=0,columnspan=3,pady=0)
    
    def mostrar_eliminar():
        main_frame.grid_forget()
        eliminar.grid(row=0,column=0,columnspan=3,pady=0)
    
    def mostrar_principal():
        listar_Archivos.pack_forget()
        editar.grid_forget()
        agregar.grid_forget()
        eliminar.grid_forget()
        main_frame.grid(row=0,column=0,columnspan=3,pady=0)

    main_frame = Frame(master)
    main_frame.grid(row=0,column=0,columnspan=3,pady=0)
    import listar_Archivos
    import agregar
    import editar
    import eliminar
    listar_Archivos = listar_Archivos.ventana_listar(master, mostrar_principal)
    agregar=agregar.ventana_agregar(master, mostrar_principal)
    editar=editar.ventana_editar(master, mostrar_principal)
    eliminar=eliminar.ventana_eliminar(master, mostrar_principal)
    mostrar_principal()   

    
    Label(main_frame,text="ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ").grid(row=0,column=0, columnspan=3, pady=5)
    Label(main_frame,text="ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ").grid(row=6,column=0, columnspan=3, pady=5)
    ttk.Button(main_frame, text="Listar Cursos",command=mostrar_listar).grid(row=1,column=1,sticky=W+E, pady=5)
    ttk.Button(main_frame,text="Agregar Curso", command=mostrar_agregar).grid(row=2,column=1,sticky=W+E, pady=5)
    ttk.Button(main_frame,text="Editar Curso", command=mostrar_editar).grid(row=3,column=1,sticky=W+E, pady=5)
    ttk.Button(main_frame,text="Eliminar Curso",command=mostrar_eliminar).grid(row=4,column=1,sticky=W+E, pady=5)
    ttk.Button(main_frame, text="Regresar", command=callback).grid(row=5,column=1,sticky=W+E, pady=5)
    return main_frame


       



