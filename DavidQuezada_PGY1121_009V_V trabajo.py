import random

vehiculos = []

def grabar_vehiculo():
    tipo = input("Tipo de vehículo: ")
    patente = input("Patente: ")
    marca = input("Marca: ")
    precio = float(input("Precio: "))
    multas = []
    while True:
        opcion = input("¿Agregar multa? (S/N): ")
        if opcion.lower() == 'n':
            break
        monto = float(input("Monto de la multa: "))
        fecha = input("Fecha de la multa: ")
        multas.append((monto, fecha))
    fecha_registro = input("Fecha de registro del vehículo: ")
    dueño = input("Nombre del dueño: ")

    if not validar_patente(patente):
        print("La patente ingresada no es válida.")
        return

    if not validar_marca(marca):
        print("La marca debe tener entre 2 y 15 caracteres.")
        return

    if precio <= 5000000:
        print("El precio debe ser mayor a $5.000.000.")
        return

    vehiculo = {
        "Tipo": tipo,
        "Patente": patente,
        "Marca": marca,
        "Precio": precio,
        "Multas": multas,
        "Fecha de registro": fecha_registro,
        "Dueño": dueño
    }

    vehiculos.append(vehiculo)
    print("Vehículo registrado exitosamente.")

def buscar_vehiculo():
    patente = input("Ingrese la patente del vehículo: ")
    encontrado = False
    for vehiculo in vehiculos:
        if vehiculo["Patente"] == patente:
            print("Información del vehículo:")
            print("Tipo:", vehiculo["Tipo"])
            print("Patente:", vehiculo["Patente"])
            print("Marca:", vehiculo["Marca"])
            print("Precio:", vehiculo["Precio"])
            print("Multas:", vehiculo["Multas"])
            print("Fecha de registro:", vehiculo["Fecha de registro"])
            print("Dueño:", vehiculo["Dueño"])
            encontrado = True
            break
    if not encontrado:
        print("Vehículo no encontrado.")

def imprimir_certificados():
    for vehiculo in vehiculos:
        cert_emision = random.uniform(1500, 3500)
        cert_anotaciones = random.uniform(1500, 3500)
        cert_multas = random.uniform(1500, 3500)

        print("Certificado de Emisión de Contaminantes")
        print("Patente:", vehiculo["Patente"])
        print("Dueño:", vehiculo["Dueño"])
        print("Valor:", cert_emision)

        print("Certificado de Anotaciones Vigentes")
        print("Patente:", vehiculo["Patente"])
        print("Dueño:", vehiculo["Dueño"])
        print("Valor:", cert_anotaciones)

        print("Certificado de Multas")
        print("Patente:", vehiculo["Patente"])
        print("Dueño:", vehiculo["Dueño"])
        print("Valor:", cert_multas)

def validar_patente(patente):
    
    return True

def validar_marca(marca):
    return 2 <= len(marca) <= 15

def menu():
    while True:
        print("\n--- Automotora Auto Seguro ---")
        print("1. Grabar vehículo")
        print("2. Buscar vehículo")
        print("3. Imprimir certificados")
        print("4. Salir")
        opcion = input("Ingrese una opción: ")

        if opcion == '1':
            grabar_vehiculo()
        elif opcion == '2':
            buscar_vehiculo()
        elif opcion == '3':
            imprimir_certificados()
        elif opcion == '4':
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

menu()