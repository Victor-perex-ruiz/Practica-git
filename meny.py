#Logica para un pequeño sistema de menú para un Minimarket, el menú principal cuenta con 3 categorias, Verduras, Menestras, Carnes
#Definiendo la lógica del sistema
import os
def clear_screen():
    #comprobación de sistema operatibo
    if os.name == 'nt' : #windows
            os.system('cls')
    else: #Linux y macOS
        os.system('clear')
clear_screen()
def mostrar_menu(opciones):
    print("=============================================")
    print("|  Restaurante JUNGLE RUN RUN               |")
    print("|          Productos:                       |")
    for opcion, detalle in opciones.items():
        descripcion = detalle["descripción"]
        if "precio" in detalle: 
            precio = detalle["precio"]
            print(f"| {opcion}. {descripcion.ljust(18)}: {precio} soles |")
        else:
            print(f"| {opcion}. {descripcion.ljust(18)}                 |")
    print("==============================================")
    print("")

def obtener_opcion():
    print("==============================================")
    opcion = input("Selecciona una opción: ")
    return opcion

def mostrar_submenu(opcion_principal, submenu, total_preventa):
    while True:
        print("===============================================")
        print(f"|               Submenú: {opcion_principal}    |")
        for opcion, detalle in submenu. items():
            descripcion = detalle["descripción"]
            precio = detalle["precio"]
            if opcion.lower() == "v":
                print("| V. Volver al Menú principal           |")
            else:
                print(f"| {opcion}. {descripcion.ljust(18)}: {precio} soles|")
        print("================================================")
        opcion_submenu = input("Selecciona una opción:      ").lower() #Convertir a minúsculas
        if opcion_submenu == "v":
            print("Volviendo al Menú Principal...")
            return total_preventa # Retornar el valor actualizado de total_preventa
        if opcion_submenu in submenu:
            item_seleccionado = submenu[opcion_submenu]
            
            total_preventa += item_seleccionado["precio"]
            print(f"Has seleccionado:{item_seleccionado['descripción']} - {item_seleccionado['precio']} soles")
        else: 
            print("Opción inválida. Por  favor, selecciona una opción válida del submenu.")

    return total_preventa # Por si acaso el bucle termina sin seleccionar la opción "v"


opciones_aperitivos = {
    "1" : {"descripción": "Tequeños Amazónicos", "precio": 14.0},
    "2" : {"descripción": "Piqueo Amazónicos", "precio": 13.0},
    "3" : {"descripción": "Tortilla de jamón", "precio": 9.0},
    "4" : {"descripción": "Humita", "precio": 10.0},
    "5" : {"descripción": "Tamal", "precio": 7.0},
    "6" : {"descripción": "Juane", "precio": 15.0},
    "7" : {"descripción": "Causa", "precio": 9.0},
    "v" : {"descripción": "Volver al Menú principal", "precio": 0.0},
}

opciones_ensaladas ={
    "1" : {"descripción": "Ensalada de palmito", "precio": 8.0},
    "2" : {"descripción": "Ensalada rusa", "precio": 7.0},
    "3" : {"descripción": "Ensalada de chonta", "precio": 12.0},
    "4" : {"descripción": "Ensalda de palta", "precio": 8.0},
    "v" : {"descripción": "Volver al Menú principal", "precio": 0.0}
}

opciones_carnes = {
    "1" : {"descripción": "Juane de gallina", "precio": 15.0},
    "2" : {"descripción": "Cecina con patacones", "precio": 18.0},
    "3" : {"descripción": "Pechuga de pollo con papas doradas", "precio": 17.0},
    "4" : {"descripción": "Lomo saltado", "precio": 18.0},
    "5" : {"descripción": "Saltado de pollo", "precio": 20.0},
    "6" : {"descripción": "Bistec a lo pobre", "precio": 19.0},
    "7" : {"descripción": "Aguadito de pollo", "precio": 18.0}, 
    "v" : {"descripción": "Volver al Menú principal", "precio": 0.0}
}

opciones_pescados = {
    "1" : {"descripción": "Gamitana asada con patacones", "precio": 15.0},
    "2" : {"descripción": "Paiche frito con patacones", "precio": 18.0},
    "3" : {"descripción": "Palometa envuelto en hoja con patacones ", "precio": 17.0},
    "4" : {"descripción": "Picadillo de paiche con patacones", "precio": 18.0},
    "5" : {"descripción": "Doncella asada con patacones", "precio": 20.0},
    "v" : {"descripción": "Volver al Menú principal", "precio": 0.0}
}

opciones_bebidas = {
    "1" : {"descripción": "Camu Camu", "precio": 12.0},
    "2" : {"descripción": "Cocona", "precio": 12.0},
    "3" : {"descripción": "Aguajina", "precio": 12.0},
    "4" : {"descripción": "Unghurai", "precio": 15.0},
    "5" : {"descripción": "Tumbo", "precio": 8.0},
    "6" : {"descripción": "Agua con gas", "precio": 6.0},
    "7" : {"descripción": "Agua sin gas", "precio": 6.0},
    "8" : {"descripción": "INKA personal", "precio": 6.0},
    "9" : {"descripción": "Coca Cola personal", "precio": 6.0},
    "v" : {"descripción": "Volver al Menú principal", "precio": 0.0}
}

opciones_adicionales = {
    "1" : {"descripción": "Tacacho", "precio": 5.0},
    "2" : {"descripción": "Plátano frito", "precio": 5.0},
    "3" : {"descripción": "Yuca frita", "precio": 4.0},
    "4" : {"descripción": "Papa frita", "precio": 4.0},
    "5" : {"descripción": "Papas doradas", "precio": 6.0},
    "6" : {"descripción": "Maduro frito", "precio": 4.0},
    "7" : {"descripción": "Maduro asado", "precio": 4.0},
    "8" : {"descripción": "Platano asado", "precio": 4.0},
    "v" : {"descripción": "Volver al Menú principal", "precio": 0.0}
}


# Menú principal del programa
