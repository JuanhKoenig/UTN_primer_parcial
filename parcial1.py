
herramientas = []
cantidades = []
carga_de_herramientas_inicial = False




eleccion = "0"
while not eleccion == "8":
    eleccion = input("\n1)Carga de herramientas\n2)Carga de existencias\n3)Ver inventario\n4)Consulta de stock\n5)Agotados\n6)Nuevo producto\n7)Actualizar stock (compra/venta)\n8)Salir\n")




    #CARGA DE HERRAMIENTAS
    if eleccion == "1":

        if not carga_de_herramientas_inicial:
            carga_de_herramientas_inicial = True

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
                                
                            
                            elif not nombre_de_herramienta.isalpha():
                                print("por favor solo use letras")


                            elif(nombre_de_herramienta in herramientas):
                                print(f"{nombre_de_herramienta} ya fue agregada")
                                
                            
                            else:

                                contador += 1
                                herramientas.append(nombre_de_herramienta)
                                herramienta_valida = True

        else:
            print("ya se han cargado herramientas.")








    #CARGA DE EXISTENCIAS
    elif eleccion == "2":


        if not herramientas: #este if es true si la lista esta vacia, una lista vacia es False
            print("No hay herramientas cargadas")
        
        else:
            for i in range(len(herramientas)):
                

                validacion_stock_de_herramienta = False
                while not validacion_stock_de_herramienta:

                    stock_de_herramienta = (input(f"Ingrse la cantidad de {herramientas[i]}: "))


                    if not stock_de_herramienta.isdigit():
                        print("Entrada invalida, use solo numeros\n")

                        

                    else:    
                        stock_de_herramienta = int(stock_de_herramienta)
                        cantidades.append(stock_de_herramienta)
                        validacion_stock_de_herramienta = True





    #VISUALIZACION DE INVENTARIO

    elif eleccion == "3":


        if ((len(cantidades)) == (len(herramientas)) ):
            
            print("\nINVENTARIO:\n")
            for i in range(len(herramientas)):
                print(f"{herramientas[i]} : {cantidades[i]}\n")

        else:
            print("faltan cargar herramientas y/o cantidades")




    #CONSULTA DE STOCK

    if eleccion == "4":

        if not cantidades:
            print("no hay cantidades cargadas")
            
        else:

            buscar_herramienta = input("\nBuscar: ")

            if buscar_herramienta in herramientas:
                print(f"herramienta: {buscar_herramienta}, Stock: {cantidades[herramientas.index(buscar_herramienta)]}")

            else:
                print("\nno se encontró la herramienta\n")





    #REPORTA DE AGOTADOS

    if eleccion == "5":

        if 0 in cantidades:
            print("\nAGOTADOS:\n")
            for i in range(len(cantidades)):
                if cantidades[i] == 0:
                    print(f"{herramientas[i]}")

        else:
            print("No hay stock agotados")




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

            if validar_agrear_herramienta == False:

                cantidad_agregar_herramienta = input("ingrese la cantidad: ")


                if not cantidad_agregar_herramienta.isdigit():
                    print("Entrada invalida, solo use numeros por favor")

                elif (cantidad_agregar_herramienta == "0") or (int(cantidad_agregar_herramienta) < 0):
                    
                    validar_agrear_herramienta = True
                    print("Entrada invalida, no puede ser 0 ni negativo.\nVolviendo al menu principal")
                    
                
                else:
                    cantidad_agregar_herramienta = int(cantidad_agregar_herramienta)
                    cantidades.append(cantidad_agregar_herramienta)
                    herramientas.append(agregar_herramienta)
                    validar_agrear_herramienta = True




    #ACTUALIZAR STOCK

    elif eleccion == "7":
        
        validar_compra_venta = True
        while validar_compra_venta:

            #MENU DE COMPRA Y VENTA
            eleccion_compra_venta = input("1) Venta (-stock)\n2) Compra (+stock)\n")

            #VALIDACION

            if not eleccion_compra_venta.isdigit():
                print("Entrada invalida,  volviendo al menu principal")
                validar_compra_venta = False
            
            elif eleccion_compra_venta not in ("1", "2"):
                print("Entrada fuera de rango, volviendo al menu principal")
                validar_compra_venta = False


            #VENTA
            elif eleccion_compra_venta == "1":

                herramienta_vendida = input("herramienta vendida: ")
                validar_cantidad_vendida = False

                if herramienta_vendida in herramientas:
                    cantidad_vendida = (input(f"stock vendido ({herramienta_vendida}): "))

                    if not cantidad_vendida.isdigit():
                        print("Entrada invalida, solo se permiten numeros, volviendo al menu principal")
                        validar_compra_venta = False

                    else:
                        cantidad_vendida = int(cantidad_vendida)
                        validar_cantidad_vendida = True

                
                else:
                    print("Herramienta no encontrada, volviendo al menu principal")
                    validar_compra_venta = False


                while validar_cantidad_vendida:

                    if cantidad_vendida <= int(cantidades[herramientas.index(herramienta_vendida)]):

                        (cantidades[herramientas.index(herramienta_vendida)]) -= cantidad_vendida
                        print(f"quedan {cantidades[herramientas.index(herramienta_vendida)]} {herramienta_vendida}")
                        validar_cantidad_vendida = False
                    
                    else:
                        print("Stock insuficiente, volviendo al menu principal")
                        validar_compra_venta = False
                        validar_cantidad_vendida = False
            
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