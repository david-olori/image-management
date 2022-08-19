
from tkinter import *


class Table:
    # Initialize a constructor
    def __init__(self, gui, employee_list, total_rows, total_columns):

        # An approach for creating the table
        for i in range(total_rows):
            for j in range(total_columns):

                if i ==0:
                    self.entry = Entry(gui, width=20, bg='LightSteelBlue', fg='Black',
                                       font=('Arial', 16, 'bold'))
                else:
                    self.entry = Entry(gui, width=20, fg='blue',
                               font=('Arial', 16, ''))

                self.entry.grid(row=i, column=j)
                self.entry.insert(END, employee_list[i][j])
                if(total_columns==total_columns and i>0):
                    btn_eliminar=Button(gui,text='Eliminar')
                    btn_eliminar.grid(row=i, column=j+1)

    def load_dataframe (gui, df):
        res= df.columns
        print (res)
        total_rows = len(df.index)
        total_columns = len(df.columns)

        for i in range(0,20):
            j = 0
            for column in df:

                if i == 0:
                    entry = Entry(gui, width=30, bg='LightSteelBlue', fg='Black',
                                       font=('Arial', 16, 'bold'))
                else:
                    entry = Entry(gui, width=30, fg='blue',
                                       font=('Arial', 16, ''))

                entry.grid(row=i, column=j)
                if i == 0:
                    entry.insert(END, column)
                else:
                    entry.insert(END, df.loc[i, column])
                j=j+1;

            btn_eliminar = Button(gui, text='Eliminar')
            btn_eliminar.grid(row=i, column=j )




