import ast
import logging
import time

"""
Módulo auxiliar para transformar los datos de 'matrizCasosTest' del módulo empresa1
Este módulo pertenece a la capa de acceso a datos del programa gestionador
de stock de la tienda de Ollivander.


Funciones:
    -Convertir strings a otro tipo de dato-> convertirStringADatos(matrizCasosTest)
    -Convertir cualquier tipo de dato a string-> convertirDatosAString(matrizCasosTest)
    


Notas:
 
El log de errores se almacena en 'Empresa1_error_log.log'

"""

def convertirStringADatos(matrizCasosTest):
    """ Toma datos en formato str y los transforma al tipo de datos que se evalua
    
    Args:
        matrizCasosTest: Lista contenedora de los datos
        

    Returns:
        None, modifica 'matrizCasosTest' para que los tipos de dato correspondan al tipo más
        significativo de dato posible, de forma que se pueda operar con él más adelante, 
        en este caso item [str,int,int]
    
    Ejecución:
        Evalua el tipo de dato de las propiedades de cada item
        Cuando el valor de las propiedades contiene letras u otros caracteres especiales que :
            No conforman un booleano
            No se encuentran integradas en una lista,diccionario o tupla
            No se encuentran en comillas anidadas ("'str'" o '"str"')
        se produce un error, y la propiedad conserva el tipo str
        
        Postcondiciones:

            ADVERTENCIA:en caso de insertar nuevas propiedades, 
            asegurarse de la correspondencia de propiedadIndice con el tipo de dato esperado
            sobre todo si se modifica el indice de las existentes

            Comprobar que la primera propiedad es tipo str
            Comprobar que la segunda y tercera propiedades son de tipo int
            En caso contrario se registra en el log de errores

    """
    
    logging.basicConfig(filename='Empresa1_error_log.log', level=logging.DEBUG)
      
    for matrizDiaIndice in range(len(matrizCasosTest)):
        for listaItemIndice in range(len(matrizCasosTest[matrizDiaIndice])):
            for propiedadIndice in range(len(matrizCasosTest[matrizDiaIndice][listaItemIndice])):
                try:
                    matrizCasosTest[matrizDiaIndice][listaItemIndice][propiedadIndice] = \
                    ast.literal_eval(\
                    matrizCasosTest[matrizDiaIndice][listaItemIndice][propiedadIndice].strip())
                except (SyntaxError, NameError, ValueError):
                    pass
                if propiedadIndice == 0:
                    try:
                        assert isinstance(matrizCasosTest[matrizDiaIndice]\
                        [listaItemIndice][propiedadIndice], str)
                    except AssertionError:
                        logging.info("En día y hora: " + time.strftime("%c"))
                        logging.info(__name__)
                        logging.info(\
                            "Función "+convertirStringADatos.__name__+" ||  atributo = "\
                            +str(matrizCasosTest[matrizDiaIndice][listaItemIndice][propiedadIndice])\
                            +" || atributo type = "\
                            +str(type(matrizCasosTest[matrizDiaIndice][listaItemIndice][propiedadIndice])))
                        logging.error("assert isinstance(matrizCasosTest[matrizDiaIndice][listaItemIndice][propiedadIndice],str) \n")

                elif propiedadIndice == 1 or propiedadIndice == 2:
                    try:
                        assert isinstance(matrizCasosTest\
                        [matrizDiaIndice][listaItemIndice][propiedadIndice], int)
                    except AssertionError:
                        logging.info("En día y hora: " + time.strftime("%c"))
                        logging.info(__name__)
                        logging.info("Función "+convertirStringADatos.__name__\
                        +" ||  atributo = "+str(matrizCasosTest\
                        [matrizDiaIndice][listaItemIndice][propiedadIndice])\
                        +" || atributo type = "+str(type(matrizCasosTest\
                        [matrizDiaIndice][listaItemIndice][propiedadIndice])))
                        logging.error("assert isinstance(matrizCasosTest[matrizDiaIndice][listaItemIndice][propiedadIndice],int) \n")

