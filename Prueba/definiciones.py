import os
import time
import numpy

abitaciones = numpy.zeros((2,5),int)


lista_ruts = []
lista_nombres = []
lista_filas = []
lista_columnas = []
lista_totales = []

def mostrar_menu():
    print("""MENÚ
    1. Grabar
    2. Buscar
    3. Retirarse
    4. Salir""")

def validar_opcion():
    while True:
        try:
            opcion = int(input("Ingrese opción: "))
            if opcion in(1,2,3,4):
                return opcion
            else:
                print("ERROR! OPCIÓN INCORRECTA!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")

def validar_rut():
    while True:
        try:
            rut = int(input("Ingrese rut(sin puntos ni dígito verificador): "))
            if len(str(rut)) == 7 and len(str(rut)) == 8:
                return rut
            else:
                print("ERROR! EL RUT DEBE ESTAR ENTRE 1000000 y 99999999!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")

def validar_nombre():
    while True:
        nombre = input("Ingrese nombre: ")
        if len(nombre.strip()) >= 3 and nombre.isalpha():
            return nombre
        else:
            print("ERROR! EL NOMBRE DEBE TENER AL MENOS 3 LETRAS!")

def validar_nombre_perro():
    while True:
        nombre_perro = input("Ingrese nombre: ")
        if len(nombre_perro.strip()) >= 3 and nombre_perro.isalpha():
            return nombre_perro
        else:
            print("ERROR! EL NOMBRE DEBE TENER AL MENOS 3 LETRAS!")

def validar_abitacion_dispo(p_abitacion):
    while True:
        try:
            abitacion = int(input("Ingrese número de abitacion: "))
            if abitacion in(p_abitacion):
                return abitacion
            else:
                print("ERROR! NÚMERO DE ABITACION NO DISPONIBLE!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")

def validar_dias():
    
    while True:
        try:
            dias = int(input("Ingrese cuandos dias dejara a su mascota: "))
            if dias <= 50 and dias >= 1:
                return dias
            else:
                print("ERROR! numero de dias incorrecto!")

        except:
            print("ERROR! ingrese un numero mayor a 0")

def validar_grabar():
    rut = validar_rut()
    nombre_dueño = validar_nombre()

    nombre_perro = validar_nombre_perro()
    dias = validar_dias()
    lista_ruts[rut]
    return rut


def validar_abitacion():
    for x in range(2):
        for y in range(5):
            abitaciones = input("Ingrese la abitacion que desea comprar(1 a 10): ")
            return abitaciones
        

def validar_compra():
    rut = validar_rut()
    dias = validar_dias()
    pago = validar_pago()
    print(f"su total a pagar es {pago} por un total de {dias} dias en la guarderia")


def validar_pago():
    dias = validar_dias()
    pago = 15000 * dias
    return pago

def busqueda_mascota():
    rut = validar_rut()
    for x in range(lista_ruts[rut]):
        print(f"su mascota se encuenta en la siguiente abitacion: {abitaciones}")
        














