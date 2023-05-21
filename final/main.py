# this is the starting point of the application
import tkinter as tk
from tkinter import filedialog
from PIL import Image
from PIL import ImageTk
from PIL.ImageTk import PhotoImage
import os

# importing own modules
from model_work import run_model
from image_processing import image_processing

from marks_calculate import GetMarks, GetRollNo, GetSubject
from cornerplot import Plot
import csv
import easyocr

# modify this current path as needed
# current_path = 'C:/__Sandbox/python/university/dip/Marks D&C/final'
current_path = 'E:/University/Semester 6 - Spring 2023/Digital Image Processing/LabWork/dip_project/AI-DIP_Marks-DC/final'
os.chdir(current_path)

window = tk.Tk()

window.geometry("1000x600")
window.title("Marks Detector & Calculator")


roll_no=None
subject=None 
total_marks=None
obtained_marks=None

def add_data_to_csv():
    # Check if the file exists
    file_exists = False
    try:
        with open('scores.csv', 'r') as file:
            reader = csv.reader(file)
            if any(reader):
                file_exists = True
    except FileNotFoundError:
        print('fail')
        return
    
    print(roll_no, subject, total_marks, obtained_marks)
    # Open the CSV file in append mode
    with open('scores.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        
        # Write the header row if the file is empty
        if not file_exists:
            writer.writerow(['Roll No', 'Subject', 'Total Marks', 'Obtained Marks'])
        
        # Write the data row
        if not(roll_no and subject and total_marks and obtained_marks):
            return
        writer.writerow([roll_no, subject, sum(total_marks), sum(obtained_marks)])


# main tasks
def rest_of_tasks(filename):
    global roll_no
    global subject
    global obtained_marks
    global total_marks

    reader = easyocr.Reader(['en'])

    marks_box_path, roll_no_box_path, subject_name_path = run_model(current_path, filename)

    # reading the roll no and the subject
    roll_no = GetRollNo(roll_no_box_path, reader)
    subject = GetSubject(subject_name_path, reader)

    # we need to make individual boxes for the marks things
    image_processing(current_path, marks_box_path) 

    # reading total and obtained marks
    total_marks = []

    for i in range(10):
        marks = GetMarks(f'results/result{i+11}.png', reader)
        total_marks.extend([marks])

    obtained_marks = []
    for i in range(10):
        marks = GetMarks(f'results/result{i+21}.png', reader)
        obtained_marks.extend([marks])

    print("\n-------------------------------------")
    print('Student Roll No: '+ ''.join(roll_no))
    print('Subject Name: ' + ''.join(subject))
    print('Total Marks: ' + str(sum(total_marks)))
    print('Obtained Marks: ' + str(sum(obtained_marks)))
    print("-------------------------------------\n")


    # ADD to csv
    # add_data_to_csv(roll_no, subject, total_marks, obtained_marks)
    # moved to add to excel file button
    # displaying data in tkinter text box
    data = f"FOR CURRENT FILE: \nRoll No: {roll_no}\nSubject: {subject}\nTotal Marks: {sum(total_marks)}\nObtained Marks: {sum(obtained_marks)}\n\n"
    info_text.insert(tk.END, data)

def visualize():
    Plot()

    

# function for file upload
def upload_image():
    # Only allow JPG and PNG files
    filetypes = [("JPEG Image", "*.jpg"), ("PNG Image", "*.png")]
    filename = filedialog.askopenfilename(filetypes=filetypes)
    if filename:
        # Display selected image in the image container
        image = ImageTk.PhotoImage(Image.open(filename).resize((400, 400)))
        # canvas.itemconfig(image_item, image=image
        image_item.config(image=image)
        canvas.image_item = image
        print(filename)
        rest_of_tasks(filename)


# Create a Canvas widget
canvas = tk.Canvas(window, bg="#FFFFFF", width=1000, height=600,
                   bd=0, highlightthickness=0, relief="ridge")
canvas.place(x=0, y=0)

# getting the path to the current working directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# background image
bg_image_path = os.path.join(script_dir, 'bg_img.jpg')
background_image = ImageTk.PhotoImage(Image.open(bg_image_path))
canvas.create_image(0, 0, anchor=tk.NW, image=background_image)

canvas.create_text(200, 10, anchor="nw", text="Marks Detector & Calculator",
                   fill="#FFFFFF", font=("Times New Roman", 35))

# Create button to upload image
upload_button = tk.Button(window, text="Upload Image", command=upload_image, height=2,
                          borderwidth=5, highlightthickness=10, font=("Times New Roman", 12, "bold"), bg="#6CB4EE", fg="white")
upload_button.place(x=250, y=80, width=150, height=40)

# Create button to add to Excel file
add_to_excel_button = tk.Button(window, text="Add to Excel File", height=2, borderwidth=5, command=add_data_to_csv,
                                highlightthickness=10, font=("Times New Roman", 12, "bold"), bg="#6CB4EE", fg="white")
add_to_excel_button.place(x=680, y=80, width=150, height=40)

# gojo_image_path = os.path.join(script_dir, 'gojo.jpg')
# default_image = ImageTk.PhotoImage(Image.open(gojo_image_path).resize((550, 500)))
# image_item = canvas.create_image(100, 100, anchor="nw", image=default_image)

# Create a frame as a child of the canvas
frame0 = tk.Frame(canvas, bg='white', bd=5)
# frame.place(relx=0.5, rely=0.5, anchor='center')
# place the frame at 100,100
frame0.place(x=100, y=120, width=400, height=400)

# Load the image and create an ImageTk object
gojo_image_path = os.path.join(script_dir, 'gojo.jpg')
default_image = ImageTk.PhotoImage(Image.open(gojo_image_path).resize((400, 400)))

# Create an image item as a child of the frame
image_item = tk.Label(frame0, image=default_image)
image_item.pack()


#button
visualize_button = tk.Button(window, text="Visualize", height=2, borderwidth=5,
                             command= visualize,
                                highlightthickness=10, font=("Times New Roman", 12, "bold"), bg="#6CB4EE", fg="white")
visualize_button.place(x=450, y=540, width=150, height=40)

# Create a window inside the canvas to hold the frame
canvas.create_window(100, 120, anchor='nw', window=frame0)


# frame for the text area   
frame = tk.Frame(canvas, bg='white', bd=5)
frame.place(x=550, y=120, width=400, height=400)
# Create text area for information
info_text = tk.Text(frame, height=20, width=50)
# info_text.place(x=500, y=100, width=400, height=400)
info_text.pack()

window.mainloop()

