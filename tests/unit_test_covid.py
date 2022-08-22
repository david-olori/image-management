"""
Modulo de UnitTest para category
"""
import unittest
from src.core.covid import Covid


# Clase en la que se ejecutarán las pruebas.
class UnitTestCovid(unittest.TestCase):
    """
    Clase de UnitTest para Category
    """
    def test_create(self):
        """
        Validar creación de la categoría
        """
        category = Covid('../data/prepared')
        self.assertEqual(category.__str__(), 'Categoria: $COVID, Imagenes: 0')

    def test_load_dataframe(self):
        """
        Validar creación de la categoría
        """
        category = Covid('../data/prepared')
        category.load_dataframe()
        self.assertEqual(category.__str__(), 'Categoria: $COVID, Imagenes: 5')
