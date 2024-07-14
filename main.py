import tkinter
from tkinter import *
from tkinter import ttk

import sv_ttk

entry_a = 0
entry_b = 0
conjunto_a = 0
conjunto_b = 0
ListaSeleccion = 0
def Enviaruno(ListaTuplas):
    seleccionTuplas = ListaTuplas.curselection()
    print("Haz seleccionado:", seleccionTuplas)

def relacionesLista(entry_a, entry_b, ListaTuplas):
    valor_a = entry_a.get()
    valor_b = entry_b.get()
    conjunto_a = valor_a.split(",")
    conjunto_b = valor_b.split(",")
    print("el valor de a es", valor_a)
    print("el valor de b es", valor_b)

    print("el conjunto a es:", conjunto_a)
    print("el conjunto b es:", conjunto_b)
    ListaTuplas.delete(0, tkinter.END)

    #Rellenado de la listbox
    ListaTuplasLista = []
    for elemento_a in conjunto_a:
        for elemento_b in conjunto_b:
            ListaTuplasLista.append((elemento_a, elemento_b))
            ListaTuplas.insert("end", f"({elemento_a}, {elemento_b})")
    print(f"Las tuplas del conjunto A y B son:", ListaTuplasLista)


def click_boton():
    for widget in frame2.winfo_children():
        widget.destroy()
    print("widgets eliminados \u2713")


def relaciones():
    #se remueve el texto de bienvenida
    for widget in frame2.winfo_children():
        widget.destroy()
    print("widgets anteriores eliminados")

    #caja de texto del conjunto a
    conjuntotitulo_a = ttk.LabelFrame(frame2, text="Conjunto A", style="Card.TFrame")
    conjuntotitulo_a.grid(padx=(10, 10), row=0, column=1)
    entry_a = ttk.Entry(conjuntotitulo_a)
    entry_a.grid(row=0, column=1, padx=10, pady=10)

    #caja de texto del conjunto b
    conjuntotitulo_b = ttk.LabelFrame(frame2, text="Conjunto B", style="Card.TFrame")
    conjuntotitulo_b.grid(padx=(10, 10), row=0, column=3)
    entry_b = ttk.Entry(conjuntotitulo_b)
    entry_b.grid(row=0, column=3, padx=10, pady=10)

    #recordatorio de que se debe separar con coma
    aviso_coma = tkinter.Label(frame2, text="*Separar con coma ( , )", fg="grey")
    aviso_coma.grid(row=0, column=2, padx=0, pady=(15, 0))

    #boton para subir la relacion
    boton_subir = ttk.Button(frame2, text="Enviar", style="Accent.TButton", command=lambda: relacionesLista(entry_a, entry_b, ListaTuplas))
    boton_subir.grid(row=0, column=4, padx=(10, 0), pady=(15, 0))

    #Textbox seleccion
    ListaTuplas = Listbox(frame2, selectmode="multiple")
    ListaTuplas.place(relx=0.25, rely=0.5, relwidth=0.45, relheight=0.65, anchor="center")

    #Listbox relaciones
    ListaSeleccion = Listbox(frame2, width=40, height=18)
    ListaSeleccion.place(relx=0.75, rely=0.5, relwidth=0.45, relheight=0.65, anchor="center")

    #boton para enviar a la relacion
    Boton_enviar_uno = ttk.Button(frame2, text=">", style="Accent.TButton", command=lambda: Enviaruno(ListaTuplas))
    Boton_enviar_uno.grid(row=1, column=1, padx=10, pady=10, sticky='ews')
    frame2.rowconfigure(1, weight=3)



#ventana principal
root = Tk()
root.title("Hecho por: Jonathan Salazar")
root.minsize(820, 520)
root.maxsize(1280, 520)

root.rowconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

#frame izquierdo que contiene los botones
frame1 = ttk.LabelFrame(root, text="Opciones", width=300, height=400, style="Card.TFrame")
frame1.grid(row=0, column=0, padx=20, pady=15, sticky="nsew")
#frame1.columnconfigure(0, weight=1)

#boton de crear relacion y propiedades, separados del resto
button = ttk.Button(frame1, text="Crear Relacion", style="Accent.TButton", command=relaciones)
button.grid(row=1, column=0, padx=10, pady=(35, 10), sticky="ew")
button = ttk.Button(frame1, text="Propiedades", style="Button.TButton", command=click_boton)
button.grid(row=2, column=0, padx=10, pady=(10, 120), sticky="ew")

#label de texto para los otros botones
rep_lab = ttk.Label(frame1, text="Representaciones", anchor="center")
rep_lab.grid(row=3, column=0, padx=10, pady=10)

#el resto de los botones
button = ttk.Button(frame1, text="Matriz", style="Button.TButton", command=click_boton)
button.grid(row=4, column=0, padx=10, pady=10, sticky="ew")
button = ttk.Button(frame1, text="Sagital", style="Button.TButton", command=click_boton)
button.grid(row=5, column=0, padx=10, pady=10, sticky="ew")
button = ttk.Button(frame1, text="Grafo", style="Button.TButton", command=click_boton)
button.grid(row=6, column=0, padx=10, pady=10, sticky="ew")

#segundo frame
frame2 = ttk.LabelFrame(root, text="Ventana Principal", padding=10)

#frame2.rowconfigure(0, weight=1)
#frame2.rowconfigure(1, weight=5)

frame2.grid(row=0, column=1, padx=20, pady=15, sticky="nsew")
label2 = ttk.Label(frame2, text="Bienvenido Usuario, seleccione una opcion para comenzar")
label2.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
#tema
sv_ttk.set_theme("dark")

#Fin
root.mainloop()
