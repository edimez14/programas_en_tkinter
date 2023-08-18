from tkinter import *
from tkinter import ttk 

# configuraciones de la ventana
window = Tk()
# window.geometry("100x200+700+50")
window.title("login")
# window.minsize(width=100, height=100)
# window.config(bg = "black")

list_time = [
	"secunds to minutes", 
	"secunds to hours", 
	"minutes to secunds", 
	"minutes to hours",
	"hours to secunds"
]

# funciones para la logica de programa
def select():
	# variables para a definicion de tiempos
	segundos_por_minuto = 60
	minutos_por_hora = 60
	segundos_por_hora = 3600

	i = menu.get()  # Obtener la opción seleccionada en el menu

	if i == list_time[0]:  # segundos a minutos
	    value = int(valor.get())
	    valor_time.set(value // segundos_por_minuto) 
	    valor_secunds.set(value % segundos_por_minuto)
	    result.set("minutes") 
	elif i == list_time[1]:  # segundos a horas
	    value = int(valor.get())
	    valor_time.set(value // segundos_por_hora)
	    valor_secunds.set(0)
	    result.set("hours")
	elif i == list_time[2]:  # minutos a segundos
	    value = int(valor.get())
	    valor_time.set(value * segundos_por_minuto) 
	    valor_secunds.set(0)  # No hay segundos en esta conversión
	    result.set("secunds")
	elif i == list_time[3]:  # minutos a horas
	    value = int(valor.get())
	    valor_time.set(value // minutos_por_hora)
	    valor_secunds.set(value % minutos_por_hora)
	    result.set("hours")
	elif i == list_time[4]:  # horas a segundos
	    value = int(valor.get())
	    valor_time.set(value * (segundos_por_minuto * minutos_por_hora))
	    valor_secunds.set(0)  # No hay segundos en esta conversión
	    result.set("secunds")

def calculate(*args):
	return select()

# el frame que contine los widget de la ventana
mainframe = ttk.Frame(window, padding='3 3 12 12')
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)

# declaramos la variable que contendra el valor que queremos convertir a metros
valor = StringVar()
valor_entry = ttk.Entry(mainframe, width=7, textvariable=valor)
valor_entry.grid(column=2,columnspan=2, row=1, sticky=(W, E))

# declaramos la variable que mostrara el valor convertido
valor_time = StringVar()
ttk.Label(mainframe, textvariable=valor_time).grid(column=2, row=2, sticky=(W, E))
valor_secunds = StringVar()
ttk.Label(mainframe, textvariable=valor_secunds).grid(column=3, row=2, sticky=(W, E))

menu = StringVar() 
drop = OptionMenu(mainframe, menu, *list_time)
drop.grid(column=4, row=1, sticky=W)
# el boton para convrtir los valores
ttk.Button(mainframe, text='calculate', command=calculate).grid(column=3, row=3, sticky=W)

# los bloques que muestran los valores del usuario
ttk.Label(mainframe, text='is equivalent to').grid(column=1, row=2, sticky=E)
result = StringVar()
ttk.Label(mainframe, textvariable=result).grid(column=4, row=2, sticky=E)

window.mainloop()