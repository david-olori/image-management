"""
Modulo de UnitTest para category
"""
import unittest
from src.core.normal import Normal


# Clase en la que se ejecutarán las pruebas.
class UnitTestNormal(unittest.TestCase):
    """
    Clase de UnitTest para Category
    """
    def test_create(self):
        """
        Validar creación de la categoría
        """
        category = Normal('../data/prepared')
        self.assertEqual(category.__str__(), 'Categoria: $Normal, Imagenes: 0')

    def test_load_dataframe(self):
        """
        Validar creación de la categoría
        """
        category = Normal('../data/prepared')
        category.load_dataframe()
        self.assertEqual(category.__str__(), 'Categoria: $Normal, Imagenes: 5')
