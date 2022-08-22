
from tkinter import *
from ui import Pagination;


class Table:

    def __init__(self, gui, df, pagination):
        self.gui =gui
        self.df=df
        self.pagination = pagination


    def load_dataframe(self):

        k = 0;
        inicio = self.pagination.getOffsset()
        fin = self.pagination.getOffsset() + self.pagination.getPageSize()

        for i in range(inicio,fin+1):

            j = 0
            for column in self.df:

                if k == 0:
                    entry = Entry(self.gui, width=40, bg='LightSteelBlue', fg='Black',
                                  font=('Arial', 16, 'bold'))
                else:
                    entry = Label(self.gui, width=40, fg='blue', bg='white',
                                  font=('Arial', 16, ''), text=self.df.loc[i-1, column])

                entry.grid(row=k, column=j)
                if k == 0:
                    entry.insert(END, column)

                j = j+1;
            if k > 0:
                btn_eliminar = Button(self.gui, name=f"button{i}",text='Eliminar',command = lambda indicex=i-1: self.eliminar(indicex))
                btn_eliminar.grid(row=k, column=j)
            k = k + 1;

    def siguiente(self):

        for widget in self.gui.winfo_children():
            widget.destroy()
        self.pagination.getNext()
        self.load_dataframe();

    def anterior(self):

        for widget in self.gui.winfo_children():
            widget.destroy()
        self.pagination.getPrevious()
        self.load_dataframe();

    def eliminar(self,indice):
        self.df.drop([indice],inplace=True)
        self.df.reset_index(inplace=True,drop=True)
        self.load_dataframe()