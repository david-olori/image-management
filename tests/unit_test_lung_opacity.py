"""
Modulo de UnitTest para category
"""
import unittest
from src.core.lung_opacity import LungOpacity


# Clase en la que se ejecutarán las pruebas.
class UnitTestLungOpacity(unittest.TestCase):
    """
    Clase de UnitTest para Category
    """
    def test_create(self):
        """
        Validar creación de la categoría
        """
        category = LungOpacity('../data/prepared')
        self.assertEqual(category.__str__(), 'Categoria: $Lung_Opacity, Imagenes: 0')

    def test_load_dataframe(self):
        """
        Validar creación de la categoría
        """
        category = LungOpacity('../data/prepared')
        category.load_dataframe()
        self.assertEqual(category.__str__(), 'Categoria: $Lung_Opacity, Imagenes: 5')
