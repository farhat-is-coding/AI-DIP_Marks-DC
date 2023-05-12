import tkinter as tk
from tkinter import filedialog
from PIL import Image
from PIL import ImageTk
from PIL.ImageTk import PhotoImage
import os

window = tk.Tk()

window.geometry("1200x800")

# Define function to handle file upload
def upload_image():
    # Only allow JPG and PNG files
    filetypes = [("JPEG Image", "*.jpg"), ("PNG Image", "*.png")]
    filename = filedialog.askopenfilename(filetypes=filetypes)
    if filename:
        # Display selected image in the image container
        image = ImageTk.PhotoImage(Image.open(filename).resize((600, 600)))
        canvas.itemconfig(image_item, image=image)
        canvas.image_item = image

# Create a Canvas widget
canvas = tk.Canvas(window, bg ="#FFFFFF", width=1200, height=800, bd = 0, highlightthickness = 0, relief ="ridge")
canvas.place(x = 0, y = 0)

#getting the path to the current working directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# background image
bg_image_path = os.path.join(script_dir, 'bg_img.jpg')
background_image = ImageTk.PhotoImage(Image.open(bg_image_path))
canvas.create_image(0, 0, anchor=tk.NW, image=background_image)

canvas.create_text(300, 10, anchor="nw", text="Marks Detector & Calculator", fill="#FFFFFF", font=("Bold", 35))

# Create button to upload image
upload_button = tk.Button(window, text="Upload Image", command=upload_image, width=20, height=2, borderwidth=0,highlightthickness=0,relief="flat",font=("Inter Bold", 12), fg="white", bg= "#5072A7")
upload_button.place(x=320, y=60, width=120, height=40)

# Create button to add to Excel file
add_to_excel_button = tk.Button(window, text="Add to Excel File", width=20, height=2, font=("Bold", 12), bg= "#6CB4EE", fg="white")
add_to_excel_button.place(x=890, y=60, width=120, height=40)

gojo_image_path = os.path.join(script_dir, 'gojo.jpg')
default_image = ImageTk.PhotoImage(Image.open(gojo_image_path).resize((550, 500)))
image_item = canvas.create_image(100, 100, anchor="nw", image=default_image)

# Create text area for information
info_text = tk.Text(window, height=20, width=50)
info_text.place(x=750, y=100, width=400, height=400)

window.mainloop()
