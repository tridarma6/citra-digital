import customtkinter as ctk
from tkinter import filedialog, Canvas
from settings import * 

class ImageImport(ctk.CTkFrame):
    def __init__(self, parent, import_func):
        super().__init__(master=parent)
        self.grid(column = 0, columnspan = 2, row = 0, sticky = 'nsew')
        self.import_func = import_func

        # title
        title_font = ctk.CTkFont(weight='bold', size=40)
        ctk.CTkLabel(self, text='Aplikasi Photo Editor Sederhana', font=title_font).pack(pady = 20)

        # app description
        for desc in APP_DESCRIPTION:
            ctk.CTkLabel(self, text=desc, height=1, justify='center').pack()
        
        ctk.CTkLabel(self, text=' ').pack(pady=10)

        # nama anggota
        ctk.CTkLabel(self, text='Made By:').pack(pady=5)
        for name in NAMES:
            ctk.CTkLabel(self, text=name, height=2).pack()
        
        ctk.CTkButton(self, text='Open Image', command=self.open_dialog).pack(expand=True)
    # cover entire window

    def open_dialog(self):
        path = filedialog.askopenfile().name
        self.import_func(path)

class ImageOutput(Canvas):
    def __init__(self, parent, resize_image):
        super().__init__(master=parent, background=BACKGROUND_COLOR, bd = 0, highlightthickness=0, relief='ridge')
        self.grid(row = 0 ,column=1, sticky='nsew', padx = 10, pady = 10)
        self.bind('<Configure>', resize_image)

class CloseOutput(ctk.CTkButton):
    def __init__(self, parent, close_func):
        super().__init__(master=parent, 
                         command=close_func,
                         text='x', 
                         text_color=WHITE, 
                         fg_color='transparent', 
                         width=40, 
                         height=40,
                         corner_radius=0,
                         hover_color=CLOSE_RED)
        self.place(relx = 0.99, rely = 0.01, anchor = 'ne')