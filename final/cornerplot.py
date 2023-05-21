# make a scatter plot of data points and calculate the standard deviation

import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import csv 
import numpy as np
import scipy.stats as stats

def getMarksFromCSV():
    obtained_marks_list = []

    # reading all obtained marks from csv file
    with open('scores.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            obtained_marks = int(row['Obtained Marks'])
            obtained_marks_list.append(obtained_marks)

    # for i in range(101-len(obtained_marks_list)):
    #     obtained_marks_list.append(0)
    return  obtained_marks_list



def Plot():
    # Generate data for x-axis (0 to 100)
    x = range(101)

    # Example marks obtained (replace with your actual data)
    marks_obtained = getMarksFromCSV()

    # Create a Tkinter window
    window = tk.Tk()
    window.title("Graph")

    # Create a Figure object and specify the size (width and height) of the graph
    figure = Figure(figsize=(6, 4), dpi=100)

    # Create a subplot within the Figure
    subplot = figure.add_subplot(111)

    data = marks_obtained

    # Calculate the standard deviation
    std_dev = np.std(data)

    # Create a plot with a horizontal line representing the standard deviation
    subplot.axhline(y=std_dev, color='red', linestyle='--', label='Standard Deviation')

    # Create a scatter plot of the data points
    subplot.scatter(range(len(data)), data, color='blue', label='Data')

    # Set labels for x-axis and y-axis
    subplot.set_xlabel('Data Points')
    subplot.set_ylabel('Values')

    # Set the plot title and legend
    subplot.set_title('Standard Deviation')
    subplot.legend()

    # Create a canvas widget for displaying the graph
    canvas = FigureCanvasTkAgg(figure, master=window) # used to display Matplotlib graph in tkinter
    canvas.draw()
    canvas.get_tk_widget().pack()

    # Start the Tkinter event loop
    window.mainloop()
