class Gasolinera:

    def __init__(self):
        self.cantidad_maxima = 1000000
        self.cantidad_actual = 1000000
        self.valor_litro_combustible = 7

    def recargar_combustible_a(self, vehiculo):
        print(f'se ha llenado el tanque su cuenta es {self.valor_litro_combustible * vehiculo.litros_faltantes()} $')
        vehiculo.recargar_combustible()