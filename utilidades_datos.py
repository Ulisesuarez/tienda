import ast
def convertirDeStringADatos(matrizCasosTest):
    assert matrizCasosTest is not None
    assert isinstance(matrizCasosTest,list)
    assert matrizCasosTest!=[]
    for matrizDiaIndice in range(len(matrizCasosTest)):
        for listaItemIndice in range(len(matrizCasosTest[matrizDiaIndice])):
            for atributoIndice in range(len(matrizCasosTest[matrizDiaIndice][listaItemIndice])):
                try:
                    matrizCasosTest[matrizDiaIndice][listaItemIndice][atributoIndice]= ast.literal_eval(matrizCasosTest[matrizDiaIndice][listaItemIndice][atributoIndice].strip())
                except (SyntaxError,NameError):
                    pass
                if atributoIndice==0:
                    assert isinstance(matrizCasosTest[matrizDiaIndice][listaItemIndice][atributoIndice],str)
                else:
                    assert isinstance(matrizCasosTest[matrizDiaIndice][listaItemIndice][atributoIndice],int)
                            


def covertirDeDatosAString(matrizCasosTest):
    assert matrizCasosTest is not None
    assert isinstance(matrizCasosTest,list)
    assert matrizCasosTest!=[]
    for matrizDiaIndice in range(len(matrizCasosTest)):
        for listaItemIndice in range(len(matrizCasosTest[matrizDiaIndice])):
            for atributoIndice in range(len(matrizCasosTest[matrizDiaIndice][listaItemIndice])):
                
                if not isinstance(matrizCasosTest[matrizDiaIndice][listaItemIndice][atributoIndice],str):
                    try:
                        matrizCasosTest[matrizDiaIndice][listaItemIndice][atributoIndice]= str(matrizCasosTest[matrizDiaIndice][listaItemIndice][atributoIndice])
                    except SyntaxError:
                        pass
                assert isinstance(matrizCasosTest[matrizDiaIndice][listaItemIndice][atributoIndice],str)



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
                
        
    