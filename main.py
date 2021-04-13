from lib.Gasolinera import Gasolinera
from lib.Camion import Camion
from lib.Cisterna import Cisterna
from lib.Auto import Auto

if __name__ == '__main__':
    santana = Auto('wolsvagen', 'yigael')
    mac = Camion('refacciones','fedex')
    santana.realizar_viaje(22)
    mac.realizar_viaje(32)
    shell = Gasolinera()
    shell.recargar_combustible_a(santana)
    premium_shell = Cisterna('shell')
    premium_shell.recargar_combustible_a(mac)