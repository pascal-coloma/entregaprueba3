import csv 

def menu(opc):
    print("""
1.- Registrar puntajes torneo
2.- Listar puntajes
3.- Imprimir por Tipo
4.- Salir del programa""")
    while opc < 1 or opc > 4:
        try:
            opc = int(input('Ingrese opcion: '))
            if opc < 1 or opc > 4:
                print('Opcion invalida')
        except ValueError:
            print('Solo numeros')
    return opc

def agregarDatos(id, nombre, juego, puntaje, tipo):
    listaPuntajes = [
        ['ID Jugador', 'Nombre', 'VALORANT', 'FORTNITE', 'FIFA', 'Tipo'],
    ]
    listaDatos = [id, nombre, 0, 0, 0, '']
    listaPuntajes.append(listaDatos)
    for n in range(len(listaPuntajes[0])):
        if juego == 1:
            listaPuntajes[1][2] = puntaje
        elif juego == 2:
            listaPuntajes[1][3] = puntaje
        elif juego == 3:
            listaPuntajes[1][4] = puntaje
        if tipo == 1:
            listaDatos[-1] = 'Principante'
        elif tipo == 2:
            listaDatos[-1] = 'Avanzado'
        elif tipo == 3:
            listaDatos[-1] = 'Experto'
    
        return listaPuntajes

def ingresoDatos():
    idJugador = nombre = ''
    while idJugador == '' :
        try:
            idJugador = input('Ingrese ID: ').lower()
            if idJugador == '':
                print('No se aceptan campos vacios')
        except Exception as error:
            print('Ha ocurrido un error:', error)
    while nombre == '':
        try:
            nombre = input('Ingrese nombre: ').lower()
            if nombre == '':
                print('No se aceptan campos vacios')
        except Exception as error:
            print('Ha ocurrido un error:', error)
    print("""Seleccione un juego: 
1.- Valorant
2.- Fortnite
3.- FIFA""")
    juego = 0
    while juego < 1 or juego > 3:
        try:
            juego = int(input('Ingrese opción: '))
            if juego < 1 or juego > 3:
                print('Opcion invalida')
        except ValueError:
            print('Solo numeros')
    puntaje = -1
    while puntaje < 0:
        try:
            puntaje = int(input('Ingrese puntaje: '))
            if puntaje < 0:
                print('Solo valores positivos')
        except ValueError:
            print('Solo numeros')
    print("""Seleccione un tipo: 
1.- Principante
2.- Avanzado
3.- Experto""")
    tipo = 0
    while tipo < 1 or tipo > 3:
        try:
            tipo = int(input('Ingrese tipo [Principante, Avanzado, Experto]: '))
            if tipo < 1 or tipo > 3:
                print('Opcion invalida')
        except Exception as error:
            print('Ha ocurrido un error:', error)
    return idJugador, nombre, juego, puntaje, tipo
    
def mostrarLista(lista):
    for fila in lista:
        print(fila)
    print()
    return lista

def escribirArchivo(lista):
    with open('eShirlitos.csv', 'w', newline='') as archivo:
        escritor = csv.writer(archivo)
        for fila in lista:
            escritor.writerows(lista)
    return archivo