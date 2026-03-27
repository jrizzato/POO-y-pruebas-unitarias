import math

class Cilindro:
    def __init__(self, radio, altura):
        """
        Inicializa un objeto Cilindro con el radio y la altura proporcionados.
        Args:
            radio (float): El radio de la base del cilindro.
            altura (float): La altura del cilindro.
        Precondiciones:
            - radio debe ser un número positivo.
            - altura debe ser un número positivo.
        Postcondiciones:
            - Se crea un objeto Cilindro con los atributos __radio y __altura establecidos.
            - Si alguno de los valores no cumple con las precondiciones, se lanza una excepción ValueError.
        Returns:
            None
        """
        if radio <= 0 or altura <= 0:
            raise ValueError("Radio y altura deben ser positivos")
        self.__radio = radio
        self.__altura = altura

    @property
    def radio(self):
        """
        Getter para el atributo radio.

        Precondiciones:
            - El atributo __radio debe ser un número positivo.
            - El atributo __radio debe ser un valor numérico (int o float).
        Postcondiciones:
            - Se devuelve el valor del radio del cilindro.
        Returns:
            float: El valor del radio del cilindro.
        """
        return self.__radio
    
    @property
    def altura(self):
        """
        Getter para el atributo altura.

        Precondiciones:
            - El atributo __altura debe ser un número positivo.
            - El atributo __altura debe ser un valor numérico (int o float).
        Postcondiciones:
            - Se devuelve el valor de la altura del cilindro.
        Returns:
            float: El valor de la altura del cilindro.
        """

        return self.__altura
    
    @radio.setter
    def radio(self, nuevo_radio):
        """
        Setter para el atributo radio.

        Args:
            nuevo_radio (float): El nuevo valor del radio del cilindro.

        Precondiciones:
            - nuevo_radio debe ser un número positivo.
            - nuevo_radio debe ser un valor numérico (int o float).

        Postcondiciones:
            - El atributo __radio se actualiza con el nuevo valor proporcionado.
            - Si el nuevo valor no cumple con las precondiciones, se lanza una excepción ValueError.
        Returns:
            None
        """
        if nuevo_radio <= 0:
            raise ValueError("El radio debe ser positivo")
        self.__radio = nuevo_radio

    @altura.setter
    def altura(self, nueva_altura):
        """
        Setter para el atributo altura.

        Args:
            nueva_altura (float): El nuevo valor de la altura del cilindro.

        Precondiciones:
            - nueva_altura debe ser un número positivo.
            - nueva_altura debe ser un valor numérico (int o float).

        Postcondiciones:
            - El atributo __altura se actualiza con el nuevo valor proporcionado.
            - Si el nuevo valor no cumple con las precondiciones, se lanza una excepción ValueError.
        Returns:
            None
        """
        if nueva_altura <= 0:
            raise ValueError("La altura debe ser positiva")
        self.__altura = nueva_altura
    
    def calc_vol(self):
        """
        Calcula el volumen del cilindro.

        Precondiciones:
            - Los atributos __radio y __altura deben ser números positivos.
            - Los atributos __radio y __altura deben ser valores numéricos (int o float).

        Postcondiciones:
            - Se devuelve el volumen del cilindro.

        Returns:
            float: El volumen del cilindro.
        """

        return math.pi * (self.__radio ** 2) * self.__altura
    
    def area(self):
        """
        Calcula el área superficial del cilindro.

        Precondiciones:
            - Los atributos __radio y __altura deben ser números positivos.
            - Los atributos __radio y __altura deben ser valores numéricos (int o float).

        Postcondiciones:
            - Se devuelve el área superficial del cilindro.

        Returns:
            float: El área superficial del cilindro.
        """
        area = 2 * math.pi * self.__radio * (self.__radio + self.__altura)
        return area