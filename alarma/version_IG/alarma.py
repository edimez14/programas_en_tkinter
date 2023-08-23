'''
alarma en python 
'''
# importamos los modulos que usaremos para hacer la alarma
from tkinter import Tk, Label, ttk, messagebox 
from time import strftime 
from pygame import mixer
 
# hacemos la configuracion de la ventana
window = Tk()
window.config(bg='#77fdca')
window.geometry('500x250')
window.title('alarm')
window.minsize(width=500, height=250)
mixer.init()

# listas que contiene el tiempo
list_hour = []
list_minute = []
list_seconds = []

# ciclos for para el funcionamineto de el tiempo
for i in range(0, 24):
	list_hour.append(i)
for i in range(0, 60):
	list_minute.append(i)
for i in range(0, 60):
	list_seconds.append(i)

# mostramos en la ventana la localizacion de asignar el tiempo de l alarma
text1 = Label(window, text= 'hour', bg= '#77fdca', fg= 'black', font= ('Arial', 12, 'bold'))
text1.grid(row=1, column=0, padx=5, pady=5)
text2 = Label(window, text= 'minute', bg= '#77fdca', fg= 'black', font= ('Arial', 12, 'bold'))
text2.grid(row=1, column=1, padx=5, pady=5)
text3 = Label(window, text= 'seconds', bg= '#77fdca', fg= 'black', font= ('Arial', 12, 'bold'))
text3.grid(row=1, column=2, padx=5, pady=5)

# mostramos los bloques donde podemos seleccionar el tiempo que queremos que suene la alarma
combobox1 = ttk.Combobox(window, values = list_hour, style = "TCombobox", justify='center', width='12', font='Ariel')
combobox1.grid(row=2, column=0, padx=15, pady=5)
combobox1.current(0)
combobox2 = ttk.Combobox(window, values = list_minute, style = "TCombobox", justify='center', width='12', font='Ariel')
combobox2.grid(row=2, column=1, padx=15, pady=5)
combobox2.current(0)
combobox3 = ttk.Combobox(window, values = list_seconds, style = "TCombobox", justify='center', width='12', font='Ariel')
combobox3.grid(row=2, column=2, padx=15, pady=5)
combobox3.current(0)

# el estilo de la ventana y partes de la interfas
style = ttk.Style()
style.theme_create('combostyle', parent='alt', settings = {'TCombobox':
	{'configure':{
	'selectbackground': '#10a8bb',
	'fieldbackground': '#10a8bb',
	'background': 'white'
	}}})
style.theme_use('combostyle')


# la funcionalidad para seleccionar las opciones para asignar la hora que suene la alarma
window.option_add('*TCombobox*Listbox*Background', 'white')
window.option_add('*TCombobox*Listbox*Foreground', 'black')
window.option_add('*TCombobox*Listbox*selectBackground', '#1750b8')
window.option_add('*TCombobox*Listbox*selectForeground', 'black')

# mostramos cuando sonara la alarma y cuantas veces
alarm = Label(window, fg = '#040f7b', bg = '#77fdca', font = ('Radioland', 20))
alarm.grid(column=0, row=3, sticky='nsew', ipadx=5, ipady=20)
repeat = Label(window, fg = 'black', bg = '#77fdca', text = 'repeat', font = ('Arial'))
repeat.grid(column=1, row=3, sticky='nsew', ipadx=5, ipady=20)
amount = ttk.Combobox(window, values = (1,2,3,4,5), justify='center', width='8', font = ('Arial'))
amount.grid(column=2, row=3, sticky='nsew', ipadx=5, ipady=10)
amount.current(0)

# funcion para mostras la hora en la parte superior y la hora a la que va a sonar, ademas de que sonara la musica cuando sea el momento
def obtain_time():
	x_hour = combobox1.get()
	x_minutes = combobox2.get()
	x_seconds = combobox3.get()

	hour = strftime('%H')
	minutes = strftime('%M')
	seconds = strftime('%S')

	total_hour = (hour + ' : ' + minutes + ' : ' + seconds)
	text_hour.config(text=total_hour, font = ('Radioland', 25))

	alarm_hour = x_hour + ' : ' + x_minutes + ' : ' + x_seconds
	alarm['text']= alarm_hour
	if int(minutes) == int(x_minutes):
		 if int(hour) == int(x_hour):
		 	if int(seconds) == int(x_seconds):
		 		mixer.music.load("y2mate.com - The Big Bang Theory IntroLyrics.mp3")
		 		mixer.music.play(loops= int(amount.get()))
		 		messagebox.showinfo(message=alarm_hour, title="alarm")
	text_hour.after(100, obtain_time)
text_hour = Label(window, fg = 'black', bg='#77fdca')
text_hour.grid(columnspan=3, row=0, sticky="nsew", ipadx=5, ipady=20)

# ejecutamos la funcion y hacemos que se visualize la ventana
obtain_time()
window.mainloop()


