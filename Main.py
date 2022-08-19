from tkinter import *
from interfaz import TableList ,ImageForm
import pandas as pd


# take the data
emp_list = [('ID', 'Name', 'City', 'Age'),
        (1, 'Gorge', 'California', 30),
       (2, 'Maria', 'New York', 19),
       (3, 'Albert', 'Berlin', 22),
       (4, 'Harry', 'Chicago', 19),
       (5, 'Vanessa', 'Boston', 31),
       (6, 'Ali', 'Karachi', 30),
        (7, 'juan', 'Bgfoston', 44),
        (8, 'Daniela', 'Chicago', 44),
        (9, 'Carlos', 'Chicago', 44)]
total_rows = len(emp_list)
total_columns = len(emp_list[0])


CSV_PATH="./data/COVID.metadata.xlsx"
df = pd.read_excel(CSV_PATH)



# create root window
master = Tk()
master.title(" Manejo de Imagenes")
main = Frame(master)
main.pack(side="bottom",fill="both",expand=False)


TableList.Table.load_dataframe(main,df)
btn_quit = Button(master, text= "Salir", command = master.destroy)
btn_quit.pack(side='left', fill="x");

#table_list = TableList.Table(main, emp_list,total_rows,total_columns)


btn_newimage = Button(master, text="Adicionar Imagen")
btn_newimage.bind("<Button>", lambda e: ImageForm.ImageForm())
btn_newimage.pack(side='left',pady=10)


master.mainloop()

#my_w.geometry("350x200")
