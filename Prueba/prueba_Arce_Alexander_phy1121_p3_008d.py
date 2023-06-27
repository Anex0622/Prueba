import definiciones as fn
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
def validar_pago():
    dias = validar_dias()
    pago = 15000 * dias
    return pago
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

while True:
    mostrar_menu()
    opcion = validar_opcion()
    if opcion == 1:
        fn.validar_grabar()
    elif opcion == 2:
        fn.busqueda_mascota()
    elif opcion == 3:
        fn.validar_pago()
    else:
        print("Gracias por preferirnos a nosotros!")