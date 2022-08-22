from tkinter import *
from ui import TableList ,ImageForm ,Pagination
import pandas as pd




CSV_PATH = "/Users/dolori-macbook/PycharmProjects/image-management/data/raw/COVID.metadata.xlsx"
df = pd.read_excel(CSV_PATH)

v_offsset = 0;
# create root window
master = Tk()
master.title("Manejo de Imagenes")
main = Frame(master)

pagi= Pagination.Pagination(0,25)
table_df = TableList.Table(main,df,pagi);
table_df.load_dataframe()
main.pack(side="bottom",fill="both",expand=False)
botton_Frame = Frame(master)
botton_Frame.pack(side="right",fill="x",expand=False)

btn_previuous = Button(botton_Frame, text=" << Anterior")
btn_previuous.bind("<Button>", lambda e: table_df.anterior())
btn_previuous.pack(side='left',pady=10)

btn_next = Button(botton_Frame, text="Siguiente >> ")
btn_next.bind("<Button>", lambda e: table_df.siguiente())
btn_next.pack(side='right',pady=10)

btn_quit = Button(master, text= "Salir", command= master.destroy)
btn_quit.pack(side='left', fill="x");

btn_newimage = Button(master, text="Adicionar Imagen")
btn_newimage.bind("<Button>", lambda e: ImageForm.ImageForm())
btn_newimage.pack(side='left',pady=10)

master.mainloop()


#my_w.geometry("350x200")
