#1) Meter los números del 1 al 20 en una lista y mostrarla en pantalla. Hacer lo mismo para un rango de números indicado por un usuario. 
#2) Pide un número y guarda en una lista su tabla de multiplicar hasta el 10. Por ejemplo, si pide el 5 la lista tendrá: 5,10,15,20,25,30,35,40,45,50 
#3) Pide una cadena (string) por teclado, mete los caracteres en una lista sin repetir caracteres. 
#4) Pide una cadena (string) por teclado, mete los caracteres en una lista sin espacios. 
#5) Crea una tupla con números, pide un numero por teclado e indica cuantas veces se repite. 
#6) Crea una tupla con los meses del año, pedir números al usuario. Si el numero esta entre 1 y la longitud máxima de la tupla, muestra el contenido de esa posición sino muestra un mensaje de error. El programa termina cuando el usuario introduce un cero 
#7) Crea una tupla con números e indica el número con mayor valor y el que menor tenga.
#8) (Opcional)Escribir un programa que vaya solicitando al usuario que ingrese nombres. - Si el nombre se encuentra en la agenda (implementada con un diccionario), debe mostrar el teléfono y, opcionalmente, permitir modificarlo si no es correcto. - Si el nombre no se encuentra, debe permitir ingresar el teléfono correspondiente. El usuario puede utilizar la cadena "*", para salir del programa 
#9) Opcional: Pide números y mételos en una lista, cuando el usuario meta un 0 ya dejaremos de insertar. Por último, muestra los números ordenados de menor a mayor.
#10) Opcional: Lo mismo que el anterior, pero ordenando de mayor a meno.

print("----")
print("--N°3--")
print("----")
print()
usuario = input("Ingrese un texto: ")
lista = [usuario]
for strigs in usuario:
  if strigs not in lista:
    lista.append(usuario)
print(f"El texto que ingreso es: {lista}")
print(lista)

print("----")
print("--N°4--")
print("----")
print()

cadena = input("Ingrese una cadena de texto: ")

lista_sin_espacios = []

for caracter in cadena:
    if caracter != ' ': 
        lista_sin_espacios.append(caracter)

print("Lista de caracteres sin espacios en la cadena:")
print(lista_sin_espacios)

print("----")
print("--N°5--")
print("----")
print()

tupla_numeros = (1, 2, 3, 4, 5, 3, 2, 6, 7, 3, 8, 3)

numero_buscado = int(input("Ingrese un número: "))

repeticiones = tupla_numeros.count(numero_buscado)

if repeticiones > 0:
    print(f"El número {numero_buscado} se repite {repeticiones} veces en la tupla.")
else:
    print(f"El número {numero_buscado} no se encuentra en la tupla.")
print("----")
print("--N°6--")
print("----")
print()

numeros_tupla = (1, 2, 3, 4, 5, 3, 2, 6, 7, 3, 8, 3)

maximo_valor = max(numeros_tupla)

minimo_valor = min(numeros_tupla)

print(f"El número más alto es: {maximo_valor}")
print(f"El número más bajo es: {minimo_valor}")

print("----")
print("--N1--")
print("----")
print()

lista_numeros_1_al_20 = list(range(1, 21))

print("Lista de números del 1 al 20:")
print(lista_numeros_1_al_20)

inicio = int(input("Ingrese el número de inicio del rango: "))
fin = int(input("Ingrese el número de fin del rango: "))

lista_rango_usuario = list(range(inicio, fin + 1))

print(f"Lista de números en el rango {inicio} al {fin}:")
print(lista_rango_usuario)
print("----")
print("--N2--")
print("----")
print()

numero = int(input("Ingrese un número: "))

tabla_de_multiplicar = []

for i in range(1, 11):
    resultado = numero * i
    tabla_de_multiplicar.append(resultado)

print(f"Tabla de multiplicar del número {numero} hasta 10:")
print(tabla_de_multiplicar)
