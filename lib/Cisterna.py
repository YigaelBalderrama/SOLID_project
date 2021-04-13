from lib.Camion import Camion
from lib.Gasolinera import Gasolinera


class Cisterna(Camion, Gasolinera):

    def __init__(self, empresa):
        Camion.__init__(self, 'combustible', empresa)
        Gasolinera.__init__(self)
        Gasolinera.cantidad_maxima = 10000
        Gasolinera.cantidad_actual = 10000
        Gasolinera.valor_litro_combustible = 12
