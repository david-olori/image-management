"""
Módulo que permite manipular la metadata de las imágenes.
"""
from datetime import datetime
import os
import shutil
import cv2


class ImageMetadata:
    """
    Clase que permite gestionar la imagen y su metadata
    """
    def __init__(self, base_path):
        self.file_name = None
        self.format = None
        self.size = None
        self.base_path = base_path
        self.img_paths = ['', '']
        self.create_at = None
        self.update_at = None

    def add_image(self, img_path, metadata):
        """
        Adiciona una imagen a partir del path, además registra en el
        dataframe, el diccionario y las carpetas correspondientes.
        :param img_path: Ruta de la imagen.
        :param metadata: Metadata de la imagen.
        :return: None
        """
        self.file_name = metadata['file_name']
        self.format = metadata['format']
        self.size = metadata['size']
        self.generate_paths()

        # Asignar fechas
        curr_date = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        self.create_at = curr_date
        self.update_at = curr_date

        print(self.img_paths[0])
        print(self.img_paths[1])
        # Abrir la imagen (0: Gray, 1: Original)
        orig_img = cv2.imread(img_path)
        # Convertir obtener una imagen en GRAY
        gray_img = cv2.cvtColor(orig_img, cv2.COLOR_BGR2GRAY)
        # Convertir obtener una imagen en BlackAndWhite
        (thresh, bw_img) = cv2.threshold(gray_img, 127, 255, cv2.THRESH_BINARY)
        # mostrar una imagen
        # cv2.imshow('Black white image', bw_img)
        # cv2.imshow('Original image', orig_img)
        # cv2.imshow('Gray image', gray_img)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        # Guardar la imagen
        cv2.imwrite(self.img_paths[0], orig_img)
        cv2.imwrite(self.img_paths[1], bw_img)

    def rename_image(self, new_name):
        """
        Renombra una imagen.
        :param new_name: Nuevo nombre de la imagen
        :return: None
        """
        old_image_path = self.img_paths[0]
        old_mask_path = self.img_paths[1]
        self.file_name = new_name
        self.generate_paths()
        shutil.move(old_image_path, self.img_paths[0])
        shutil.move(old_mask_path, self.img_paths[1])
        curr_date = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        self.update_at = curr_date

    def delete_image(self):
        """
        Elimina las imágenes de sus respectivos directorios.
        :return: None
        """
        os.remove(self.img_paths[0])
        os.remove(self.img_paths[1])

    def generate_paths(self):
        """
        Genera las rutas de sus respectivos directorios.
        :return: None
        """
        file_name = self.file_name + '.' + self.format
        self.img_paths[0] = self.base_path + '/images/' + file_name
        self.img_paths[1] = self.base_path + '/masks/' + file_name

    def as_row(self):
        """
        Retorna los atributos de la imagen como una colección.
        :return atributos (arr): Atributos de la imagen.
        """
        return [self.file_name, self.format, self.size, self.base_path,
                self.create_at, self.update_at]
