import os

def clear(): 
    if os.name == "posix":
        os.system ("clear")
    elif os.name == ("ce", "nt", "dos"):
        os.system ("cls")
        
#########################
       #TRABAJO:
#########################
    
lista_avril = ["When youre gone", "Complicated", "What the hell", "Complicated"]

continuar = True

while continuar:
    os.system("cls")
    print "\t--AVRIL LAVIGNE--\n"
    print "Objetivo del programa: Agrege, Elimine, Ordene o Busque, canciones sobre la cantante AVRIL LAVIGNE."
    print "\nLista Actual: ", lista_avril, "\n"
    print "Opciones:\n"
    print "1- Agregar cancion."
    print "2- Agregar VARIAS canciones."
    print "3- Agregar cancion a un posicion determinada."
    print "4- Eliminar ultima cancion de la lista."
    print "5- Eliminar cancion por posicion."
    print "6- Eliminar cancion."
    print "7- Ordenar lista en REVERSA."
    print "8- Ordenar lista en forma ascendente."
    print "9- Ordenar lista en forma descendente."
    print "10- Buscar cancion repetidas."
    print "11- Buscar posicion de una cancion."
    print "12- Ninguna opcion."
    num = input("\nElija Opcion: ")
    os.system("cls")
    if int(num) == 1:
        print "Lista Actual: ", lista_avril, "\n"
        x = raw_input ("\nCancion: ")
        lista_avril.append(x)
        print "Lista Actualizada: ", lista_avril
    
    elif int(num) == 2:
        continuar1 = True
        while continuar1:
            print "Lista Actual: ", lista_avril, "\n"
            z = raw_input ("\nCancion: ")
            lista_avril.extend([z])
            print "Lista Actualizada: ", lista_avril
            continuar1 = ("s" == raw_input("\nAgregar otra cancion? s/n: ").lower())
            os.system("cls")
    
    elif int(num) == 3:
        print "Lista Actual: ", lista_avril, "\n"
        q = raw_input("\nCancion: ")
        qdet = input("Posicion: ")
        lista_avril.insert(qdet-1, q)
        print "Lista Actualizada: ", lista_avril

    elif int(num) == 4:
        print "Lista Vieja: ", lista_avril, "\n"
        lista_avril.pop()
        print "Lista Actualizada: ", lista_avril

    elif int(num) == 5:
        print "Lista Actual: ", lista_avril, "\n"
        p = input("Posicion: ")
        lista_avril.pop(p-1)
        print "Lista Actualizada: ", lista_avril

    elif int(num) == 6:
        print "Lista Actual: ", lista_avril, "\n"
        w = raw_input("\nCancion a eliminar: ")
        lista_avril.remove(w)
        print "Lista Actualizada: ", lista_avril

    elif int(num) == 7:
        print "Lista Actual: ", lista_avril, "\n"
        lista_avril.reverse()
        print "Lista Actualizada: ", lista_avril

    elif int(num) == 8:
        print "Lista Actual: ", lista_avril, "\n"
        lista_avril.sort()
        print "Lista Actualizada: ", lista_avril

    elif int(num) == 9:
        print "Lista Actual: ", lista_avril, "\n"
        lista_avril.sort(reverse=True)
        print "Lista Actualizada: ", lista_avril

    elif int(num) == 10:
        print "Lista Actual: ", lista_avril, "\n"
        y = raw_input("\nCancion a buscar: ")
        print "Veces repetidas: ", lista_avril.count(y)

    elif int(num) == 11:
        print "Lista Actual: ", lista_avril, "\n"
        m = raw_input("\nCancion a buscar: ")
        print "Posicion: ", lista_avril.index(m)

    elif int(num) == 12:
        print ""
    
    else:
        print "\nOpcion Incorrecta."
    continuar = ("s" == raw_input("\nDesea continuar con el programa? s/n: ").lower())

os.system("cls")
print "Lista Final: ", lista_avril, "\n"
print "Gracias por utilizar nuestro programa :)\n"
raw_input("Presione una tecla para salir...")
    



