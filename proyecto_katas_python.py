# %%
#1. Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados.#
def frecuencia_letras(texto):
    frecuencias = {}
    for letra in texto:
        if not letra.isspace():
            frecuencias[letra] = frecuencias.get(letra, 0) + 1
    return frecuencias

print(frecuencia_letras("hola mundo"))

# %%
#2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map()#
def dobles(numeros):
    return list(map(lambda x: x * 2, numeros))

print(dobles([1, 2, 3, 4, 5]))


# %%
#3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.#
def palabras_con_objetivo(palabras, objetivo):
    return [palabra for palabra in palabras if objetivo in palabra]

print(palabras_con_objetivo(["manzana", "banana", "cereza", "mango"], "an"))


# %%
#4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map()#
def diferencia_listas(lista1, lista2):
    return list(map(lambda a, b: a - b, lista1, lista2))

print(diferencia_listas([10, 20, 30], [1, 2, 3]))

# %%
#5. Ecribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por defecto es 5. La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual que nota aprobado. Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver una tupla que contenga la media y el estado.#
def media_y_estado(numeros, nota_aprobado=5):
    media = sum(numeros) / len(numeros)
    estado = "aprobado" if media >= nota_aprobado else "suspenso"
    return media, estado

print(media_y_estado([6, 7, 8, 9, 10]))
print (media_y_estado([0,1,1,2]))

# %%
#6. Escribe una función que calcule el factorial de un número de manera recursiva.# (Me ha costado entender que es lo que se me pedía con factorial)
def factorial(n):
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos.")
    if n in (0, 1):
        return 1
    return n * factorial(n - 1)

print(factorial(5))

# %%
#7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()#
def tuplas_a_strings(tuplas):
    return list(map(lambda t: ' '.join(map(str, t)), tuplas))

print(tuplas_a_strings([(1, 2), (3, 4), (5, 6)]))


# %%
#8. Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico o intenta dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje indicando si la división fue exitosa o no.#
def dividir_numeros(número_a, número_b):
    try:
        resultado = número_a / número_b
        print(f"La división fue exitosa: {resultado}")
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero.")
    except TypeError:
        print("Error: Por favor, ingrese valores numéricos válidos.")

print (dividir_numeros(5, 2))  
print (dividir_numeros(5, 0))  
print (dividir_numeros(5, "x"))  

# %%
#9. Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"].Usa la función filter()#
def filtrar_mascotas(mascotas):
    mascotas_prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
    return list(filter(lambda mascota: mascota not in mascotas_prohibidas, mascotas))

print(filtrar_mascotas(["Perro", "Gato", "Mapache", "Tigre", "Conejo", "Cocodrilo", "Pez"]))

# %%
#10. Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una excepción personalizada y maneja el error adecuadamente.#
def promedio(numeros):
    if not numeros:
        print(ValueError("La lista está vacía. Inserte números para calcular el promedio."))
        return None
    return sum(numeros) / len(numeros)

print (promedio([1, 2, 3, 4, 5]))
print (promedio ([]))

# %%

#11. Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones adecuadamente.#

class EdadFueraDeRangoError(Exception):
    """Se lanza cuando la edad no está entre 0 y 120."""


def pedir_edad(simulado="30"):
    try:
        edad = int(pedir("Introduce tu edad: ", simulado))
        if edad < 0 or edad > 120:
            raise EdadFueraDeRangoError(f"{edad} no está entre 0 y 120.")
    except ValueError:
        print("Error: la edad debe ser un número entero.")
    except EdadFueraDeRangoError as error:
        print(f"Error: edad fuera de rango ({error})")
    else:
        print(f"Edad registrada correctamente: {edad} años.")



# %%
#12. Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map()#
def longitud_palabras(frase):
    return list(map(len, frase.split()))

print (longitud_palabras("Hola mundo desde Python"))

# %%
#13. Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en mayúsculas y minúsculas. Las letras no pueden estar repetidas .Usa la función map()#
def letras_mayusculas_minusculas(conjunto_caracteres):
    letras_unicas = sorted({c.lower() for c in conjunto_caracteres if c.isalpha()})
    return list(map(lambda letra: (letra.upper(), letra.lower()), letras_unicas))

print(letras_mayusculas_minusculas("aAbBcCdeEfFgG"))

