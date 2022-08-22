import os
import shutil
import pandas as pd
from datetime import datetime


def copy_category(df_src_path, df_dst_path, src_path, dst_path, max_rows):
    # Creamos los directorios requeridos de la categoria
    os.mkdir(dst_path)
    os.mkdir(dst_path + '/images')
    os.mkdir(dst_path + '/masks')
    df_src = pd.read_excel(df_src_path)
    # Ponemos en formato el nuevo dataframe
    df_src.rename(columns={
        'FILE NAME': 'FileName',
        'FORMAT': 'Format',
        'SIZE': 'Size',
        'URL': 'Path'
    }, inplace=True)
    # Agregamos fecha de creacion y edicion
    curr_date = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    df_src['CreateAt'] = curr_date
    df_src['UpdateAt'] = curr_date
    # Actualizamos el path
    df_src['Path'] = dst_path
    # df_dst = df_src.head(max_rows)
    df_dst = df_src.iloc[:max_rows, :]
    for i in range(len(df_dst)):
        # Preparo el nombre generico de la imagen a copiar
        file = df_dst.iloc[i]['FileName'] + '.' + df_dst.iloc[i]['Format']
        # Copiamos la imagen de .../images/
        src = src_path + '/images/' + file
        dst = dst_path + '/images/' + file
        shutil.copy2(src, dst)
        # Copiamos la imagen de .../masks/
        src = src_path + '/masks/' + file
        dst = dst_path + '/masks/' + file
        shutil.copy2(src, dst)
    # Guardamos el nuevo dataframe en un CSV
    df_dst.to_csv(df_dst_path, index=False)


def prepare_paths(bit_file, category_name, raw_path, prepared_path, max_rows):
    bit_file.write(datetime.today().strftime('%Y-%m-%d %H:%M:%S'))
    bit_file.write(': Preparando la categoria: ' + category_name + '.....\n')
    df_src_path = raw_path + '/' + category_name + '.metadata.xlsx'
    df_dst_path = prepared_path + '/' + category_name + '.metadata.csv'
    src_path = raw_path + '/' + category_name
    dst_path = prepared_path + '/' + category_name
    copy_category(df_src_path, df_dst_path, src_path, dst_path, max_rows)
    bit_file.write(datetime.today().strftime('%Y-%m-%d %H:%M:%S'))
    bit_file.write(': Preparacion de la categoria: ' + category_name + '.....Completado!\n')


def initialize_project(max_rows):
    print('Iniciando la creacion del ambiente de pruebas')
    raw_path = '../../data/raw/COVID-19_Radiography_Dataset'
    prepared_path = '../../data/prepared'
    if os.path.exists(prepared_path):
        shutil.rmtree(prepared_path)
    os.mkdir(prepared_path)

    # Creamos un archivo bitacora.txt
    file_name = datetime.today().strftime('%Y%m%d_%H%M%S') + '-bitacora.txt'
    bit_file = open(prepared_path + '/' + file_name, 'a')
    bit_file.write('Bitacora de la creacion del dataset de pruebas\n')
    bit_file.write('===============================================\n')

    # Ahora copiamos las categorias
    prepare_paths(bit_file, 'COVID', raw_path, prepared_path, max_rows)
    prepare_paths(bit_file, 'Lung_Opacity', raw_path, prepared_path, max_rows)
    prepare_paths(bit_file, 'Normal', raw_path, prepared_path, max_rows)
    prepare_paths(bit_file, 'Viral Pneumonia', raw_path, prepared_path, max_rows)

    # Cerramos la bitacora
    bit_file.write(datetime.today().strftime('%Y-%m-%d %H:%M:%S'))
    bit_file.write(': Dataset generado satisfactoriamente.\n')
    bit_file.close()
    print('La creacion del dataset de pruebas se completo')

initialize_project(7)