def convertirDatosAString(matrizCasosTest):
    """ Toma datos de diferentes tipos y los convierte a tipo str
    
    Args:
        matrizCasosTest: Lista contenedora de los datos
        

    Returns:
        None, modifica 'matrizCasosTest' para que los dato puedan ser escritos 
        en un fichero 
    
    Ejecución:
        Si el tipo de dato de la propiedad no es ya str, la convierte a str
        
        Postcondiciones:

            Comprobar que todas las propiedades son tipo str
            En caso contrario se registra en el log de errores
    """
    logging.basicConfig(filename='Empresa1_error_log.log', level=logging.DEBUG)
    for matrizDiaIndice in range(len(matrizCasosTest)):
        for listaItemIndice in range(len(matrizCasosTest[matrizDiaIndice])):
            for propiedadIndice in range(len(matrizCasosTest[matrizDiaIndice][listaItemIndice])):

                if not isinstance(matrizCasosTest[matrizDiaIndice][listaItemIndice][propiedadIndice], str):
                    
                        matrizCasosTest[matrizDiaIndice][listaItemIndice][propiedadIndice] = \
                        str(matrizCasosTest[matrizDiaIndice][listaItemIndice][propiedadIndice])
                    
                try:
                    assert isinstance(matrizCasosTest[matrizDiaIndice][listaItemIndice][propiedadIndice], str)
                except AssertionError:
                    logging.info("En día y hora: " + time.strftime("%c"))
                    logging.info(__name__)
                    logging.info(\
                    "Función "+convertirDatosAString.__name__\
                    +" ||  atributo = "+str(matrizCasosTest\
                    [matrizDiaIndice][listaItemIndice][propiedadIndice])\
                    +" || atributo type = "+str(type(matrizCasosTest\
                    [matrizDiaIndice][listaItemIndice][propiedadIndice])))
                    logging.error("assert isinstance(matrizCasosTest[matrizDiaIndice][listaItemIndice][propiedadIndice],str) \n")


if __name__ == "__main__":# or True :
    
    

    #Tests
    test1antes = [[["test1", "   1", " -2"]]]
    test1despues = [[["test1", 1, -2]]]

    convertirStringADatos(test1antes)
    assert test1antes == test1despues
    test2antes = [[["test2", 1, -2]]]
    test2despues = [[["test2", "1", "-2"]]]
    convertirDatosAString(test2antes)
    assert test2antes == test2despues

    #Errologtest
    convertirStringADatos([[["1", "1"]]])
    convertirStringADatos([[["error", "thats not an int"]]])

    
    
    

"""def deStringADatos(matrizCasosTest):
    for matrizDia in range(len(matrizCasosTest)):
        for listaItem in range(len(matrizCasosTest[matrizDia])):
            for atributo in range(len(matrizCasosTest[matrizDia][listaItem])):
                EsString=False
                matrizCasosTest[matrizDia][listaItem][atributo]=matrizCasosTest[matrizDia][listaItem][atributo].strip()
                for caracter in matrizCasosTest[matrizDia][listaItem][atributo]:
                    
                    if caracter.isalpha():
                        EsString=True
                if not EsString:
                    
                    if matrizCasosTest[matrizDia][listaItem][atributo].find("."):
                        try:
                            matrizCasosTest[matrizDia][listaItem][atributo]=float(matrizCasosTest[matrizDia][listaItem][atributo])
                            
                        except ValueError:
                            pass
                    if matrizCasosTest[matrizDia][listaItem][atributo].find("["):
                        try:
                            matrizCasosTest[matrizDia][listaItem][atributo]=list(matrizCasosTest[matrizDia][listaItem][atributo])
                            
                        except ValueError:
                            pass
                    
                    else:
                        try:
                            matrizCasosTest[matrizDia][listaItem][atributo]=int(matrizCasosTest[matrizDia][listaItem][atributo])
                        except ValueError:
                            pass
                
                elif matrizCasosTest[matrizDia][listaItem][atributo]=="True" or matrizCasosTest[matrizDia][listaItem][atributo]=="true" or matrizCasosTest[matrizDia][listaItem][atributo]=="TRUE":
                        matrizCasosTest[matrizDia][listaItem][atributo]=True
                elif matrizCasosTest[matrizDia][listaItem][atributo]=="False" or matrizCasosTest[matrizDia][listaItem][atributo]=="false" or matrizCasosTest[matrizDia][listaItem][atributo]=="FALSE":
                        matrizCasosTest[matrizDia][listaItem][atributo]=False

 """
    