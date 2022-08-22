"""
Modulo de UnitTest para category
"""
import unittest
from src.core.viral_pneumonia import ViralPneumonia


# Clase en la que se ejecutarán las pruebas.
class UnitTestViralPneumonia(unittest.TestCase):
    """
    Clase de UnitTest para Category
    """
    def test_create(self):
        """
        Validar creación de la categoría
        """
        category = ViralPneumonia('../data/prepared')
        self.assertEqual(category.__str__(), 'Categoria: $Viral Pneumonia, Imagenes: 0')

    def test_load_dataframe(self):
        """
        Validar creación de la categoría
        """
        category = ViralPneumonia('../data/prepared')
        category.load_dataframe()
        self.assertEqual(category.__str__(), 'Categoria: $Viral Pneumonia, Imagenes: 5')
