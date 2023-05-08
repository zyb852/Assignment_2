'''
This part of the code is used to explain the Python libraries that I have used to implement this task.

1. OpenCV (Open Source Computer Vision) is an open-source computer vision library that provides rich 
implementations of image processing and computer vision algorithms. It offers a series of functions 
and classes for image and video processing, and is a cross-platform library that can be used on 
different operating systems. OpenCV provides functions and tools specifically designed for image 
and video processing.

Image Reading and Display:
cv2.imread(): Used to read an image from a file.
cv2.imshow(): Used to display an image in a window.
cv2.waitKey(): Used to wait for keyboard input.

Image Saving:
cv2.imwrite(): Used to save an image to a file.

Color Space Conversion:
cv2.cvtColor(): Used to convert between different color spaces, such as from BGR to grayscale image.

2. pandas is an open-source Python library that provides efficient data structures and data analysis 
tools, making data manipulation and analysis in Python more simple and convenient. It is one of the 
most commonly used libraries in the fields of data science and data analysis.

Data Reading and Writing:
pd.read_csv(): Reads data from a CSV file and creates a DataFrame.
pd.to_csv(): Writes data from a DataFrame to a CSV file.

Data Visualization:
DataFrame.plot(): Plots the data in a DataFrame.
pd.plotting module: Provides additional plotting functions and tools, such as scatter plots, histograms, box plots, etc.
Combine with plotting libraries like Matplotlib to perform more complex data visualization operations.

The advantage of pandas library is that it provides high-performance, flexible, and easy-to-use 
data structures and data manipulation methods, making data processing, analysis, and modeling more 
efficient. It is an important tool for tasks such as data cleaning, data preprocessing, feature 
engineering, and data modeling. Whether dealing with small or large datasets, pandas provides 
convenient data manipulation and analysis capabilities, making it one of the essential tools in 
the fields of data science and data analysis.

3.NumPy (Numerical Python) is one of the most commonly used numerical computation libraries in Python. 
It provides high-performance multidimensional array objects and functions for manipulating these arrays.
NumPy is the foundation for many scientific and data analysis libraries, providing powerful numerical 
computing and vectorization capabilities.

Array Objects:
ndarray: The core data structure of NumPy, a multidimensional array object that can hold elements of 
the same data type.

Array Creation:
np.array(): Creates an array from a Python list or tuple.
The NumPy library is renowned for its efficient multidimensional array objects and rich mathematical 
functions, providing a powerful foundation for fields such as scientific computing, data analysis, 
and machine learning. Whether performing simple numerical calculations or dealing with large datasets, 
NumPy provides high performance and convenience.

The core of NumPy is the ndarray (N-dimensional array) object, which is a multidimensional array that 
can hold elements of the same data type. Since the elements of the array are stored in contiguous 
memory, NumPy can take advantage of the optimization techniques of the underlying C language to 
achieve efficient numerical calculations. Compared to Python's native list, NumPy arrays provide 
faster numerical calculations and vectorized operations, making it more efficient to handle large 
datasets.

4. Tkinter is the standard Graphical User Interface (GUI) toolkit for Python, which provides 
functionality for creating windows, controls, and implementing user interactions. It is based 
on the Tk graphical library, which can be used on multiple platforms and is easy to learn and use.

Creating a Window:
tk.Tk(): Creates a top-level window object.
window.title(): Sets the window title.
window.geometry(): Sets the window size and position.

Widgets:
Label Widget: tk.Label(), used to display text or image.
Button Widget: tk.Button(), used to trigger events or execute commands.
Input Widget: tk.Entry(), used to receive user input text.
Listbox Widget: tk.Listbox(), used to display lists or options.
Checkbox Widget: tk.Checkbutton(), used to select multiple options.
Radio Button Widget: tk.Radiobutton(), used to select a single option.
Dropdown Menu Widget: tk.OptionMenu(), used to select a single option.
Scrollbar Widget: tk.Scrollbar(), used to scroll views or lists.

Layout Managers:
pack(): Automatically layouts widgets in the order they were added.
grid(): Uses a grid-like layout to position widgets.
place(): Positions widgets based on specified coordinates and size.

Event Handling:
widget.bind(): Binds events to event handling functions.
event.widget: Gets the widget that triggered the event.
event.keysym: Gets the name of the key that was pressed.
event.x, event.y: Gets the position of the mouse click.

Dialog Boxes:
tk.messagebox.showinfo(): Shows an information dialog box.
tk.messagebox.showwarning(): Shows a warning dialog box.
tk.messagebox.showerror(): Shows an error dialog box.
tk.messagebox.askquestion(): Shows a question dialog box.
tk.messagebox.askyesno(): Shows a yes/no dialog box.

Drawing:
tk.Canvas(): Creates a canvas widget.
canvas.create_line(): Draws a line.
canvas.create_rectangle(): Draws a rectangle.
canvas.create_oval(): Draws an ellipse or circle.
canvas.create_text(): Draws text.

5. Matplotlib is a Python library for creating charts and visualizing data. It provides a rich 
set of plotting tools and features, and can create high-quality static, dynamic, and interactive 
graphics. Matplotlib can seamlessly integrate with other libraries such as NumPy and Pandas for 
convenient data manipulation and visualization. It is a commonly used plotting library in the 
fields of data science, data analysis, and machine learning, widely used for tasks such as data 
exploration, model evaluation, and result presentation.
'''

