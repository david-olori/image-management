from tkinter import *
from tkinter.ttk import Progressbar
import os
import shutil

from tkinter.filedialog import askopenfile
import time


class ImageForm(Toplevel):

    def __init__(self, master=None,df):

        super().__init__(master=master)
        self df=df;
        self.master= master
        self.title("Upload A new Image")
        self.geometry("800x200")
        self.file_path=""
        label = Label(self, text="Image Path")
        label.pack(side='top')
        self.entry = Entry(self, width=50,  fg='Black')
        self.entry.pack(side='top')

        btn_choosefile = Button(self,text='Choose File ',
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

        shutil.copy(self.file_path.name,"./")

        for i in range(5):
            self.update_idletasks()
            pb1['value'] += 20
            time.sleep(1)
        pb1.destroy()
        lbl_message=Label(self, text='File Uploaded Successfully!', foreground='green').pack()



