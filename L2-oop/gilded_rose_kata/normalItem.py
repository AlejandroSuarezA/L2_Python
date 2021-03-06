# -*- coding: utf-8 -*-


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            # qué items hay en este if? => clases
            item.update_quality()


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


# class Interface para añadir comportamientos:
# una promesa

class Interfaz():

    def update_quality(self):
        # Comportamiento a implementar en las subclases
        pass


class NormalItem(Item, Interfaz):
    # Herencia múltiple

    def __init__(self, name, sell_in, quality):
        Item.__init__(self, name, sell_in, quality)

    def setSell_in(self):
        self.sell_in = self.sell_in - 1

    def setQuality(self, valor):
        if self.quality + valor > 50:
            self.quality = 50
        elif self.quality + valor >= 0:
            self.quality = self.quality + valor
        else:
            self.quality = 0
        assert 0 <= self.quality <= 50, "quality de %s fuera de rango" % self.__class__.__name__

    # Override metodo update_quality de la interfaz
    def update_quality(self):
        if self.sell_in > 0:
            self.setQuality(-1)
        else:
            self.setQuality(-2)
        self.setSell_in()


class Legendary(NormalItem):

    def __init__(self, name, sell_in, quality):
        NormalItem.__init__(self, name, sell_in, quality)

    # Override metodo setQuality
    def update_quality(self):
        pass


class Conjured(NormalItem):

    def __init__(self, name, sell_in, quality):
        NormalItem.__init__(self, name, sell_in, quality)

# Override metodo update_quality

    def update_quality(self):
        if self.sell_in > 0:
            self.setQuality(-2)
        else:
            self.setQuality(-4)
        self.setSell_in()


class Ticket(NormalItem):

    def __init__(self, name, sell_in, quality):
        NormalItem.__init__(self, name, sell_in, quality)

    # Override metodo update_quality
    # 10 dias o menos la quality +2, 5 dias o menos quality +3
    # dia 0 quality drop a 0

    def update_quality(self):
        if self.sell_in > 10:
            self.setQuality(+1)

        elif self.sell_in > 5:
            self.setQuality(+2)

        elif self.sell_in > 0:
            self.setQuality(+3)

        else:
            self.quality = 0
        self.setSell_in()


class Cheese(NormalItem):

    def __init__(self, name, sell_in, quality):
        NormalItem.__init__(self, name, sell_in, quality)

    # Override metodo update_quality

    def update_quality(self):
        self.setQuality(+1)
        self.setSell_in()
