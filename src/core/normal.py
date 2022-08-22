"""
Módulo que permite gestionar una determinada categoría.
"""
from src.core.category import Category  # Clase padre category


class Normal(Category):
    """
    Clase que permite gestionar el dataframe y las imágenes
    de una determinada categoría.
    """
    def __init__(self, base_path):
        super().__init__('Normal',
                         base_path + '/Normal',
                         base_path + '/Normal.metadata.csv')
