"""
este es un programa para agregar una lista de dato y tambien se podra eliminar elementos
"""

from tkinter import *
from tkinter import ttk

window = Tk()
window.title("agrgar datos")

# variables
date_list = []

# funciones


def agregar():
    value = date.get()
    date_list.append(value)
    update_view_date()


def eliminar():
    selected_item = listbox.curselection()
    if selected_item:
        index = selected_item[0]
        if 0 <= index < len(date_list):
            date_list.pop(index)
            update_view_date()


def update_view_date():
    view_date.set("\n".join(date_list))


def do_nothing():
    pass


# entrada de datos
date = StringVar()
entry_date = ttk.Entry(window, width=10, textvariable=date)
entry_date.grid(column=0, row=0, sticky="NSEW")

# botones de agregar y eliminar
ttk.Button(window, text="agregar", command=agregar).grid(
    column=1, row=0, sticky="NSEW")
ttk.Button(window, text="eliminar", command=eliminar).grid(
    column=1, row=2, sticky="NSEW")

# view date
view_date = StringVar()
listbox = Listbox(window, listvariable=view_date, selectmode=SINGLE, height=5)
listbox.grid(column=0, columnspan=2, row=1)

# Scrollbar para la lista
scrollbar = ttk.Scrollbar(window, orient="vertical", command=listbox.yview)
scrollbar.grid(column=2, row=1, sticky="NS")
listbox.configure(yscrollcommand=scrollbar.set)

# visualizacion de interfaz
window.mainloop()
