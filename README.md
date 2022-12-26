
# Descripción del programa

Debemos incluir un método llamado 'MissingNumber' que calcule y devuelva el número faltante.
Igualmente, debemos validar la entrada de datos para asegurarnos de que el número introducido es válido y menor de 100.

## Uso/Ejemplos

```python
# Creamos un objeto de la clase Conjunto
conjunto = Conjunto()

# Extraemos un número del conjunto
conjunto.Extract(1)

# Calculamos el número faltante
missing_number = conjunto.MissingNumber()

# Imprimimos el número faltante
print("El número faltante es:", missing_number)
```


## Conclusión
La salida de este código sería: "El número faltante es: 5049" ya que se ha extraído el número 1 del conjunto y el método 'MissingNumber' ha calculado la suma de los números restantes (1 a 4 y 6 a 100).