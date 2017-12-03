import utilidades_datos
import logging
import os
def accesoCasosTestTxt(matrizCasosTest, rutaAccesoFichero):
    assert isinstance(matrizCasosTest,list) 
    try:
        if not isinstance(rutaAccesoFichero, str):
            
            raise ValueError
        fichero = open(rutaAccesoFichero, 'r')
    except FileNotFoundError:
        logging.error("Fichero no encontrado")
        #print("Fichero no encontrado")
        return []
    except ValueError:
        logging.error("El nombre del fichero ha de ser un string")
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
        
        utilidades_datos.convertirDeStringADatos(matrizCasosTest)
        assert len(matrizCasosTest)>0
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
    assert isinstance(matrizCasosTest,list) or isinstance(matrizCasosTest,tuple)
    try:
        if not isinstance(ficheroVolcadoCasosTest, str):
            raise ValueError
        stdout = open(ficheroVolcadoCasosTest, 'w')
    except ValueError:
            logging.error("La ruta de acceso al fichero ha de ser un string")
            #print("La ruta de acceso al fichero ha de ser un string")
    else:
        utilidades_datos.covertirDeDatosAString(matrizCasosTest)
        for (offset, casosTestDia) in enumerate(matrizCasosTest):
            stdout.write('-' * 5 + " Dia %d: " % offset + '-' * 5 + '\n')
            for item in casosTestDia:
                stdout.write(','.join(item) + '\n')
        
    assert os.path.exists(ficheroVolcadoCasosTest)
    assert os.stat(ficheroVolcadoCasosTest).st_size > 0
    stdout.close()

def mostrarCasosTest(matrizCasosTest):
    assert isinstance(matrizCasosTest,list)
    assert matrizCasosTest!=[]
    assert isinstance(matrizCasosTest[0],list)
    


    for (offset, casosTestDia) in enumerate(matrizCasosTest):
        print('-' * 5 + " Dia %d: " % offset + '-' * 5)
        for item in casosTestDia:
            print(item)


if __name__ == "__main__":
    logging.basicConfig(filename='errorlog.log',level=logging.DEBUG)
    rutaAccesoFichero = "/home/ulises/Micarpeta/proyectos/tienda/casos_tets.txt"
    # rutaAccesoFichero = "stdout_bug_conjured.gr"

    matrizCasosTest = []

    matrizCasosTest = accesoCasosTestTxt(matrizCasosTest, rutaAccesoFichero)

    mostrarCasosTest(matrizCasosTest)

    ficheroVolcadoCasosTest = "/home/ulises/Micarpeta/proyectos/tienda/stdout.txt"


    crearFicheroCasosTest(ficheroVolcadoCasosTest, matrizCasosTest)


    