# Import the cv2 module for image processing:
import cv2

# Import the pandas module for data analysis and manipulation:
import pandas as pd
 
# Import the numpy module for numerical computation and array manipulation:
import numpy as np

# Import the tkinter module for creating GUI interfaces:
import tkinter as tk

# Import the Matplotlib library for plotting and data visualization:
import matplotlib
 
# Import the messagebox sub-module from the tkinter module for displaying message boxes:
from tkinter import messagebox

# To set Matplotlib to use the TkAgg backend for rendering graphics using the Tkinter library, 
# use the following code:
matplotlib.use('TkAgg')

# Import the pyplot module from Matplotlib library and rename it to plt for ease of use:
from matplotlib import pyplot as plt



def load_data(file_path: str) -> np.ndarray:
    
    """
    Load data from a text file and convert it to a numpy array.

    :param file_path: The path of the text file.
    :return: A numpy array containing the data in the text file.
    """
    
    # Use pandas to read the csv file with a comma delimiter and no header
    data = pd.read_csv(file_path, sep=',', header=None)
    
    # Convert the pandas DataFrame object to an array of numpy and specify the data type uint8
    return np.array(data, dtype=np.uint8)

# load data from text files
geology = load_data("geology.txt")
transport = load_data("transport.txt")
population = load_data("population.txt")