# %%
#14. Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Usa la función filter()#
def palabras_con_letra(palabras, letra):
    return list(filter(lambda palabra: palabra.startswith(letra), palabras))

print(palabras_con_letra(["manzana", "banana", "cereza", "mango"], "m"))


# %%
#15. Crea una función lambda que sume 3 a cada número de una lista dada.#
def sumar_tres_a_lista(numeros):
    return list(map(lambda x: x + 3, numeros))

print(sumar_tres_a_lista([1, 2, 3, 4, 5]))

# %%
#16. Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de todas las palabras que sean más largas que n. Usa la función filter()#
def numeros_de_palabras(palabras, n):
    return list(filter(lambda palabra: len(palabra) > n, palabras.split()))

print (numeros_de_palabras("Hola mundo desde mi Python", 4))


# %%
#17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2] corresponde al número quinientos setenta y dos (572). Usa la función reduce()#
from functools import reduce

def lista_a_numero(digitos):
    return reduce(lambda acumulado, digito: acumulado * 10 + digito, digitos, 0)

print(lista_a_numero([5, 7, 2]))


# %%
#18. Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes (nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor o igual a 90. Usa la función filter()#

estudiantes = [
    {"nombre": "Juan", "edad": 20, "calificacion": 85},
    {"nombre": "María", "edad": 22, "calificacion": 92},
    {"nombre": "Pedro", "edad": 19, "calificacion": 78},
    {"nombre": "Ana", "edad": 21, "calificacion": 95},
]

estudiantes_destacados = list(filter(lambda estudiante: estudiante["calificacion"] >= 90, estudiantes))

print(estudiantes_destacados)

# %%
#19. Crea una función lambda que filtre los números impares de una lista dada.#
filtrar_impares = lambda numeros: list(filter(lambda x: x % 2 != 0, numeros))

