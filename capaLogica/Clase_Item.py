class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

if __name__=="__main__":
        
    testItemBrie=Item("Aged Brie", 2, 0)

    assert isinstance (testItemBrie, Item) 
    assert isinstance (testItemBrie.name, str)
    assert isinstance (testItemBrie.sell_in, int)
    assert isinstance (testItemBrie.quality, int)
    assert testItemBrie.name == "Aged Brie"


    testItemElixir=Item("Elixir of the Mongoose",5,7)

    assert isinstance (testItemElixir, Item), "No es un Item"
    assert isinstance (testItemElixir.name, str), "Name no es un string"
    assert isinstance (testItemElixir.sell_in, int), "Sell_In no es integer"
    assert isinstance (testItemElixir.quality, int), "Quality no es un integer"
    assert testItemElixir.name == "Elixir of the Mongoose"
    

