class Cuadrado:
    def __init__(self, lado):
        pass

    @property
    def lado(self):
        pass
    
    @lado.setter
    def lado(self, nuevo_lado):
        pass

    def area(self):
        pass
    
    def perimetro(self):
        """Calcula el perímetro del cuadrado.
        Precondiciones:
            - El atributo __lado debe ser un número positivo.
            - El atributo __lado debe ser un valor numérico (int o float).
        Postcondiciones:
            - Se devuelve el perímetro del cuadrado calculado como 4 veces el lado.
        Returns:
            float: El perímetro del cuadrado.
        """
        return 4 * self.__lado
    
if __name__ == "__main__":
    cuadrado1 = Cuadrado(5) # crea un cuadrado de lado 5
    area = cuadrado1.area()  # lado al cuadrado
    print(area)
    perimetro = cuadrado1.perimetro() # lado * 4
    print(perimetro)
    cuadrado1.lado = 10 # cambia el lado a 10 usando el setter
    largo_lado = cuadrado1.lado # muestra el largo del lado usando el getter
    print(largo_lado)
    area = cuadrado1.area() # lado al cuadrado
    print(area)
    perimetro = cuadrado1.perimetro() # lado * 4
    print(perimetro)

    try:
        cuadrado1.lado = -5 # intenta asignar un valor negativo al lado, lo que debería lanzar una excepción ValueError
    except ValueError as e:
        print(e)
