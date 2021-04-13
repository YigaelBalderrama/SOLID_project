from abc import ABC, abstractmethod
from random import randrange

class Vehiculo(ABC):

    def __init__(self,c_comb,c_maxtan,c_velocidad):
        self.placa = randrange(10000, 999999)
        self.__capacidad_combustible = c_comb
        self.__capacidad_maxtanque = c_maxtan
        self.__velocidad_max = c_velocidad

    def tiempo_viaje(self, cant_km):
        return cant_km/(0.5 * self.__velocidad_max)

    @abstractmethod
    def realizar_viaje(self, cant_km):
        self.__capacidad_combustible -= (cant_km/self.__capacidad_maxtanque) * cant_km
        if self.__capacidad_combustible <= 0:
            print("el vehiculo se quedara sin combustible")
            self.__capacidad_combustible = 0
        print(f'el viaje fue realizado en {self.tiempo_viaje(cant_km)} hrs aproximadamente por el auto con placa {self.placa}')
        pass

    @abstractmethod
    def identificar_datos(self):
        print(f'placa: {self.placa}')
        pass

    def recargar_combustible(self):
        self.__capacidad_combustible = self.__capacidad_maxtanque
        print(f'El tanque del vehiculo con placa {self.placa} se ha llenado')

    def litros_faltantes(self):
        return abs(self.__capacidad_combustible - self.__capacidad_maxtanque)