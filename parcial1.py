
herramientas = []
cantidades = []

#TODO ver inventario antes de agregar herramientas o cantidades genera un error, arreglar esto
#TODO no permitir numero en la carga de herramientas
#TODO en el punto 6 si se pone una letra como cantidad, int(cantidad_agregar_herramienta) rompe el codigo porque las letras no son int
#TODO poner mensaje en caso de consultar stock y que no hayan agotados

#Carga Inicial de Herramientas: Registrar los nombres de las herramientas que se pondrán a la venta.
# Se debe preguntar al usuario la cantidad de herramientas a cargar y se debe usar una estructura pertinente. 
# En caso de nombre vacío o duplicado se debe seguir pidiendo hasta que sea correcto respetando la cantidad de herramientas 
# que el usuario indicó antes de la carga.

eleccion = "0"
while not eleccion == "8":
    eleccion = input("\n1)Carga de herramientas\n2)Carga de existencias\n3)Ver inventario\n4)Consulta de stock\n5)Agotados\n6)Nuevo producto\n7)Actualizar stock (compra/venta)\n8)Salir\n")




    #CARGA DE HERRAMIENTAS
    if eleccion == "1":

        validacion_cantidad_de_herramientas = False #Para mantener la usuario en un bucle hasta que ponga entradas válidas
        while not validacion_cantidad_de_herramientas:

            cantidad_de_herramientas = input("Cuantas herramientas va a cargar?\n")

            if not cantidad_de_herramientas.isdigit():
                print("Opcion inválida, use solo numeros\n")

            else:
                validacion_cantidad_de_herramientas = True #Para salir del bucle

                contador = 1 #esto es solo para contar el numero de herramientas en el input

                for i in range(int(cantidad_de_herramientas)):


                    herramienta_valida = False #si el usuario pone una entrada invalida, igual cuenta un ciclo en el for, este while es para solucionar eso

                    while not herramienta_valida:

                        nombre_de_herramienta = input(f"Herramienta n°{contador} de {cantidad_de_herramientas}: ")

                        #verificar que la entrada no sea duplicada ni vacia
                        if nombre_de_herramienta == "" or nombre_de_herramienta.strip() == "": #strip() quita los espacios vacios al inicio y al final del string
                            print("Nombre vacio, ingrese la herramienta")
                            
                        
                        elif(nombre_de_herramienta in herramientas):
                            print(f"{nombre_de_herramienta} ya fue agregada")
                            
                        
                        else:

                            contador += 1
                            herramientas.append(nombre_de_herramienta)
                            herramienta_valida = True
























    #Carga de Existencias: Ingresar la cantidad de unidades para cada herramienta registrada previamente, respetando el orden de ingreso. 
    #Cuando el usuario ingresa existencias, el sistema debe mostrar por pantalla el nombre de la herramienta.

    #CARGA DE EXISTENCIAS
    elif eleccion == "2":

        #Me acabo de dar cuenta de que tengo que guardar las herramientas  y a la vez hacer que guarden relacion con otro valor
        #que es el numero de existencias, quizas pueda hacer que las herramientas se guarden en forma de lista y que cada lista
        #tenga 2 valores, el nombre y la cantidad
        #la otra opcion son 2 listas y que se conecten herramientas y cantidades por el indice, pero entonces hay que tener cuidado 
        #por si se borra una herramienta o varias, que mueven todos los indices
        #no pienso trabajar con tuplas

        if not herramientas: #este if es true si la lista esta vacia, una lista vacia es False
            print("No hay herramientas cargadas")
        
        else:
            for i in range(len(herramientas)):
                

                stock_de_herramienta = ""
                while not stock_de_herramienta:
                    stock_de_herramienta = int(input(f"Ingrse la cantidad de {herramientas[i]}: "))

                    if not stock_de_herramienta.is_integer():
                        print("Entrada invalida, use solo numeros\n")
                        stock_de_herramienta = ""

                        

                    else:    
                        cantidades.append(stock_de_herramienta)

















    #Visualización de Inventario: Mostrar el listado completo de herramientas junto a su stock actual.

    #VISUALIZACION DE INVENTARIO

    elif eleccion == "3":
        
        print("\nINVENTARIO:\n")
        for i in range(len(herramientas)):
            print(f"{herramientas[i]} : {cantidades[i]}\n")




















    #Consulta de Stock (existencias): Buscar una herramienta por su nombre y mostrar cuántas unidades hay disponibles.


    #CONSULTA DE STOCK

    if eleccion == "4":
        buscar_herramienta = input("\nBuscar: ")

        if buscar_herramienta in herramientas:
            print(f"herramienta: {buscar_herramienta}, Stock: {cantidades[herramientas.index(buscar_herramienta)]}")

        else:
            print("\nno se encontró la herramienta\n")
















    #Reporte de Agotados: Listar únicamente aquellos productos cuyo stock sea igual a cero.

    #REPORTA DE AGOTADOS

    if eleccion == "5":

        if "0" in cantidades:
            print("\nAGOTADOS:\n")
            for i in range(len(cantidades)):
                if cantidades[i] == "0":
                    print(f"{herramientas[i]}")

        # else:


















    #Alta de Nuevo Producto: Permitir agregar solo una nueva herramienta al final de las listas con su stock inicial. 
    # En caso de nombre vacío, nombre duplicado o valor de existencia negativo se debe volver al menú principal 
    # mostrando por pantalla el motivo

    #ALTA DE NUEVOS PRODUCTOS

    if eleccion == "6":
        
        validar_agrear_herramienta = False
        while not validar_agrear_herramienta:

            agregar_herramienta = input("Ingrese nueva herramienta: ")

            if (agregar_herramienta.isdigit()) or (agregar_herramienta == ""):
                print("entrada invalida, solo se permiten letras. Volviendo al menu principal\n")
                validar_agrear_herramienta = True

            elif(agregar_herramienta in herramientas):
                validar_agrear_herramienta = True
                print(f"{agregar_herramienta} ya está en la lista.\nVolviendo al menu principal\n")


            #CARGA DE CANTIDAD DE NUEVA HERRAMIENTA
            #Esto lo hago dentro de un if porque de lo contrario se me anidad demasiados

            if validar_agrear_herramienta == False:

                cantidad_agregar_herramienta = input("ingrese la cantidad: ")

                if (cantidad_agregar_herramienta == "0") or (int(cantidad_agregar_herramienta) < 0):
                    
                    validar_agrear_herramienta = True
                    print("Entrada invalida, no puede ser 0 ni negativo.\nVolviendo al menu principal")
                
                else:
                    cantidades.append(cantidad_agregar_herramienta)
                    herramientas.append(agregar_herramienta)
                    validar_agrear_herramienta = True














    #Actualización de Stock (Venta/Ingreso):
    # Venta: Disminuir el stock tras validar que hay unidades suficientes.
    # Ingreso: Aumentar el stock por reposición de mercadería.

    #ACTUALIZAR STOCK

    elif eleccion == "7":
        
        validar_compra_venta = True
        while validar_compra_venta:

            #MENU DE COMPRA Y VENTA
            eleccion_compra_venta = input("1) Venta (-stock)\n2) Compra (+stock)\n")

            if not eleccion_compra_venta.isdigit():
                print("Entrada invalida,  volviendo al menu principal")
                validar_compra_venta = False
            
            elif eleccion_compra_venta not in ("1", "2"):
                print("Entrada fuera de rango, volviendo al menu principal")
                validar_compra_venta = False


            #VENTA
            elif eleccion_compra_venta == "1":

                herramienta_vendida = input("herramienta vendida: ")

                if herramienta_vendida in herramientas:
                    cantidad_vendida = int(input(f"stock vendido ({herramienta_vendida}): "))


                    if cantidad_vendida <= cantidades[herramientas.index(herramienta_vendida)]:

                        cantidades[herramientas.index(herramienta_vendida)] -= cantidad_vendida
                        print(f"quedan {cantidades[herramientas.index(herramienta_vendida)]} {herramienta_vendida}")
                        break

            
            #COMPRA DE STOCK

            if eleccion_compra_venta == "2":

                herramienta_comprada = input("stock comprado: ")
                if not herramienta_comprada in herramientas:

                    print("Herramienta no cargada, volviendo al menu principal")
                
                else:
                    cantidad_stock_comprado = input("cantidad de stock adquirido: ")

                    if cantidad_stock_comprado.isdigit():

                        cantidad_stock_comprado = int(cantidad_stock_comprado)
                        cantidades[herramientas.index(herramienta_comprada)] += cantidad_stock_comprado
                        print("TEST")















print("\nRESUMEN DEL TESTEO\n")
print(herramientas)
for i in range(len(herramientas)):
    print(f"{herramientas[i]} : {cantidades[i]}")
print("FIN")