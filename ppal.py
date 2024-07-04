import funciones as fn

opc = 0
listaDefinida = False
while opc != 4:
    op = fn.menu(opc)
    if op == 1:
        idJug, nombre, juego, puntaje, tipo=  fn.ingresoDatos()
        listaPuntajes = fn.agregarDatos(idJug, nombre, juego, puntaje, tipo)
        if listaPuntajes != []:
            listaDefinida = True
    elif op == 2:
        if listaDefinida:
            for n in listaPuntajes:
                print(n)
        else:
            print('No hay datos registrados')
    elif op == 3:
        escritor = fn.escribirArchivo(listaPuntajes)
    elif op == 4:
        opc = 4 
        print('Saliendo')