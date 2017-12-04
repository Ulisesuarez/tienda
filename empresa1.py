import logging
import os
import time
import utilidades_datos
def accesoCasosTestTxt(matrizCasosTest, rutaAccesoFichero):
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
        matrizCasosTest = []
        numeroPropiedadesItem = 0
        for linea in fichero:
            if linea.find("day") != -1:
                casosTestDia = []
            elif linea == "\n":
                matrizCasosTest.append(casosTestDia)
            elif linea.find("name") != -1:
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
"""def accesoCasosTexttest primero comprueba  si el archivo existe y si el nombre es un str ,
lee linea a linea el archivo y comprueba primero la linea dia, si es una nueva linea dia crea
una lista para meter todos los items y su estado en ese dia, comprueba si se ha acabado el día 
(\n) para agregar la lista del dia a la matriz de casos test que engloba todos los dias,
se analiza la linea encabezada por name para ver el numero de atributos y dividir las otras lineas 
en esa misma cantidad de atributos (3, numeroPropiedadesItem);
Al final crea listas por cada linea de 3 elementos : como si fuera una tabla (Name, SellIn, Quality) y
añade estas a otra listea quedando una matriz con los datos de cada día."""

def crearFicheroCasosTest(ficheroVolcadoCasosTest, matrizCasosTest):
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
    assert isinstance(matrizCasosTest, list)
    assert matrizCasosTest != []
    assert isinstance(matrizCasosTest[0], list)


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
    