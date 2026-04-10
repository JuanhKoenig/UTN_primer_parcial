
herramientas = []






#voy a empezar por el menu, despues hago las estructuras while y las restricciones

eleccion = input("1)Carga de herramientas\n2)Carga de existencias\n3)Ver inventario\n4)Consulta de stock\n5)Agotados\n6)Nuevo producto\n7)Actualizar stock (compra/venta)\n8)Salir\n")


#Carga Inicial de Herramientas: Registrar los nombres de las herramientas que se pondrán a la venta.
# Se debe preguntar al usuario la cantidad de herramientas a cargar y se debe usar una estructura pertinente. 
# En caso de nombre vacío o duplicado se debe seguir pidiendo hasta que sea correcto respetando la cantidad de herramientas 
# que el usuario indicó antes de la carga.



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

                nombre_de_herramienta = input(f"Herramienta n°{contador} de {cantidad_de_herramientas}: ")
                contador += 1
                herramientas.append(nombre_de_herramienta)


#CARGA DE HERRAMIENTAS





















#Carga de Existencias: Ingresar la cantidad de unidades para cada herramienta registrada previamente, respetando el orden de ingreso. 
#Cuando el usuario ingresa existencias, el sistema debe mostrar por pantalla el nombre de la herramienta.

#CARGA DE EXISTENCIAS















#Visualización de Inventario: Mostrar el listado completo de herramientas junto a su stock actual.

#VISUALIZACION DE INVENTARIO






















#Consulta de Stock (existencias): Buscar una herramienta por su nombre y mostrar cuántas unidades hay disponibles.


#CONSULTA DE STOCK

















#Reporte de Agotados: Listar únicamente aquellos productos cuyo stock sea igual a cero.

#REPORTA DE AGOTADOS


















#Alta de Nuevo Producto: Permitir agregar solo una nueva herramienta al final de las listas con su stock inicial. 
# En caso de nombre vacío, nombre duplicado o valor de existencia negativo se debe volver al menú principal 
# mostrando por pantalla el motivo

#ALTA DE NUEVOS PRODUCTOS

















#Actualización de Stock (Venta/Ingreso):
# o Venta: Disminuir el stock tras validar que hay unidades suficientes.
# o Ingreso: Aumentar el stock por reposición de mercadería.

#ACTUALIZAR STOCK




















print(eleccion)
print("FIN")