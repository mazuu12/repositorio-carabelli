#numero1 = 1
#numero2 = 2 
#suma = 1 + 2
#resta = 1 - 2
#multiplicacion = 1 * 2  

#print("suma:",suma)
#print("resta:",resta)
#print("multiplicacion:",multiplicacion)

#usuario = input("ingresa tu nombre")
#print(f"hola {usuario} loco")

#num1 = int (input("num1:"))
#num2 = int (input("num2:"))
#print("suma:", num1 + num2)

#base = int (input("ingrese base:"))
#altura = int (input("ingrese la altura:"))
#area = base * altura
#print(area)

#nota1 = int (input("ingrese una nota:"))
#nota2 = int (input("ingrese una nota:"))
#nota3 = int (input("ingrese una nota:"))
#print("suma:", nota1 + nota2 + nota3) 

#nombre = "juan"
#apellido = "perez"
#print(nombre + " " + apellido)

#usuario = input("bro escribi algo:")
#print(usuario.upper())
#print(usuario.title())
#print(usuario.lower())

#texto = input("ingrese una palabra:")
#print("la palabra tiene", len(texto), "caracteres")

#numero = int(input("ingrese su edad:"))
#if {numero >=18}:
    #print("edad: es mayor")
#else:
    #print("edad: es menor")

numero = int(input("ingrese un numero:"))
if {numero > 0}:
    print("positivo")
elif {numero == 0}:
    print ("Es igual a 0")
else: 
    print("negativo")

numero = int(input("ingrese un numero:"))
if {numero % 2 == 0}:
    print("es par")
else: 
    print("es numero impar")

num1 = int(input("ingrese un numero:"))
num2 = int(input("ingrse un numero:"))
opciones = input(str ("opciones"))
if {opciones == "+"}:
    print(num1 + num2)
elif {opciones == "-"}:
    print(num1 - num2)
elif {opciones == "*"}:
    print(num1 * num2)
else: 
    print(num1 / num2 )

numerop = int(input("ingrese una nota:"))

if { numerop>=9}:
    print("excelente")
elif {numerop>=7}:
    print("aprobado")
elif {numerop>=5}:
    print("regular")
else:
    print("desaprobado")