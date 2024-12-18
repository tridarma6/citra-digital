import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def show_frame(frame):
    frame.tkraise()  

def open_image():
    global original_image_cv
    file_path = filedialog.askopenfilename(title="Select an image", filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.gif")])
    if file_path:
        original_image_cv = cv2.imread(file_path)
        display_image(original_image_cv)

def display_image(image_cv):
    # Convert from BGR to RGB format
    image_rgb = cv2.cvtColor(image_cv, cv2.COLOR_BGR2RGB)
    image_pil = Image.fromarray(image_rgb)

    # Resize image while preserving aspect ratio
    max_size = (400, 400)  # Maximum size for the image
    image_pil.thumbnail(max_size, Image.LANCZOS)
    photo = ImageTk.PhotoImage(image_pil)

    # Clear previous image if it exists
    for widget in frame2.winfo_children():
        if isinstance(widget, tk.Label) and widget != label3:
            widget.destroy()

    # Create a label to display the image
    image_label = tk.Label(frame2, image=photo)
    image_label.image = photo  # Keep a reference to avoid garbage collection
    image_label.pack(pady=10)

# Function to toggle full-screen mode
def toggle_fullscreen(event=None):
    is_fullscreen = window.attributes('-fullscreen')
    window.attributes('-fullscreen', not is_fullscreen)

def flip_vertical():
    global displayed_image_cv, is_flipped_vertical
    if original_image_cv is not None:
        if not is_flipped_vertical:  # Flip vertically
            height, width = original_image_cv.shape[:2]
            flip_vertical = np.zeros_like(original_image_cv)

            for x in range(width):
                for y in range(height):
                    flip_vertical[height - 1 - y, x] = original_image_cv[y, x]

            displayed_image_cv = flip_vertical
            is_flipped_vertical = True
        else:  # Return to original image
            displayed_image_cv = original_image_cv
            is_flipped_vertical = False

        display_image(displayed_image_cv)

def flip_horizontal():
    global displayed_image_cv, is_flipped_horizontal
    if original_image_cv is not None:
        if not is_flipped_horizontal:  # Flip horizontally
            height, width = original_image_cv.shape[:2]
            flip_horizontal = np.zeros_like(original_image_cv)

            for x in range(width):
                for y in range(height):
                    flip_horizontal[y, width - 1 - x] = original_image_cv[y, x]

            displayed_image_cv = flip_horizontal
            is_flipped_horizontal = True
        else:  # Return to original image
            displayed_image_cv = original_image_cv
            is_flipped_horizontal = False

        display_image(displayed_image_cv)

window = tk.Tk()
window.title("Photoshop Sederhana")
window.geometry("1920x1080")
window.attributes('-fullscreen', True) 
window.bind("<Escape>", toggle_fullscreen)

# Create two frames (pages)
frame1 = tk.Frame(window, bg="white")  # Frame 1 for the welcome message
frame2 = tk.Frame(window, bg="lightgrey")  # Frame 2 for the image display

for frame in (frame1, frame2):
    frame.grid(row=0, column=0, sticky='nsew')  # Use grid to stack frames with full size

window.grid_rowconfigure(0, weight=1)  # Allow the row to expand
window.grid_columnconfigure(0, weight=1)  # Allow the column to expand

# Content for Frame 1
label1 = tk.Label(frame1, text="Selamat datang di Photoshop Sederhana", font=("Arial", 16))
label1.pack(pady=20)  

label2 = tk.Label(frame1, text="Made By: ", font=("Arial", 12))
label2.pack(pady=0) 

names = [
    "Ni Luh Made Tika Kurniasari (2305551034)",
    "I Nyoman Gede Candra Wikananta (2305551065)",
    "Nyoman Tri Darma Wahyudi (2305551052)",
    "I Made Tara Bujawan (2305551139)"
]

for name in names:
    labelName = tk.Label(frame1, text=name, font=("Arial", 12))
    labelName.pack(pady=0) 

# Button to switch frames
button = tk.Button(frame1, text="Start", command=lambda: show_frame(frame2), width=10, height=2)
button.pack(pady=20)

# Content for Frame 2
label3 = tk.Label(frame2, text="Please Import an Image", font=("Arial", 16))
label3.pack(pady=20)

button_back = tk.Button(frame2, text="Go Back", command=lambda: show_frame(frame1), width=10, height=2)
button_back.pack(pady=20)

# Button to select an image
button_image = tk.Button(frame2, text="Select Image", command=open_image, width=10, height=2)
button_image.pack(pady=10)

# Buttons to flip the image
button_flip_vertical = tk.Button(frame2, text="Flip Vertical", command=flip_vertical, width=10, height=2)
button_flip_vertical.pack(pady=10)

button_flip_horizontal = tk.Button(frame2, text="Flip Horizontal", command=flip_horizontal, width=10, height=2)
button_flip_horizontal.pack(pady=10)

# Global variables to hold the original and displayed images
original_image_cv = None
displayed_image_cv = None

# Flip state tracking
is_flipped_vertical = False
is_flipped_horizontal = False

show_frame(frame1)

window.mainloop()
