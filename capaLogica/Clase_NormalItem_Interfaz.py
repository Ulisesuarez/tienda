import Clase_Item

class Interfaz:

    def actualizarCalidad(self):
        pass

class NormalItem(Clase_Item.Item,Interfaz):

    def __init__(self, name, sell_in, quality):
        Clase_Item.Item.__init__(self, name, sell_in, quality)

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
    
    def setquality(self):
        if self.quality>50:
            self.quality=50
        if self.quality<0:
            self.quality=0

    def setsellin(self):
        self.sell_in-=1


    def actualizarCalidad(self):
        
        if self.sell_in<0:
            self.quality-=2
            
        else:
            self.quality-=1
        
        self.setquality()


if __name__=="__main__":
        
    testItemElixir=NormalItem("Elixir of the Mongoose",5,7)
    print(testItemElixir)
    for dia in range(30):
        sell_in=testItemElixir.sell_in
        testItemElixir.setsellin()
        testItemElixir.actualizarCalidad()
        assert testItemElixir.sell_in==sell_in-1, "Valor sell_in incorrecto"
        #añadir assert quality
         

