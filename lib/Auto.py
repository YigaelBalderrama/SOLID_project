from lib.Vehiculo import Vehiculo


class Auto(Vehiculo):

    def __init__(self, marca, dueno):
        super().__init__(255.5,255.5,200)
        self.__marca = marca
        self.__dueno = dueno

    def realizar_viaje(self, cant_km):

        Vehiculo.realizar_viaje(self, cant_km)

    def identificar_datos(self):
        Vehiculo.identificar_datos(self)
        print(f'Cargamento: {self.__marca}')
        print(f'Dueño: {self.__dueno}')