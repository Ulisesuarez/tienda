"""
Este modulo pertenece a la capa de acceso a datos del programa gestionador
de stock de la tienda de Ollivander.


Funciones:
    -Obtener los datos de stock de un fichero en memoria
    almacenandolos en la variable 'matrizCasosTest' -> accesoCasosTestTxt(matrizCasosTest, rutaAccesoFichero)
    -Volcar los datos en memoria a un fichero-> crearFicheroCasosTest(ficheroVolcadoCasosTest, matrizCasosTest)
    -Mostrar datos del stock por pantalla->mostrarCasosTest(matrizCasosTest)


Notas:

Tiene un modulo auxiliar para transformar los datos de 'matrizCasosTest'
El log de errores se almacena en 'Empresa1_error_log.log'

"""

import logging
import os
import time
import utilidades_datos
def accesoCasosTestTxt(matrizCasosTest, rutaAccesoFichero, inicioListaFlag=None, finListaFlag=None,numeroPropiedadesFlag=None):
    """ Toma datos de un fichero y los vuelca en memoria
    
    Args:
        matrizCasosTest: Lista vacía donde se almacenarán los datos
        rutaAccesoFichero: Path del fichero fuente de los datos
        inicioListaFlag: string utilizada para detectar el inicio de las listas anidadas 'casosTestDia'
        finListaFlag: string utilizada para detectar el final de las listas anidadas 'casosTestDia'
        numeroPropiedadesFlag: string utilizada para detectar el numero de propiedades de cada 'item'

    Returns:
        matrizCasosTest: Lista contenedora de los datos que hay en el fichero
        transformados a los tipos de dato que corresponda, en este caso para cada
        item [str,int,int]
    
    Ejecución:
        Precondiciones:
            Comprobar si 'matrizCasosTest' es una lista
            Comprobar si 'rutaAccesoFicheros' es un str
            Si existe 'rutaAccesoFicheros', abrir 'fichero'
            Si alguna de estas acciones no dá el resultado esperado se registra el error en un log
        Se lee el fichero linea por linea (siguiendo el formato del fichero usado hasta el momento ('casos_tets.txt')):
            La línea que contiene 'inicioListaFlag' indica el principio de una lista anidadad, 'casosTestDia'
            Usamos la línea encabezada por 'numeroAtributosFlag' para obtener el numero de propiedades de cada item 
            Transformamos la linea en una lista  con len='numeroPropiedadesItem'
            Añadimos la lista 'item' a la lista 'casosTestDia'
            La línea == finListaFlag: indica el final de 'casosTestDia', añadimos la lista a 'matrizCasosTest'
            y si la hay pasamos a la siguiente lista 'casosTestDia'
        Una vez recorrido el fichero transformamos los tipos de cada propiedad invocando 
        'convertirStringADatos' del modulo 'utilidades_datos'
        Postcondiciones:
            Comprobar que 'matrizcasosTest' no está vacía
            En caso contrario se registra en el log de errores

    """
    try:
        assert isinstance(matrizCasosTest, list)
    except AssertionError:
        logging.info("En día y hora: " + time.strftime("%c"))
        logging.info(__name__)
        logging.info("Función "+accesoCasosTestTxt.__name__+" ||  matrizCasosTest = "+str(matrizCasosTest)+" || matrizCasosTest type = "+str(type(matrizCasosTest)))
        logging.error("assert isinstance(matrizCasosTest,list) \n")
        
    try:
        if not isinstance(rutaAccesoFichero, str):
            raise ValueError
        fichero = open(rutaAccesoFichero, 'r')
    except FileNotFoundError:
        logging.info("En día y hora: " + time.strftime("%c"))
        logging.info(__name__)
        logging.info("Función "+accesoCasosTestTxt.__name__+" || rutaAccesoFichero = "+rutaAccesoFichero)
        logging.error(" Fichero no encontrado \n")
        #print("Fichero no encontrado")
        return []
    except ValueError:
        logging.info("En día y hora: " + time.strftime("%c"))
        logging.info(__name__)
        logging.info("Función "+accesoCasosTestTxt.__name__+" || rutaAccesoFichero = "+ str(rutaAccesoFichero) +" || tipo de dato rutaAccesoFichero = "+str(type(rutaAccesoFichero)))
        logging.error("El nombre del fichero ha de ser un string \n")
        #print("El nombre del fichero ha de ser un string")
        return []
    else:
        if inicioListaFlag is None:
            inicioListaFlag="day"
        if finListaFlag is None:
            finListaFlag="\n"
        if numeroPropiedadesFlag is None:
            numeroPropiedadesFlag="name"
        matrizCasosTest = []
        numeroPropiedadesItem = 0
        for linea in fichero:
            if linea.find(inicioListaFlag) != -1:
                casosTestDia = []
            elif linea == finListaFlag :
                matrizCasosTest.append(casosTestDia)
            elif linea.find(numeroPropiedadesFlag) != -1:
                numeroPropiedadesItem = len(linea.split(','))
            else:
                item = linea.rstrip().rsplit(',', maxsplit=numeroPropiedadesItem - 1)
                casosTestDia.append(item)
        fichero.close()
        utilidades_datos.convertirStringADatos(matrizCasosTest)
        try:
            assert len(matrizCasosTest) > 0
        except AssertionError:
            logging.info("En día y hora: " + time.strftime("%c"))
            logging.info(__name__)
            logging.info("Función "+accesoCasosTestTxt.__name__+" ||  matrizCasosTest = "+str(matrizCasosTest)+" || matrizCasosTest len = "+len(matrizCasosTest))
            logging.error("assert len(matrizCasosTest)>0 \n")
        return matrizCasosTest


