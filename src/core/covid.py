"""
Módulo que permite gestionar una determinada categoría.
"""
from src.core.category import Category  # Clase padre category


class Covid(Category):
    """
    Clase que permite gestionar el dataframe y las imágenes
    de una determinada categoría.
    """
    def __init__(self, base_path):
        super().__init__('COVID',
                         base_path + '/COVID',
                         base_path + '/COVID.metadata.csv')