# Define a class named main win.
class main_win():
    
    # Define an initializer for this class that takes a single parameter of type tk.Tk, root, which represents the GUI window object.
    def __init__(self,root:tk.Tk):
        
        self.output_image = ""   # Recording images
        
        # Set the title of the window to "Weight Slider App".
        root.title("Weight Slider App")
        
        # Create a Matplotlib graph object called figure and set the size of the graph to 12x12 inches.
        figure = plt.figure(figsize=(12, 12))
        
        # Adds an axis object named ax to the graph at a position from (0, 0) to (1, 1).
        ax = figure.add_axes([0, 0, 1, 1])
        
        # Create a Tkinter available Matplotlib canvas object with figure as a graphical parameter and place it on the root window.
        self.canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(figure, master=root)
        
        # The Matplotlib canvas is placed on the GUI window, filling the entire window and positioned at the top.
        self.canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH)
        
        # Create three slider controls and place them on the root window. The sliders range from 0 to 1 with a step size of 0.001 and are displayed horizontally.
        self.geology_weight = tk.Scale(root, from_=0,to=1,resolution=0.01, orient=tk.HORIZONTAL, label="geology_weight")
        self.transport_weight = tk.Scale(root, from_=0, to=1, resolution=0.01, orient=tk.HORIZONTAL, label="transport_weight")
        self.population_weight = tk.Scale(root, from_=0, to=1,resolution=0.01, orient=tk.HORIZONTAL, label="population_weight")
        
        # Sets the initial value of the slider control
        self.geology_weight.set(0.33) 
        self.transport_weight.set(0.33)
        self.population_weight.set(0.34)
        
        # Create a button control called bt1 that displays the text "refresh" and calls self.refresh when the button is clicked
        # The button has a height of 2 units and a width of 20 units.
        bt1 = tk.Button(root, text="refresh",command=self.refresh,height=2, width=20)
        
        # Create a button control called bt2 that displays the text "save" and calls the self.savejpg method when the button is clicked
        # The button has a height of 2 units and a width of 20 units.
        bt2 = tk.Button(root, text="save", command=self.savejpg, height=2, width=20)
        
        
        # Layout the slider control, add the slider control to the GUI window, and fill the available space of the window using the horizontal direction.
        self.geology_weight.pack(fill=tk.X)
        self.transport_weight.pack(fill=tk.X)
        self.population_weight.pack(fill=tk.X)
        
        # Add button controls bt1,bt2 to the right side of the GUI window.
        bt1.pack(side=tk.RIGHT)
        bt2.pack(side=tk.RIGHT)

        # Create a label that displays the sum of the weights
        self.total_label = tk.Label(root, text="Total Weight: 1.000,If it is not 1, adjust it to 1 in proportion")
        self.total_label.pack()

        # Listen for slider changes and update the weight sum
        self.geology_weight.config(command=self.update_total_weight)
        self.transport_weight.configure(command=self.update_total_weight)
        self.population_weight.configure(command=self.update_total_weight)
        
        # The refresh() method is called to refresh the image and process it accordingly
        self.refresh()

    # Gets the current values of the three slider controls
    def update_total_weight(self,event):
        w1 = self.geology_weight.get()
        w2 = self.transport_weight.get()
        w3 = self.population_weight.get()

        # Calculate the sum of the weights
        total_weight = w1 + w2 + w3
       
        # If all three weight coefficients are 0, an error window pops up
        if w1 == 0 and w2 == 0 and w3 == 0:
            messagebox.showerror("error", "The limiting factor coefficients cannot all be 0")
        
    
        # If the weights do not sum to 1, update the value of the slider control to ensure that the weights do
        if total_weight != 1:
            
            # Calculate the scale
            scale = 1 / total_weight

            # Update the weight sum of the labels of the text
            text = "Total Weight: {:.3f}, Adjusted:\n".format(total_weight)
            text += "Geology Weight: {:.3f}\n".format(w1 * scale)
            text += "Transport Weight: {:.3f}\n".format(w2 * scale)
            text += "Population Weight: {:.3f}".format(w3 * scale)
            self.total_label['text']=text
            self.total_label.config(text=text)
        else:
            # Update the weight sum of the labels of the text
            self.total_label.config(text="Total Weight: {:.2f}".format(total_weight))
            
    
    def refresh(self):
        
        # Get the height and width of the Geology, Transport, and Population data
        height, width = geology.shape[0], geology.shape[1]
        
        # Create a new image based on the data weights, multiply each of the three datasets by the corresponding weights and add them together
        new_img = (self.geology_weight.get() * geology + 
                   self.transport_weight.get() * transport + 
                   self.population_weight.get() * population)
        
        '''
         The refresh function uses matrix operations to simplify the per-pixel calculation. This increases computation speed and makes the code more concise.
         
         # Create a new array of images, initialized to all zeros
         new_img = np.zeros((height, width))
         
         # Iterate over each pixel of the image
         
         for i in range(height):   
             for j in range(width):
                 
                 # Calculate the value of each pixel in the new image, according to the weight coefficient and the respective corresponding data
                 
                 new_img[i, j] = self.geology_weight.get() * geology[i, j] + self.transport_weight.get() * transport[
                     i, j] + self.population_weight.get() * population[i, j]
        '''
        
        # Get the maximum and minimum values of the new image
        max_num, min_num = np.max(new_img), np.min(new_img)
        
        # The new image is normalized to map the pixel values to the range 0-255
        normalized_new_img = (new_img - min_num) / (max_num - min_num) * 255
        
        # Converts the normalized image to an 8-bit integer type (uint8)
        suitability_evaluation = normalized_new_img.astype(np.uint8)

        # create color map for the four images
        images = {
            "Geology": geology,  # The variable geology is associated with the key "Geology", which represents the geological image data
            "Transport": transport,   # The variable transport is associated with the key "Transport", which represents the traffic image data
            "Population": population,  # The variable population is associated with the key "Population", which represents the population image data
            "Suitability Evaluation": suitability_evaluation,  # associates the variable suitability_evaluation with the key "Suitability Evaluation", which represents the suitability evaluation image data
        }
        
        # The image is transformed from grayscale to color
        colors = {
            "Geology": cv2.COLORMAP_JET,   # cv2.COLORMAP_JET is assigned to the key "Geology" to represent the color map of the geological image
            "Transport": cv2.COLORMAP_JET,  # cv2.COLORMAP_JET is assigned to the key "Transport" to represent the color map of the transportation image
            "Population": cv2.COLORMAP_JET,  # cv2.COLORMAP_JET is assigned to the key "Population" to represent the color map of the population image
            "Suitability Evaluation": cv2.COLORMAP_JET,  # cv2.COLORMAP_JET is assigned to the key "Suitability Evaluation" to indicate the color mapping of the suitability evaluation image
        }

        # Get the height and width of the input image geology.
        height, width = geology.shape[0], geology.shape[1]
        
        # Create a numpy array with the input image height times 4 and the width of the input image width times 3.
        # The data type of each pixel is an unsigned 8-bit integer, with 3 representing the RGB channel.
        result = np.zeros((height, 4 * width, 3), dtype=np.uint8)
        
        # Iterate over each title and image pair in the 'images' dictionary
        for i, (title, image) in enumerate(images.items()):
            
            # Apply the current image to the color map using the corresponding colors in the 'colors' dictionary
            color_map = cv2.applyColorMap(image, colors[title])
            
            # The color map corresponding to black pixels in the original image is set to black
            color_map[np.where(image == 0)] = [0, 0, 0]
            
            # Adds the color map to the appropriate position in the result array
            result[:, i * width:(i + 1) * width, :] = color_map
            
            # Adds title to the top-left corner of the current subimage
            cv2.putText(result, title, (i * width + 10, 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)


        self.output_image = result  # The resulting array is assigned to the jpf property of the object for later use
        plt.imshow(result)  # Use matplotlib's imshow function to display the resulting image in the current plotting window
        self.canvas.draw()  # Refresh the drawing window to display the new image
        
        # Close all OpenCV Windows
        cv2.destroyAllWindows()
        
        # Call the save_suitability_evaluation_to_txt() method to save the data to a text file
        file_path = "Suitability_evaluation.txt"
        self.save_suitability_evaluation_to_txt(suitability_evaluation, file_path)
        
    @staticmethod
    def save_suitability_evaluation_to_txt(suitability_evaluation: np.ndarray, file_path: str) -> None:
        
        # Save the suitability evaluation matrix to a text file
        with open(file_path, "w") as fp:
            
            # The suitability evaluation matrix is converted into a string and written into a text file line by line
            fp.writelines("\n".join([",".join([str(i) for i in row]) for row in suitability_evaluation]))

    '''
    This code block uses a try-except statement to catch exceptions in the block and print an error message when an exception occurs.
    except Exception as e: Specifies that all types of exceptions are caught and the exception object is stored in the variable e.
    If any of the statements in the code block raise an exception, the exception object is printed. This helps programmers quickly identify problems in their code and fix them.
    '''
    
    def savejpg(self):
        try:
            filepath = tk.filedialog.asksaveasfilename(defaultextension=".jpg")  # The file dialog box pops up to get the file path selected by the user
            cv2.imwrite(filepath, self.output_image)  # 将结果数组保存为JPEG格式的图像
            messagebox.showinfo("Info", "Image saved successfully at:\n%s" % filepath)  # 弹出消息框，提示用户保存成功，并显示文件路径
        except Exception as e:
            print(e)


if __name__ == "__main__":

    # Create a Tk object, the main window object.
    root = tk.Tk()
    
    # Create a main win object, which is the main window.
    main_win(root)
    
    # Entering the event loop
    root.mainloop()