def crearFicheroCasosTest(ficheroVolcadoCasosTest, matrizCasosTest):
    """ Toma datos de una variable y los vuelca en un fichero
    
    Args:
        ficheroVolcadoCasosTest: Path del fichero donde se volcarán los datos
        matrizCasosTest: Lista contenedora de los datos

    Returns:
        None, crea el fichero 'stoudt.txt'
    
    Ejecución:
        Precondiciones:
            Comprobar si 'matrizCasosTest' es una lista
            Comprueba que 'matrizCasosTest' no está vacía y que la primera lista 
            anidada tampoco está vacía
            Comprobar si 'ficheroVolcadoCasosTest' es un str
            Si alguna de estas acciones no dá el resultado esperado se registra el error en un log
        Transformamos los tipos de cada propiedad  a str invocando 
        'convertirDatosAString' del modulo 'utilidades_datos'
        Se escribe el fichero linea por linea :
            Utilizamos el indice de 'CasoTestDia' dentro de 'matrizCasosTest' para escribir un
            encabezado con el numero de día
            Escribimos todos los items que hay en ese día
            Si lo hay pasamos al siguiente día
        
        Postcondiciones:
            Una vez recorrida 'matrizCasosTest', 
            Comprobar que el fichero 'ficheroVolcadoCasosTest' ('stoudt.txt') ha sido creado
            y que no está vacío.
            En caso contrario se registra en el log de errores

    """
    try:
        assert isinstance(matrizCasosTest, list)
    except AssertionError:
        logging.info("En día y hora: " + time.strftime("%c"))
        logging.info(__name__)
        logging.info("Función "+crearFicheroCasosTest.__name__+" ||  matrizCasosTest = "+str(matrizCasosTest)+" || matrizCasosTest type = "+str(type(matrizCasosTest)))
        logging.error("assert isinstance(matrizCasosTest, list) \n")
    try:
        assert len(matrizCasosTest[0]) > 0

    except (AssertionError,IndexError):
        logging.info("En día y hora: " + time.strftime("%c"))
        logging.info(__name__)
        logging.info("Función "+crearFicheroCasosTest.__name__+" ||  matrizCasosTest = "+str(matrizCasosTest))
        logging.error("assert len(matrizCasosTest[0])>0 \n")

    try:
        if not isinstance(ficheroVolcadoCasosTest, str):
            raise ValueError
        stdout = open(ficheroVolcadoCasosTest, 'w')
    except ValueError:
        logging.info("En día y hora: " + time.strftime("%c"))
        logging.info(__name__)
        logging.info("Función "+crearFicheroCasosTest.__name__+" || ficheroVolcadoCasosTest = "+ str(ficheroVolcadoCasosTest) +" || tipo de dato ficheroVolcadoCasosTest = "+str(type(ficheroVolcadoCasosTest)))
        logging.error("La ruta de acceso al fichero ha de ser un string \n")
            #print("La ruta de acceso al fichero ha de ser un string")
    else:
        utilidades_datos.convertirDatosAString(matrizCasosTest)
        for (offset, casosTestDia) in enumerate(matrizCasosTest):
            stdout.write('-' * 5 + " Dia %d: " % offset + '-' * 5 + '\n')
            for item in casosTestDia:
                stdout.write(','.join(item) + '\n')
        try:
            assert os.path.exists(ficheroVolcadoCasosTest)
        except AssertionError:
            logging.info("En día y hora: " + time.strftime("%c"))
            logging.info(__name__)
            logging.info("Función "+accesoCasosTestTxt.__name__+" || ficheroVolacadoCasosTest="+ficheroVolcadoCasosTest)
            logging.error("assert os.path.exists(ficheroVolcadoCasosTest) \n")
        try:
            assert os.stat(ficheroVolcadoCasosTest).st_size > 0
        except AssertionError:
            logging.info("En día y hora: " + time.strftime("%c"))
            logging.info(__name__)
            logging.info("Función "+accesoCasosTestTxt.__name__ +" || ficheroVolcadoCasosTest = Empty File")
            logging.error("assert os.stat(ficheroVolcadoCasosTest).st_size > 0 \n")
        
        stdout.close()

