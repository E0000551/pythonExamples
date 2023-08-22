opcion = ""
lista = []


while ( opcion != "5" ):
    print("1 Mostrar la lista de tareas")
    print("2 Agregar Tarea")
    print("3 Eliminar tarea")
    print("4 Editar tarea")
    print("5 Salir")
    opcion = input("  Selecciona una opcion: ")

    if opcion == "1" :
        i = 1
        print ( "Mostrando valores en la lista:" );
        for element in lista:
            print ("    ", i, " " ,element);
            i += 1
    elif opcion == "2" :
        valor = input("  Escribe el valor que quieres agregar: ")
        lista.append(valor)
        print("   ",valor, " agregado al final de la lista ")
    elif opcion == "3" :
        valor = input("  Dame el valor que quieres borrar: ")
        lista.remove(valor)
        print("   ",valor, " eliminado de la lista")
    elif opcion == "4" :
        valor = input("  Escribe el valor que quieres actualizar: ")
        nuevovalor = input("  Escribe el nuevo valor: ")
        indice = 0
        found = False
        for element in lista:
            if element == valor:
                lista[indice] = nuevovalor
                found = True
            indice += 1
        if found:
            print("   ",valor, " actualizado por ", nuevovalor)
        else:
            print("   ",valor, " no encontrado ")

    elif opcion == "5" :
        print("bye")
    else:
        print("opcion no valida")
