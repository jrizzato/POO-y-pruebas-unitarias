class Cuadrado:
    def __init__(self, lado):
        pass


    @property
    def lado(self):
        """
        Getter para el atributo lado.

        Precondiciones:
            - El atributo __lado debe ser un número positivo.
            - El atributo __lado debe ser un valor numérico (int o float).

        Postcondiciones:
            - Se devuelve el valor del lado del cuadrado.
        Returns:
            float: El valor del lado del cuadrado.
        """
        return self.__lado
    
    @lado.setter
    def lado(self, nuevo_lado):
        """
        Setter para el atributo lado.

        Args:
            nuevo_lado (float): El nuevo valor del lado del cuadrado.

        Precondiciones:
            - nuevo_lado debe ser un número positivo.
            - nuevo_lado debe ser un valor numérico (int o float).

        Postcondiciones:
            - El atributo __lado se actualiza con el nuevo valor proporcionado.
            - Si el nuevo valor no cumple con las precondiciones, se lanza una excepción ValueError.
        Returns:
            None
        """
        if nuevo_lado <= 0:
            raise ValueError("ERROR: El lado debe ser positivo")
        self.__lado = nuevo_lado

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
