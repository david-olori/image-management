"""
Módulo que permite gestionar las categorías e imágenes
"""
import os
import cv2
import pandas as pd

from src.core.image_metadata import ImageMetadata  # Clase ImageMetadata


def retrieve_metadata(img_path):
    """
    Retorna el metadata de una ruta.
    :param img_path:  ruta de la imagen.
    :return metadata (dict): estado y message del proceso.
    """
    metadata = {'path': img_path, 'status': True, 'message': None}
    # Verificar si path existe
    if os.path.exists(img_path):
        # Verificar si es un archivo
        if os.path.isfile(img_path):
            # Asignar nombre y extension
            basename = os.path.basename(img_path)
            name_ext = os.path.splitext(basename)
            metadata['file_name'] = name_ext[0]
            metadata['format'] = name_ext[1][1:]
            # Abrir la imagen (0: Gray, 1: Original)
            orig_img = cv2.imread(img_path)
            # Obtener el alto y ancho de la imagen
            metadata['size'] = f'{orig_img.shape[0]}*{orig_img.shape[1]}'
        else:
            metadata['status'] = False
            metadata['message'] = 'La ruta no es un archivo'
    else:
        metadata['status'] = False
        metadata['message'] = 'La ruta no existe'

    return metadata


class Category:
    """
    Clase que permite gestionar el dataframe y las imágenes.
    """

    def __init__(self, name, base_path, df_path):
        self.name = name
        self.base_path = base_path
        self.df_path = df_path
        self.dataframe = None
        self.images_dict = {}

    def __str__(self):
        return f'Categoria: ${self.name}, Imagenes: {len(self.images_dict)}'

    def load_dataframe(self):
        """
        Función que carga el dataframe y un diccionario de imágenes.
        :return: None
        """
        self.dataframe = pd.read_csv(self.df_path)
        for i in range(len(self.dataframe)):
            image = ImageMetadata(self.base_path)
            image.file_name = self.dataframe.iloc[i]['FileName']
            image.format = self.dataframe.iloc[i]['Format']
            image.size = self.dataframe.iloc[i]['Size']
            image.create_at = self.dataframe.iloc[i]['CreateAt']
            image.update_at = self.dataframe.iloc[i]['UpdateAt']
            image.generate_paths()
            self.images_dict[image.file_name] = image

    def add_image(self, img_path):
        """
        Adiciona una imagen a partir del path, además registra en el
        dataframe, el diccionario y las carpetas correspondientes.
        :param img_path: Ruta de la imagen.
        :return metadata (dict): estado y message del proceso.
        """
        res = {'sts': False, 'msg': None}
        metadata = retrieve_metadata(img_path)
        if metadata['status']:
            if metadata['file_name'] in self.images_dict:
                fil_name = metadata['file_name']
                res['sts'] = False
                res['msg'] = f'La imagen({fil_name}) ya existe'
            else:
                new_image = ImageMetadata(self.base_path)
                new_image.add_image(img_path, metadata)
                self.dataframe.loc[len(self.dataframe)] = new_image.as_row()
                # Guardamos los cambios del dataframe en un CSV
                self.dataframe.to_csv(self.df_path, index=False)
                self.images_dict[new_image.file_name] = new_image
                res['sts'] = True
                res['msg'] = f'La imagen({new_image.file_name}) se añadió'
        else:
            res['sts'] = False
            res['msg'] = metadata['message']

        return res

    def rename_image(self, img_name, new_img_name):
        """
        Renombra una imagen, además actualiza el dataframe,
        el diccionario y las carpetas correspondientes.
        :param img_name: Nombre actual de la imagen.
        :param new_img_name: Nuevo nombre de la imagen.
        :return metadata (dict): estado y message del proceso.
        """
        res = {'sts': False, 'msg': None}
        if new_img_name in self.images_dict:
            res['sts'] = False
            res['msg'] = f'La imagen({new_img_name}) ya existe'

            return res
        if img_name in self.images_dict:
            img_cache = self.images_dict[img_name]
            img_cache.rename_image(new_img_name)
            self.dataframe.loc[self.dataframe['FileName'] == img_name] = img_cache.as_row()
            # Guardamos los cambios del dataframe en un CSV
            self.dataframe.to_csv(self.df_path, index=False)
            del self.images_dict[img_name]
            self.images_dict[new_img_name] = img_cache
            res['sts'] = True
            res['msg'] = f'La imagen({img_name}) se renombro a {new_img_name}'
        else:
            res['sts'] = False
            res['msg'] = f'La imagen({img_name}) no existe'

        return res

    def delete_image(self, img_name):
        """
        Elimina una imagen, además actualiza el dataframe,
        el diccionario y las carpetas correspondientes.
        :param img_name: Nombre de la imagen.
        :return metadata (dict): estado y message del proceso.
        """
        res = {'sts': False, 'msg': None}
        if img_name in self.images_dict:
            img_cache = self.images_dict[img_name]
            img_cache.delete_image()
            self.dataframe = self.dataframe.query("FileName != @img_name")
            # Guardamos los cambios del dataframe en un CSV
            self.dataframe.to_csv(self.df_path, index=False)
            del self.images_dict[img_name]
            res['sts'] = True
            res['msg'] = f'La imagen({img_name}) se elimino'
        else:
            res['sts'] = False
            res['msg'] = f'La imagen({img_name}) no existe'

        return res

    def get_images_dict(self):
        """
        Retorna el diccionario de imágenes.
        :return images_dict (dict): Diccionario de imágenes.
        """
        return self.images_dict

    def get_images_dict_keys(self):
        """
        Retorna la colección de nombres de imágenes.
        :return keys (arr): Diccionario de imágenes.
        """
        return self.images_dict.keys()

    def get_images_dict_values(self):
        """
        Retorna la colección de imágenes.
        :return values (arr): Diccionario de imágenes.
        """
        return self.images_dict.values()

    def print_dataframe(self):
        """
        Imprime el dataframe
        :return: None
        """
        print(self.dataframe)

    def print_images(self):
        """
        Imprime el diccionario de imágenes
        :return: None
        """
        print(self.images_dict)
