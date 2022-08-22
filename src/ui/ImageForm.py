from tkinter import *
from tkinter.ttk import Progressbar
import os
import shutil
from tkinter import ttk
from tkinter.filedialog import askopenfile
import time


class ImageForm(Toplevel):
    def sel(self):
        selection = "You selected the option " + str(self.var.get())

    def __init__(self, master=None):

        super().__init__(master=master)

        self.master= master
        self.title("Upload A new Image")
        self.geometry("800x200")

        self.var = IntVar()
        rcovid = ttk.Radiobutton(self, text="Covid", variable=self.var, value=1, command=self.sel())
        rcovid.pack(side='top')

        rlungopacity = ttk.Radiobutton(self, text="Lung Opacity", variable=self.var, value=2, command=self.sel())
        rlungopacity.pack(side='top')

        rnomal = ttk.Radiobutton(self, text="Normal", variable=self.var, value=3, command=self.sel())
        rnomal.pack(side='top')

        rviral = ttk.Radiobutton(self, text="Viral Pneumonia", variable=self.var, value=4, command=self.sel())
        rviral.pack(side='top')

        self.file_path=""
        label = Label(self, text="Image Path")
        label.pack(side='top')
        self.entry = Entry(self, width=50,  fg='Black')
        self.entry.pack(side='top')


        btn_choosefile = Button(self,text='Choose File',
                                command=lambda: self.open_file()

        )
        btn_choosefile.pack(side='top')

        btn_uploadfile = Button(
            self,
            text='Upload File',
            command=self.upload_files
        )
        btn_uploadfile.pack(side='bottom')



    def open_file(self):
        self.file_path = askopenfile(mode='r', filetypes=[('Image Files', '*jpg')])
        self.entry.insert(0,self.file_path.name)
        if self.file_path is not None:
            pass

    def upload_files(self):
        pb1 = Progressbar(
            self,
            orient=HORIZONTAL,
            length=300,
            mode='determinate'
        )
        pb1.pack();

        selection = "You selected the option " + str(self.var.get())
        print(selection);

        if self.var.get() == 1:
            shutil.copy(self.file_path.name, "./data/COVID")
        elif self.var.get() == 2:
            shutil.copy(self.file_path.name, "./data/Lung_Opacity")
        elif self.var.get() == 3:
            shutil.copy(self.file_path.name, "./data/Normal")
        elif self.var.get() == 4:
            shutil.copy(self.file_path.name, "./data/Viral Pneumonia")
        else:
            print("choose am option")

        for i in range(5):
            self.update_idletasks()
            pb1['value'] += 20
            time.sleep(1)
        pb1.destroy()
        lbl_message=Label(self, text='File Uploaded Successfully!', foreground='green').pack()

