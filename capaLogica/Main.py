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
print(testItemBrie.)
