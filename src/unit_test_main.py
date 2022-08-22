"""
Modulo principal para correr unit tests
"""
import unittest
from tests import unit_test_covid as cat1
from tests import unit_test_lung_opacity as cat2
from tests import unit_test_normal as cat3
from tests import unit_test_viral_pneumonia as cat4
from initializer import migrator

# Creamos un ambiente con 5 imágenes
migrator.initialize_project('../data', 5)
# *************************
# ** Pruebas de UnitTest **
# *************************
print('===================')
print('Categoría COVID:')
suite = unittest.TestLoader().loadTestsFromTestCase(cat1.UnitTestCovid)
_ = unittest.TextTestRunner().run(suite)
print('-------------------')
print('===================')
print('Categoría Lung_Opacity:')
suite = unittest.TestLoader().loadTestsFromTestCase(cat2.UnitTestLungOpacity)
_ = unittest.TextTestRunner().run(suite)
print('-------------------')
print('===================')
print('Categoría Normal:')
suite = unittest.TestLoader().loadTestsFromTestCase(cat3.UnitTestNormal)
_ = unittest.TextTestRunner().run(suite)
print('-------------------')
print('===================')
print('Categoría Viral Pneumonia:')
suite = unittest.TestLoader().loadTestsFromTestCase(cat4.UnitTestViralPneumonia)
_ = unittest.TextTestRunner().run(suite)
print('-------------------')
