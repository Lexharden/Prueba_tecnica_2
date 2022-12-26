
"""Debemos incluir un método llamado 'MissingNumber' que calcule y devuelva el número faltante.
Igualmente, debemos validar la entrada de datos para asegurarnos de que el número introducido es válido y menor de 100."""

class Conjunto:
    def __init__(self):
        self.numbers = list(range(1, 101))

    def Extract(self, number):
        if number not in self.numbers:
            return "El número no está en el conjunto"
        self.numbers.remove(number)
        return "El número ha sido extraído del conjunto"

    def MissingNumber(self):
        return sum(self.numbers)


# Creamos un objeto de la clase Conjunto
conjunto = Conjunto()

# Extraemos un número del conjunto
conjunto.Extract(1)

# Calculamos el número faltante
missing_number = conjunto.MissingNumber()

# Imprimimos el número faltante
print("El número faltante es:", missing_number)
