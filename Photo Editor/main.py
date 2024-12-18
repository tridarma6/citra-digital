import customtkinter as ctk
import numpy as np
import cv2
from image_widgets import *
from PIL import Image, ImageTk, ImageOps, ImageEnhance, ImageFilter
from menu import Menu
from settings import *

class App(ctk.CTk):
    def __init__(self):

        #setup
        super().__init__()
        ctk.set_appearance_mode('dark')
        self.geometry('1000x600')
        self.title('Photo Editor Sederhana')
        self.minsize(800,500)
        self.init_parameters()

        # layout
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=2, uniform='a')
        self.columnconfigure(1, weight=6, uniform='a')

        # canvas data
        self.image_width = 0
        self.image_height = 0
        self.canvas_width = 0
        self.canvas_height = 0

        # widgets
        # ImportButton (Frame with button)
        
        self.image_import = ImageImport(self, self.import_image)

        # run
        self.mainloop()

    def init_parameters(self):
        self.pos_vars = {
            'rotate' : ctk.DoubleVar(value=ROTATE_DEFAULT),
            'rotateOp' : ctk.StringVar(value=ROTATE_OPTIONS),
            'zoom' : ctk.DoubleVar(value=ZOOM_DEFAULT),
            'flip' : ctk.StringVar(value=FLIP_OPTIONS[0])
        }

        self.color_vars = {
            'brightness' : ctk.DoubleVar(value=BRIGHTNESS_DEFAULT),
            'grayscale' : ctk.BooleanVar(value=GRAYSCALE_DEFAULT),
            'invert' : ctk.BooleanVar(value=INVERT_DEFAULT),
            'vibrance' : ctk.DoubleVar(value=VIBRANCE_DEFAULT),
            'red' : ctk.DoubleVar(value=RED_DEFAULT),
            'green' : ctk.DoubleVar(value=GREEN_DEFAULT),
            'blue' : ctk.DoubleVar(value=BLUE_DEFAULT),
        }

        self.effect_vars = {
            'blur' : ctk.DoubleVar(value=BLUR_DEFAULT),
            'contrast' : ctk.IntVar(value=CONTRAST_DEFAULT),
            'effect' : ctk.StringVar(value=EFFECT_OPTIONS[0]),
            'threshold' : ctk.StringVar(value=THRESHOLD_OPTIONS[0]),
            'equalize' : ctk.StringVar(value=EQUALIZE_OPTINS[0]),
            'sharpening' : ctk.StringVar(value=SHARPENING_OPTIONS[0])

        }

        # tracing
        combined_vars = list(self.pos_vars.values()) + list(self.color_vars.values()) + list(self.effect_vars.values())
        for var in combined_vars:
            var.trace('w', self.manipulate_image)

    def manipulate_image(self, *args):
        self.image = self.original

        # rotate / candra
        if self.pos_vars['rotate'].get() != ROTATE_DEFAULT:
            self.image = self.image.rotate(self.pos_vars['rotate'].get())

        # rotate options
        if self.pos_vars['rotateOp'].get() != ROTATE_OPTIONS[0]:
            if self.pos_vars['rotateOp'].get() == '90':
                self.image = self.image.rotate(90)
            if self.pos_vars['rotateOp'].get() == '-90':
                self.image = self.image.rotate(-90)
            if self.pos_vars['rotateOp'].get() == '180':
                self.image = self.image.rotate(180)

        # zoom / candra
        if self.pos_vars['zoom'].get() != ZOOM_DEFAULT:
            self.image = ImageOps.crop(image=self.image, border=self.pos_vars['zoom'].get())

        # flip / candra
        if self.pos_vars['flip'].get() != FLIP_OPTIONS[0]:
            if self.pos_vars['flip'].get() == 'Horizontal':
                self.image = ImageOps.mirror(self.image)
            if self.pos_vars['flip'].get() == 'Vertical':
                self.image = ImageOps.flip(self.image)
            if self.pos_vars['flip'].get() == 'Both':
                self.image = ImageOps.mirror(self.image)
                self.image = ImageOps.flip(self.image)

        # brightness/ tara
        if self.color_vars['brightness'].get() != BRIGHTNESS_DEFAULT:
            brightness_enhancer = ImageEnhance.Brightness(self.image)
            self.image = brightness_enhancer.enhance(self.color_vars['brightness'].get())

        #  vibrance / tika
        if self.color_vars['vibrance'].get() != VIBRANCE_DEFAULT:
            vibrance_enhancer = ImageEnhance.Color(self.image)
            self.image = vibrance_enhancer.enhance(self.color_vars['vibrance'].get())

        ## RGB // tara

        # red
        if self.color_vars['red'].get() != RED_DEFAULT:
                arr_img = np.array(self.image)
                arr_img[:, :, 0] =  np.clip(arr_img[:, :, 0] + self.color_vars['red'].get(), 0, 255)
                self.image = Image.fromarray(arr_img.astype('uint8'))

        # blue
        if self.color_vars['green'].get() != BLUE_DEFAULT:
                arr_img = np.array(self.image)
                arr_img[:, :, 1] =  np.clip(arr_img[:, :, 0] + self.color_vars['green'].get(), 0, 255)
                self.image = Image.fromarray(arr_img.astype('uint8'))

        # green
        if self.color_vars['blue'].get() != GREEN_DEFAULT:
                arr_img = np.array(self.image)
                arr_img[:, :, 2] =  np.clip(arr_img[:, :, 0] + self.color_vars['blue'].get(), 0, 255)
                self.image = Image.fromarray(arr_img.astype('uint8'))


        # grayscale &  // tri
        if self.color_vars['grayscale'].get():
            self.image = ImageOps.grayscale(self.image)

        # invert // tika
        if self.color_vars['invert'].get():
            self.image = ImageOps.invert(self.image)

        # blur / tika
        if self.effect_vars['blur'].get() != BLUR_DEFAULT:
            self.image = self.image.filter(ImageFilter.GaussianBlur(self.effect_vars['blur'].get()))

        # contrast / tika
        if self.effect_vars['contrast'].get() != CONTRAST_DEFAULT:
            self.image = self.image.filter(ImageFilter.UnsharpMask(self.effect_vars['contrast'].get()))

        # threshold // tri
        if self.effect_vars['threshold'].get() != THRESHOLD_OPTIONS[0]:
            arr_img = np.array(self.image)
            gray_image = cv2.cvtColor(arr_img, cv2.COLOR_BGR2GRAY)
            _, threshold_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)
            self.image = Image.fromarray(threshold_image.astype('uint8'))

        # equalization // candra
        if self.effect_vars['equalize'].get() != EQUALIZE_OPTINS[0]:
            arr_img = np.array(self.image)
            clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
            r, g, b = cv2.split(arr_img)
            r_clahe = clahe.apply(r)
            g_clahe = clahe.apply(g)
            b_clahe = clahe.apply(b)
            clahe_color_image = cv2.merge((r_clahe, g_clahe, b_clahe))
            self.image = Image.fromarray(clahe_color_image.astype('uint8'))

        # sharpening
        if self.effect_vars['sharpening'].get() != SHARPENING_OPTIONS[0]:
            arr_img = np.array(self.image)
            # Membuat kernel sharpening
            kernel = np.array([[0, -1, 0],
                            [-1, 5, -1],
                            [0, -1, 0]])
            
            # Melakukan filtering gambar menggunakan kernel sharpening
            sharpened_img = cv2.filter2D(arr_img, -1, kernel)
            self.image = Image.fromarray(sharpened_img.astype('uint8'))
    

        # effects
        match self.effect_vars['effect'].get():
            case 'Emboss' : self.image = self.image.filter(ImageFilter.EMBOSS) # tri
            case 'Find Edges' : self.image = self.image.filter(ImageFilter.FIND_EDGES) # tri
            case 'Contour' : self.image = self.image.filter(ImageFilter.CONTOUR)
            case 'Edge Enhance' : self.image = self.image.filter(ImageFilter.EDGE_ENHANCE) 

        self.place_image()

    def import_image(self, path):
        self.original = Image.open(path)
        self.image = self.original
        self.image_ratio=self.image.size[0] / self.image.size[1]
        self.image_tk = ImageTk.PhotoImage(self.image)

        self.image_import.grid_forget()
        self.image_output = ImageOutput(self, self.resize_image)
        self.close_button = CloseOutput(self, self.close_edit)
        self.menu = Menu(self, self.pos_vars, self.color_vars, self.effect_vars, self.export_image)

    def close_edit(self):
        self.image_output.grid_forget()
        self.close_button.place_forget()
        self.menu.grid_forget()
        self.image_import = ImageImport(self, self.import_image)

    def resize_image(self, event):

        # current canvas ratio
        canvas_ratio = event.width / event.height

        # update canvas attribute
        self.canvas_width = event.width
        self.canvas_height = event.height

        # resize
        if canvas_ratio > self.image_ratio: # canvas is wider than the image
            self.image_height = int(event.height)
            self.image_width = int(self.image_height * self.image_ratio)
        else: # canvas is taller than image
            self.image_width = int(event.width)
            self.image_height = int(self.image_width / self.image_ratio)

        self.place_image()

    def place_image(self):
        # place image
        self.image_output.delete('all')
        resized_image = self.image.resize((self.image_width, self.image_height))
        self.image_tk = ImageTk.PhotoImage(resized_image)
        self.image_output.create_image(self.canvas_width/2, self.canvas_height/2, image =  self.image_tk)

    def export_image(self, name, file, path):
        export_string = f'{path}/{name}.{file}'
        self.image.save(export_string)


App()