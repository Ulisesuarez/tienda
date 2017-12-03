"""def deStringADatos(matrizCasosTest):"""
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

 "   
                
def deStringADatos2(matrizCasosTest):
    for matrizDia in range(len(matrizCasosTest)):
        for listaItem in range(len(matrizCasosTest[matrizDia])):
            for atributo in range(len(matrizCasosTest[matrizDia][listaItem])):
                try:
                    matrizCasosTest[matrizDia][listaItem][atributo]= eval(matrizCasosTest[matrizDia][listaItem][atributo])
                except (SyntaxError,NameError):
                    pass

def deDatosASTring(matrizCasosTest):
    for matrizDia in range(len(matrizCasosTest)):
        for listaItem in range(len(matrizCasosTest[matrizDia])):
            for atributo in range(len(matrizCasosTest[matrizDia][listaItem])):
                
                if not isinstance(matrizCasosTest[matrizDia][listaItem][atributo],str):
                    try:
                        matrizCasosTest[matrizDia][listaItem][atributo]= str(matrizCasosTest[matrizDia][listaItem][atributo])
                    except SyntaxError:
                        pass
        
        
    