
#customtkinter es un modulo para ser interfaces mas modernas
from customtkinter  import CTk, CTkFrame, CTkEntry, CTkLabel,CTkButton,CTkCheckBox, CTkLabel 
import tkinter
from tkinter import ttk
from tkinter import messagebox, Toplevel

# variable de colores
c_pink = '#f73772'
c_light_pink = 'pink'


# configracion de la ventana
window = CTk()
window.geometry("400x500+700+50")
window.title("login")
window.minsize(width=400, height=500)
window.config(bg = c_light_pink)


# variables constantes 
email =  "edimez14@gmail.com"
password = "244255266"

# fucionamiento de login
def login():
	global email
	global password

	email_date = email_entry.get()
	password_date = password_entry.get()

	if email_date != email and password_date != password:
		messagebox.showerror(title = "error", message = "incorrect email and password")
	elif email_date != email:
		messagebox.showerror(title = "error", message = "incorrect email address")
	elif password_date != password:
		messagebox.showerror(title = "error", message = "incorrect password")
	else:
		newwindow = Toplevel(window)
		newwindow.geometry("200x100+700+50")
		newwindow.minsize(width=200, height=100)
		newwindow.config(bg = c_light_pink)
		label_welcome = CTkLabel(master=newwindow, text='WELCOME', text_color='white',
			font=('Ariel', 30))
		label_welcome.place(x = 25, y = 25)

# configurando el widget
widget = CTkFrame(master=window, width=350, height=460, corner_radius=10, fg_color='black')
widget.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)


# configuracion de las diviciones del widget
# configuracion para informa al usuario que esta ingresando
div_login = CTkFrame(master=widget, fg_color='black', width=300, height=150)
div_login.place(relx=0.5, rely=0.33, anchor=tkinter.S)
label_login = CTkLabel(master=widget, text='LOGIN', text_color='white',
	font=('Ariel', 50), width=300, height=150)
label_login.place(relx=0.5, rely=0.43, anchor=tkinter.S)

# configuracion donde el usuario debe ingresar sus datos
div_date = CTkFrame(master=widget, fg_color='black', width=300, height=150)
div_date.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

# variables de introducion de datos
email_entry = CTkEntry(div_date, font = ('sans rerif', 12), placeholder_text = 'email address',
	text_color = "white", border_color = c_pink, fg_color = 'black', width = 220, height = 40)
email_entry.grid(columnspan = 2, row = 1, padx = 4, pady = 4)
password_entry = CTkEntry(div_date, font = ('sans rerif', 12), placeholder_text = 'password',
	border_color = c_pink, text_color = "white", fg_color = 'black', width = 220, height = 40)
password_entry.grid(columnspan = 2, row = 2, padx = 4, pady = 4)

# variable para recordar los datos introducidos
# remember_date = CTkCheckBox(div_date, text = "remember the date login", text_color = "white", hover_color = c_pink,
# 	border_color = c_pink, fg_color = c_pink)
# remember_date.grid(columnspan = 1, row = 3, padx = 4, pady = 4)

# configuracion para el boton de ingresar o el mesaje de error en los datos
div_enter = CTkFrame(master=widget, fg_color='black', width=300, height=150)
div_enter.place(relx=0.5, rely=0.67, anchor=tkinter.N)

# variable para el boton de iniciar
bt_login = CTkButton(div_enter, font = ("sans rerif", 12),fg_color = "black", text_color = "white",
	border_color = c_pink, hover_color = c_pink, corner_radius = 12, border_width = 2,
	text = "LOGIN", command = login)
bt_login.grid(columnspan = 2, row = 0, padx = 4, pady = 4)

window.mainloop()