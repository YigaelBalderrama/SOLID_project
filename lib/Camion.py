from lib.Vehiculo import Vehiculo


class Camion(Vehiculo):

    def __init__(self, cargamento, empresa):
        super().__init__(567.812,567.812,160)
        self.__cargamento = cargamento
        self.__empresa = empresa

    def realizar_viaje(self, cant_km):
        Vehiculo.realizar_viaje(self, cant_km)

    def identificar_datos(self):
        Vehiculo.identificar_datos(self)
        print(f'Cargamento: {self.__cargamento}')
        print(f'Empresa: {self.__empresa}')
