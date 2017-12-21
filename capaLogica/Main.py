class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


testItemBrie=Item("Aged Brie", 2, 0)
testItemElixir=Item("Elixir of the Mongoose",5,7)
print(testItemElixir)
print(testItemElixir.name)
print(testItemBrie)
print(testItemBrie.quality)

class Interfaz:

    def actualizarCalidad(self):
        pass

class NormalItem(Item,Interfaz):

    def __init__(self, name, sell_in, quality):
        Item.__init__(self, name, sell_in, quality)

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

testItemElixir=NormalItem("Elixir of the Mongoose",5,7)

print(testItemElixir)
for dia in range(30):
    
    testItemElixir.setsellin()
    testItemElixir.actualizarCalidad()
    print(testItemElixir)