def mostrarCasosTest(matrizCasosTest):
    """ Toma datos de una variable y los muestra en pantalla
    
    Args:
        matrizCasosTest: Lista contenedora de los datos

    Returns:
        None, muestra los datos en pantalla
    
    Ejecución:
        Precondiciones:
            Comprobar si 'matrizCasosTest' es una lista y que no está vacía
            Comprueba  que el primer elemento es una lista anidada y que no está vacía
        Muestra los datos de 'matrizCasosTest' siguiendo el mismo formato que
        los escritos en 'crearFicheroCasosTest':
            encabezado con numero de día (offset de casosTestDia) y items de ese día
    """    
    assert isinstance(matrizCasosTest, list)
    assert matrizCasosTest != []
    assert isinstance(matrizCasosTest[0], list)
    assert matrizCasosTest[0] != []
    


    for (offset, casosTestDia) in enumerate(matrizCasosTest):
        print('-' * 5 + " Dia %d: " % offset + '-' * 5)
        for item in casosTestDia:
            print(item)


if __name__ == "__main__":
    logging.basicConfig(filename='Empresa1_error_log.log', level=logging.DEBUG)
    
    trutaAccesoFichero = "/home/ulises/Micarpeta/proyectos/tienda/casos_tets.txt"
    # rutaAccesoFichero = "stdout_bug_conjured.gr"

    tmatrizCasosTest = []

    tmatrizCasosTest = accesoCasosTestTxt(tmatrizCasosTest, trutaAccesoFichero)

    mostrarCasosTest(tmatrizCasosTest)

    tficheroVolcadoCasosTest = "/home/ulises/Micarpeta/proyectos/tienda/stdout.txt"


    crearFicheroCasosTest(tficheroVolcadoCasosTest, tmatrizCasosTest)

    #errorlog test
    accesoCasosTestTxt(9,"k")
    accesoCasosTestTxt([], 87)
    accesoCasosTestTxt([], "289")
    crearFicheroCasosTest([], [])
    #errolog test modulo utilidades
    utilidades_datos.convertirStringADatos([[["1", "1"]]])
    utilidades_datos.convertirStringADatos([[["error", "thats not an int"]]])
    