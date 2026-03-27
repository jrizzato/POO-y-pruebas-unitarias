import math

class Piramide:
    # *** Constructor: Debe validar que base_longitud y altura sean positivos, luego asignarlos a los atributos
    def __init__(self, base_longitud, altura):
        # Escriban su código acá
        pass

    # *** Método getter base_longitud
    @property
    def base_longitud(self):
        # Escriban su código acá
        pass

    # *** Método getter altura
    @property
    def altura(self):
        # Escriban su código acá
        pass

    # *** Método setter base_longitud: Debe validar que el valor sea positivo
    @base_longitud.setter
    def base_longitud(self, nueva_base_longitud):
        # Escriban su código acá
        pass

    # *** Método setter altura: Debe validar que el valor sea positivo
    @altura.setter
    def altura(self, nueva_altura):
        # Escriban su código acá
        pass
    
    # *** Método volumen: Debe calcular (base_longitud² * altura) / 3
    def volumen(self):
        # Escriban su código acá
        pass
    
    # *** Método area_superficial: Fórmula area = base_longitud * (base_longitud + math.sqrt(4*altura² + (base_longitud/2)²))
    def area_superficial(self):
        # Escriban su código acá
        pass

