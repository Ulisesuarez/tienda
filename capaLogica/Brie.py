import Clase_NormalItem_Interfaz as NItem


class agedBrie(NItem.NormalItem):
    def __init__(self, name, sell_in, quality):
        NItem.NormalItem.__init__(self, name, sell_in, quality)