print(filtrar_impares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


# %%
#20. Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función  filter()#
def filtrar_enteros(lista):
    return list(filter(lambda x: isinstance(x, int), lista))

print (filtrar_enteros([1, "dos", 3, "cuatro", 5, "seis"]))


# %%
#21. Crea una función que calcule el cubo de un número dado mediante una función lambda#
cubo = lambda x: x ** 3

print(cubo(3))


# %%
#22. Dada una lista numérica, obtén el producto total de los valores de dicha lista.Usa la función reduce() .#
def producto_total(numeros):
    return reduce(lambda a, b: a * b, numeros, 1)

print (producto_total([1, 2, 3, 4, 5]))


# %%
#23. Concatena una lista de palabras.Usa la función reduce() .#
def concatenar_palabras(palabras):
    return reduce(lambda a, b: a + " " + b, palabras)

print(concatenar_palabras(["Hola", "mundo", "desde", "Python"]))

# %%
#24. Calcula la diferencia total en los valores de una lista. Usa la función reduce() .#
def diferencia_total(numeros):
    return reduce(lambda a, b: a - b, numeros)

print (diferencia_total([10, 2, 3]))


# %%
# 25. Crea una función que cuente el número de caracteres en una cadena de texto dada.#
def contar_caracteres(cadena):
    return len(cadena)

print(contar_caracteres("Hola mundo desde Python"))


# %%
#26. Crea una función lambda que calcule el resto de la división entre dos números dados.#
resto_division = lambda a, b: a % b

print(resto_division(10, 3))


# %%
#27. Crea una función que calcule el promedio de una lista de números.#
promedio = lambda numeros: sum(numeros) / len(numeros) if numeros else 0

print(promedio([1, 2, 3, 4, 5]))


# %%
#28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.#
def primer_duplicado(lista):
    vistos = set()
    for elemento in lista:
        if elemento in vistos:
            return elemento
        vistos.add(elemento)

print(primer_duplicado([1, 2, 3, 4, 2, 5, 5]))

# %%
#29. Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el carácter '#', excepto los últimos cuatro.# (Me ha costado entender que es lo que pedía)
def enmascarar(variable):
    texto = str(variable)
    if len(texto) <= 4:
        return texto
    return "#" * (len(texto) - 4) + texto[-4:]

print(enmascarar("Contraseña"))

# %%
#30. Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras pero en diferente orden.#
def anagramas(palabra1, palabra2):
    return sorted(palabra1) == sorted(palabra2)

print (anagramas("amor", "roma"))
print(anagramas("hola", "adios"))

# %%
#31. Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar enesa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se lanza una excepción.#

def buscar_nombre():
    nombres = input("Ingrese una lista de nombres separados por comas: ").split(",")
    nombre_a_buscar = input("Ingrese el nombre que desea buscar: ")
    
    if nombre_a_buscar in nombres:
        print(f"El nombre '{nombre_a_buscar}' fue encontrado en la lista.")
    else:
        raise ValueError(f"El nombre '{nombre_a_buscar}' no fue encontrado en la lista.")

print(buscar_nombre())

# %%
#32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona no trabaja aquí#

def buscar_empleado(nombre_completo, lista_empleados):
    for empleado in lista_empleados:
        if empleado["nombre"] == nombre_completo:
            return empleado["puesto"]
    return f"{nombre_completo} no trabaja aquí."

empleados = [
    {"nombre": "Juan Pérez", "puesto": "Gerente"},
    {"nombre": "María López", "puesto": "Analista"},
    {"nombre": "Pedro García", "puesto": "Desarrollador"},
]

print (buscar_empleado("María López", empleados))
print(buscar_empleado("Ana Torres", empleados))


# %%
#33. Crea una función lambda que sume elementos correspondientes de dos listas dadas.#
suma_elementos = lambda lista1, lista2: [a + b for a, b in zip(lista1, lista2)]

print(suma_elementos([1, 2, 3], [4, 5, 6]))

# %%
#34. Crea la clase Arbol , define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son:  crecer_tronco , nueva_rama , crecer_ramas , quitar_rama e info_arbol . El objetivo es implementar estos métodos para manipular la estructura del árbol.#
class Arbol:
    def __init__(self):
        self.tronco = 1
        self.ramas = []

    def crecer_tronco(self):
        self.tronco += 1

    def nueva_rama(self):
        self.ramas.append(1)

    def crecer_ramas(self):
        self.ramas = [rama + 1 for rama in self.ramas]

    def quitar_rama(self, rama):
        if rama in self.ramas:
            self.ramas.remove(rama)

    def info_arbol(self):
        return f"Tronco: {self.tronco}, Ramas: {self.ramas}"

arbol = Arbol()
arbol.crecer_tronco()
arbol.nueva_rama()
arbol.crecer_ramas()
arbol.nueva_rama()
arbol.nueva_rama()
arbol.quitar_rama(2)
print(arbol.info_arbol())

# %%
#36. Crea la clase UsuarioBanco ,representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente. Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y agregar dinero al saldo.#
class UsuarioBanco:
    def __init__(self, nombre, saldo, cuenta_corriente):
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    def retirar_dinero(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad a retirar debe ser mayor que cero.")
        if not self.cuenta_corriente:
            raise ValueError(f"{self.nombre} no tiene cuenta corriente.")
        if cantidad > self.saldo:
            raise ValueError(
                f"Saldo insuficiente: {self.nombre} tiene {self.saldo} y quiere retirar {cantidad}."
            )
        self.saldo -= cantidad

    def transferir_dinero(self, otro_usuario, cantidad):
        otro_usuario.retirar_dinero(cantidad)
        self.agregar_dinero(cantidad)

    def agregar_dinero(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad a agregar debe ser mayor que cero.")
        self.saldo += cantidad

alicia = UsuarioBanco("Alicia", 100, True)
bob = UsuarioBanco("Bob", 50, True)
bob.agregar_dinero(20)
print(f"Bob tras agregar 20 -> saldo: {bob.saldo}")
try:
    alicia.transferir_dinero(bob, 80)
    print(f"Transferencia realizada. Alicia: {alicia.saldo}, Bob: {bob.saldo}")
except ValueError as error:
    print(f"No se pudo transferir 80 de Bob a Alicia: {error}")
alicia.retirar_dinero(50)
print(f"Alicia tras retirar 50 -> saldo: {alicia.saldo}")

# %%
#37. Crea una función llamada procesar_texto que procesa un texto según la opción especificada: contar_palabras ,  reemplazar_palabras , eliminar_palabra . Estas opciones son otras funciones que tenemos que definir primero y llamar dentro de la función procesar_texto .#
import re

def contar_palabras(texto):
    conteo = {}
    for palabra in re.findall(r"\w+", texto.lower()):
        conteo[palabra] = conteo.get(palabra, 0) + 1
    return conteo


def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    patron = rf"\b{re.escape(palabra_original)}\b"
    return re.sub(patron, palabra_nueva, texto)


def eliminar_palabra(texto, palabra):
    patron = rf"\b{re.escape(palabra)}\b"
    sin_palabra = re.sub(patron, "", texto)
    return re.sub(r"\s+", " ", sin_palabra).strip()


def procesar_texto(texto, opcion, *args):
    if opcion == "contar":
        return contar_palabras(texto)
    if opcion == "reemplazar":
        if len(args) != 2:
            raise TypeError("'reemplazar' necesita dos argumentos: palabra_original y palabra_nueva.")
        return reemplazar_palabras(texto, *args)
    if opcion == "eliminar":
        if len(args) != 1:
            raise TypeError("'eliminar' necesita un argumento: la palabra a eliminar.")
        return eliminar_palabra(texto, *args)
    raise ValueError("Opción no válida. Usa 'contar', 'reemplazar' o 'eliminar'.")


print("\n--- Ejercicio 37 ---")
texto_prueba = "el perro corre y el gato duerme mientras el perro ladra"
print(procesar_texto(texto_prueba, "contar"))
print(procesar_texto(texto_prueba, "reemplazar", "perro", "conejo"))
print(procesar_texto(texto_prueba, "eliminar", "el"))
try:
    procesar_texto(texto_prueba, "borrar")
except ValueError as error:
    print(f"Error: {error}")


# %%
#38. Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario.#
def momento_del_dia(hora):
    try:
        hora = int(hora)
        if not 0 <= hora <= 23:
            raise ValueError
    except ValueError:
        print("Hora no válida. Debe ser un número entre 0 y 23.")
        return None
    if 6 <= hora < 14:
        momento = "día"
    elif 14 <= hora < 21:
        momento = "tarde"
    else:
        momento = "noche"
    print(f"A las {hora}h es de {momento}.")
    return momento

print(momento_del_dia(9))
print(momento_del_dia(15))
print(momento_del_dia(22))
print(momento_del_dia(25)) 

# %%
#39. Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica.#
def calificacion_en_texto(nota):
    if nota < 0 or nota > 100:
        raise ValueError("La calificación debe estar entre 0 y 100.")
    if nota < 70:
        return "insuficiente"
    if nota < 80:
        return "bien"
    if nota < 90:
        return "muy bien"
    return "excelente"

print(calificacion_en_texto(65))
print(calificacion_en_texto(75))
print(calificacion_en_texto(85))
print(calificacion_en_texto(95))


# %%
#40. Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo" , "circulo" o  "triangulo" ) y datos (una tupla con los datos necesarios para calcular el área de la figura).#
import math

def calcular_area(figura, datos):
    if figura == "rectangulo":
        base, altura = datos
        return base * altura
    if figura == "circulo":
        radio = datos
        return math.pi * radio ** 2
    if figura == "triangulo":
        base, altura = datos
        return base * altura / 2
    raise ValueError("Figura no válida. Usa 'rectangulo', 'circulo' o 'triangulo'.")

print(calcular_area("rectangulo", (5, 10)))
print(calcular_area("circulo", 3))
print(calcular_area("triangulo", (4, 6)))

# %%
#41. En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el monto final de una compra en una tienda en línea, después de aplicar un descuento.#
def compra_online(precio):
    try:
        precio = float(input("Introduce el precio original del artículo (€): "))
    except ValueError:
        print("Error: el precio debe ser un número.")
        return None
    if precio < 0:
        print("Error: el precio no puede ser negativo.")
        return None

    respuesta = input("¿Tienes un cupón de descuento? (sí/no): ").strip().lower()
    precio_final = precio

    if respuesta in ("sí", "si", "s"):
        try:
            cupon = float(input("Introduce el valor del cupón (€): "))
        except ValueError:
            print("El valor del cupón no es un número. Se continúa sin descuento.")
        else:
            if cupon > 0:
                precio_final = max(precio - cupon, 0)
                print(f"Cupón de {cupon:.2f}€ aplicado.")
            else:
                print("Cupón no válido (debe ser mayor que cero). Se continúa sin descuento.")
    elif respuesta in ("no", "n"):
        print("Sin cupón de descuento.")
    else:
        print("Respuesta no reconocida. Se continúa sin descuento.")

    print(f"Precio final de la compra: {precio_final:.2f}€")
    return precio_final

print(compra_online(100))


