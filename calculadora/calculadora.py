
from tkinter import *
from tkinter import ttk

# variables de color
c_blue = "#bfe6f9"
c_pink_1 = "#fdc0ca"
c_pink_2 = "#95676b"
c_pink_3 = "#f1929f"
c_brown = "#332c2c"

# variables globales
current_number = ""
operator = ""
first_operand = None

window = Tk()
window.title("calculadora")
window.geometry("400x500")
window.minsize(width=400, height=500)
window.configure(bg=c_pink_1)

# funciones


def handle_input(value):
    global current_number
    current_number += value
    screen.set(current_number)


def handle_operator(value):
    global current_number, operator, first_operand
    if current_number:
        if first_operand is None:
            first_operand = int(current_number)
        else:
            first_operand = perform_operation(
                first_operand, int(current_number), operator)
        current_number = ""
        operator = value
        screen.set(str(first_operand) + operator)


def perform_operation(operand1, operand2, op):
    if op == "+":
        return operand1 + operand2
    elif op == "-":
        return operand1 - operand2
    elif op == "*":
        return operand1 * operand2
    elif op == "/":
        return operand1 / operand2


def calculate_result():
    global current_number, operator, first_operand
    if current_number and operator and first_operand is not None:
        result = perform_operation(
            first_operand, int(current_number), operator)
        screen.set(result)
        current_number = str(result)
        operator = ""
        first_operand = None


def clear_screen():
    global current_number
    current_number = ""
    screen.set("")


def do_nothing():
    pass


# estilos
style_frame = ttk.Style()
style_frame.configure("TFrame", background=c_pink_3)
style_button = ttk.Style()
style_button.configure("TButton", background=c_pink_1, font=('Chandas', 20))
# style_border = ttk.Style()
# style_border.configure("TBorder", background=c_pink_2)


# frame
mainframe = ttk.Frame(window, width=400, height=500, style="TFrame")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

# label para ver los resultados
screen = StringVar()
ttk.Label(mainframe, textvariable=screen, background=c_blue,
          font=('Arial', 25, 'bold')).place(x=10, y=10, width=380, height=50)

# frame contenedor de los numeros y los operadores
content = ttk.Frame(mainframe, width=380, height=350)
content.place(x=10, y=110)
content.config(border=1, relief="solid")

# frame para los botones de los numeros
num = ttk.Frame(content, width=241, height=349)
num.place(x=0, y=0)
num.config(border=1, relief="solid")

# button de numeros
buttum_num_punto = ttk.Button(
    num, text=".", command=lambda: handle_input('.'), style="TButton")
buttum_num_punto.place(x=160, y=261.75, width=78, height=79)
buttum_num_00 = ttk.Button(
    num, text="00", command=lambda: handle_input('00'), style="TButton")
buttum_num_00.place(x=80, y=261.75, width=78, height=79)
buttum_num_0 = ttk.Button(
    num, text="0", command=lambda: handle_input('0'), style="TButton")
buttum_num_0.place(x=0, y=261.75, width=78, height=79)
buttum_num_1 = ttk.Button(
    num, text="1", command=lambda: handle_input('1'), style="TButton")
buttum_num_1.place(x=0, y=174.5, width=78, height=79)
buttum_num_2 = ttk.Button(
    num, text="2", command=lambda: handle_input('2'), style="TButton")
buttum_num_2.place(x=80, y=174.5, width=78, height=79)
buttum_num_3 = ttk.Button(
    num, text="3", command=lambda: handle_input('3'), style="TButton")
buttum_num_3.place(x=160, y=174.5, width=78, height=79)
buttum_num_4 = ttk.Button(
    num, text="4", command=lambda: handle_input('4'), style="TButton")
buttum_num_4.place(x=0, y=87.25, width=78, height=79)
buttum_num_5 = ttk.Button(
    num, text="5", command=lambda: handle_input('5'), style="TButton")
buttum_num_5.place(x=80, y=87.25, width=78, height=79)
buttum_num_6 = ttk.Button(
    num, text="6", command=lambda: handle_input('6'), style="TButton")
buttum_num_6.place(x=160, y=87.25, width=78, height=79)
buttum_num_7 = ttk.Button(
    num, text="7", command=lambda: handle_input('7'), style="TButton")
buttum_num_7.place(x=0, y=0, width=78, height=79)
buttum_num_8 = ttk.Button(
    num, text="8", command=lambda: handle_input('8'), style="TButton")
buttum_num_8.place(x=80, y=0, width=78, height=79)
buttum_num_9 = ttk.Button(
    num, text="9", command=lambda: handle_input('9'), style="TButton")
buttum_num_9.place(x=160, y=0, width=78, height=79)

# frame para los botones de los operadores
op = ttk.Frame(content, width=119, height=349)
op.place(x=260, y=0)
op.config(border=1, relief="solid")

# botones de los operadores
op_ce = ttk.Button(op, text="CE", command=clear_screen, style="TButton")
op_ce.place(x=0, y=0, width=57, height=67.8)
op_c = ttk.Button(op, text="C", command=do_nothing, style="TButton")
op_c.place(x=60, y=0, width=57, height=67.8)
op_igual = ttk.Button(op, text="=", command=calculate_result, style="TButton")
op_igual.place(x=60, y=69.8, width=57, height=277)
op_divi = ttk.Button(
    op, text="%", command=lambda: handle_operator('/'), style="TButton")
op_divi.place(x=0, y=69.8, width=57, height=67.8)
op_multi = ttk.Button(
    op, text="*", command=lambda: handle_operator('*'), style="TButton")
op_multi.place(x=0, y=139.6, width=57, height=67.8)
op_res = ttk.Button(
    op, text="-", command=lambda: handle_operator('-'), style="TButton")
op_res.place(x=0, y=209.4, width=57, height=67.8)
op_sum = ttk.Button(
    op, text="+", command=lambda: handle_operator('+'), style="TButton")
op_sum.place(x=0, y=279.2, width=57, height=67.8)

# visualizar la interfaz
window.mainloop()
