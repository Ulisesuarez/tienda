import ast
import logging
import time


def convertirStringADatos(matrizCasosTest):
    
    logging.basicConfig(filename='Empresa1_error_log.log', level=logging.DEBUG)
      
    for matrizDiaIndice in range(len(matrizCasosTest)):
        for listaItemIndice in range(len(matrizCasosTest[matrizDiaIndice])):
            for atributoIndice in range(len(matrizCasosTest[matrizDiaIndice][listaItemIndice])):
                try:
                    matrizCasosTest[matrizDiaIndice][listaItemIndice][atributoIndice] = \
                    ast.literal_eval(\
                    matrizCasosTest[matrizDiaIndice][listaItemIndice][atributoIndice].strip())
                except (SyntaxError, NameError, ValueError):
                    pass
                if atributoIndice == 0:
                    try:
                        assert isinstance(matrizCasosTest[matrizDiaIndice]\
                        [listaItemIndice][atributoIndice], str)
                    except AssertionError:
                        logging.info("En día y hora: " + time.strftime("%c"))
                        logging.info(__name__)
                        logging.info(\
                            "Función "+convertirStringADatos.__name__+" ||  atributo = "\
                            +str(matrizCasosTest[matrizDiaIndice][listaItemIndice][atributoIndice])\
                            +" || atributo type = "\
                            +str(type(matrizCasosTest[matrizDiaIndice][listaItemIndice][atributoIndice])))
                        logging.error("assert isinstance(matrizCasosTest[matrizDiaIndice][listaItemIndice][atributoIndice],str) \n")

                elif atributoIndice == 1 or atributoIndice == 2:
                    try:
                        assert isinstance(matrizCasosTest\
                        [matrizDiaIndice][listaItemIndice][atributoIndice], int)
                    except AssertionError:
                        logging.info("En día y hora: " + time.strftime("%c"))
                        logging.info(__name__)
                        logging.info("Función "+convertirStringADatos.__name__\
                        +" ||  atributo = "+str(matrizCasosTest\
                        [matrizDiaIndice][listaItemIndice][atributoIndice])\
                        +" || atributo type = "+str(type(matrizCasosTest\
                        [matrizDiaIndice][listaItemIndice][atributoIndice])))
                        logging.error("assert isinstance(matrizCasosTest[matrizDiaIndice][listaItemIndice][atributoIndice],int) \n")

def convertirDatosAString(matrizCasosTest):
    logging.basicConfig(filename='Empresa1_error_log.log', level=logging.DEBUG)
    for matrizDiaIndice in range(len(matrizCasosTest)):
        for listaItemIndice in range(len(matrizCasosTest[matrizDiaIndice])):
            for atributoIndice in range(len(matrizCasosTest[matrizDiaIndice][listaItemIndice])):

                if not isinstance(matrizCasosTest[matrizDiaIndice][listaItemIndice][atributoIndice], str):
                    try:
                        matrizCasosTest[matrizDiaIndice][listaItemIndice][atributoIndice] = \
                        str(matrizCasosTest[matrizDiaIndice][listaItemIndice][atributoIndice])
                    except SyntaxError:
                        pass
                try:
                    assert isinstance(matrizCasosTest[matrizDiaIndice][listaItemIndice][atributoIndice], str)
                except AssertionError:
                    logging.info("En día y hora: " + time.strftime("%c"))
                    logging.info(__name__)
                    logging.info(\
                    "Función "+convertirDatosAString.__name__\
                    +" ||  atributo = "+str(matrizCasosTest\
                    [matrizDiaIndice][listaItemIndice][atributoIndice])\
                    +" || atributo type = "+str(type(matrizCasosTest\
                    [matrizDiaIndice][listaItemIndice][atributoIndice])))
                    logging.error("assert isinstance(matrizCasosTest[matrizDiaIndice][listaItemIndice][atributoIndice],str) \n")


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
    