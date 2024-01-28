'''
este es un script que intenta simular una calculadora, pero le pregunta al usuario que operacion quiere hacer
y despues pregunta cuales son los numero que se sumaran, restaran, multiplicaran, etc
para ultimo mostrarle el resultado al usuario de su operacion
'''
# las variable constantes son aquellas que se escriben en mayusculas y no se pueden modificar
# creamos las variables constantes con el valor que debe elejir el usuario
SUMA = 1
RESTA = 2
MULTIPLICACION = 3
DIVISION = 4
DIVISION_ENTERA = 5
MODULO = 6
POTENCIA = 7

# mostramos en consola las operaciones que puede hacer nuestra calculadora
print(f'''

	{SUMA}) suma
	{RESTA}) resta
	{MULTIPLICACION}) multiplicacion
	{DIVISION}) division
	{DIVISION_ENTERA}) division entera
	{MODULO}) modulo
	{POTENCIA}) potencia

''')

# preguntamos al usuario que operacion quiere realizar usando int para convertir el str en num
# luego usamos input para que el usuario escriba su opcion
opc = int(input('selecciona la operacion que quieres realizar: '))
# preguntamos al usuariio cual es el primer numero de su operacion
num1 = int(input('ingresa un numero: '))
# preguntamos al usuariio cual es el segundo numero de su operacion
num2 = int(input('ingrese otro numero: '))

# creamos una rama de condicionales que dependiendo de la opcion de operacion elejida por el usuario
# hara una cosa o la otra
if SUMA <= opc <= POTENCIA:
    # la primera rama de la condiciones, si el usuario elije 1 su operacion sera suma
    if opc == SUMA:
        # sumamos los valores dados por el usuario
        print(f'{num1} + {num2} = {num1+num2}')
    # la segunda rama de la condiciones, si el usuario elije 2 su operacion sera resta
    elif opc == RESTA:
        # restamos los valores dados por el usuario
        print(f'{num1} - {num2} = {num1-num2}')
    # la tercera rama de la condiciones, si el usuario elije 3 su operacion sera multiplicacion
    elif opc == MULTIPLICACION:
        # multiplicamos los valores dados por el usuario
        print(f'{num1} * {num2} = {num1*num2}')
    # la cuarta rama de la condicional, si el usuario elije 4 su operacion sera divicion
    elif opc == DIVISION:
        # un condiciones extra por si la operacion no se puede realizar
        if num1 != 0 and num2 != 0:
            # dividimos los valores dados por el usuario
            print(f'{num1} / {num2} = {num1/num2}')
        else:
            # le mostramos al usuario en consola que su operacion no se puede realizar por lo valores que proporciono
            print('operacion no definida')
    # la quinta rama de la condiciones, si el usuario elije 5 su operacion sera divicion entera
    elif opc == DIVISION_ENTERA:
        # un condicional extra por si la operacion no se puede realizar
        if num1 != 0 and num2 != 0:
            # dividimos los valores dados por el usuario
            print(f'{num1} // {num2} = {num1//num2}')
        else:
            # le mostramos al usuario en consola que su operacion no se puede realizar por lo valores que proporciono
            print('operacion no definida')
    # la sexta rama de la condiciones, si el usuario elije 6 su operacion sera el modulo de una divicion
    elif opc == MODULO:
        if num1 != 0 and num2 != 0:
            # hacemos la operacion y mostramos el modulo de la divicion
            print(f'{num1} % {num2} = {num1%num2}')
        else:
            # le mostramos al usuario en consola que su operacion no se puede realizar por lo valores que proporciono
            print('operacion no definida')
    # la opcion siete rama de la condiciones, si el usuario elije 7 su operacion sera potencias
    elif opc == POTENCIA:
        # potenciamos los valores dados por el usuario
        print(f'{num1} ** {num2} = {num1**num2}')
# ultima condicional que es por si el usuario nos dio un valor que no es corecto, como una letra o simbolo
else:
    print('opcion no valida')
