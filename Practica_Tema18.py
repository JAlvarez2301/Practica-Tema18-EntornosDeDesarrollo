# Importo el atributo pi de la clase math
from math import pi

# Definimos una clase
class circulo:

    # Definimos las varibles
    _radio:float

    # Constructor
    def __init__(self, radio):
        self._radio = radio

    # Método que devuelve el área del circulo
    def area(self) -> float :
        return pi * (self._radio ** 2)

    # Método que devuelve el circunferencia del circulo
    def circunferencia(self) -> float :
        return 2 * pi * self._radio