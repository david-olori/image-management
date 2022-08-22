"""
Módulo para utilizar el administrador de imágenes.
"""
from src.core.covid import Covid  # Clase Covid


print('===========================')
covid_obj = Covid('../data/prepared')
print(covid_obj)
covid_obj.load_dataframe()
print(covid_obj)
covid_obj.print_dataframe()
print(covid_obj.add_image('e:/Curso/MCD/Modulo-02/ztests/perfil01.PNG'))
print(covid_obj.rename_image('perfil1', 'perfil-01'))
print(covid_obj.rename_image('perfil01', 'perfil-01'))
print(covid_obj.add_image('e:/Curso/MCD/Modulo-02/ztests/perfil01.PNG'))
print(covid_obj.rename_image('perfil01', 'perfil-02'))
print(covid_obj.delete_image('perfil-01'))
print(covid_obj)
covid_obj.print_dataframe()
print('---------------------------')
