'''
In this section, I will introduce the libraries used in the unit_test test code (and the duplicated libraries in main are not covered).

1. unittest is a testing framework in the Python standard library for writing and running unit tests. It provides a set of tools to help 
developers write test cases, run test cases, and generate test reports.By using unittest, we can verify the correctness of the program after 
the code is modified, and improve the quality and maintainability of the code.

unittest supports organizing, running, and refactoring test cases. Developers can use it to write test cases and organize them into test suites. 
A test suite can contain multiple test cases, which can be run in order or in random order. unittest also provides a series of assertion methods 
for verifying the expected behavior of programs. If a test case fails, unittest provides detailed error information so that developers can quickly 
identify the problem.

unittest also supports automatic discovery and execution of tests, making it easy to run all test cases or only specified ones. In addition, 
unittest provides a rich set of plugins and extension mechanisms, which can be customized to meet specific testing needs as required.

2. The os library is a module in the Python standard library that provides many functions for interacting with the operating system, including 
file and directory operations, process management, and system calls. Using the os library, it is easy to manipulate the file system in Python, 
including creating, deleting, renaming, copying, moving, and traversing directories. In addition, the os library provides many functions related 
to processes, such as starting new processes, killing processes, and retrieving process IDs.

The os library contains many useful functions, such as:

os.getcwd(): Get the current working directory
os.chdir(path): Change the current working directory
os.listdir(path): Get a list of all files and subdirectories in the specified directory
os.mkdir(path): Create a new directory
os.rmdir(path): Remove a directory
os.rename(src, dst): Rename a file or directory
os.remove(path): Remove a file
os.path.exists(path): Check if a path exists
os.path.isfile(path): Check if a path is a file
os.path.isdir(path): Check if a path is a directory
By using the os library, file and directory operations can be easily performed in Python, and interactions with the operating system can be made. 
The os library is a very commonly used module in the Python standard library, and is a useful tool for applications that need to interact with the 
file system or processes.

3. The unittest.mock module from the Python standard library imports two functions, MagicMock and patch, that are used as tools for mocking and 
replacing code during testing.

MagicMock is a Python class that is used to mimic the behavior of Python objects and classes. In testing, MagicMock can be used to mock and replace 
certain objects or classes in the code being tested, in order to better control the testing environment and behavior.

patch is a decorator in the unittest.mock module that is used to replace certain objects or classes in the code being tested, in order to better 
control the testing environment and behavior. By using the patch function, difficult-to-control external dependencies such as network connections 
and file system operations can be replaced during testing, in order to better control the testing results.

In testing, Mock and patch are often used in conjunction with each other. By using Mock and patch, the testing code can better isolate the code 
being tested from external dependencies, and better control the testing environment and behavior, thereby improving the accuracy and reliability 
of the testing results.

'''

import os
import unittest
import cv2
import numpy as np
from unittest.mock import MagicMock, patch
import tkinter as tk
import main  

class MockTkinter:
    def __enter__(self):
        # When entering the context manager, mock the asksaveasfilename and showinfo methods in the tkinter module
        self.patchers = [
            patch('main.tk.filedialog.asksaveasfilename', return_value="test_image.jpg"),  # Use the patch method to mock asksaveasfilename and return a test image filename
            patch('main.messagebox.showinfo')  # mock showinfo with the patch method
        ]
        [patcher.start() for patcher in self.patchers]  # Starting a mock object
        return self  # Returns the context manager object

    def __exit__(self, exc_type, exc_value, traceback):
        [patcher.stop() for patcher in self.patchers]  # Stop the mock object when you exit the context manager

def mock_tkinter():
    # Use MagicMock to create mock objects that simulate the various methods and properties of the tkinter module
    main.tk.Tk = MagicMock()  # Simulate the Tk class
    main.tk.Label = MagicMock()  # Simulate the Label class
    main.tk.Scale = MagicMock()  # Simulate the Scale class
    main.tk.Button = MagicMock()  # Simulate the Button class
    main.tk.mainloop = MagicMock()  # Simulate the mainloop method
    main.tk.messagebox.showerror = MagicMock()  # Simulate the showerror method
    main.tk.messagebox.showinfo = MagicMock()  # Simulate the showinfo method
    main.tk.filedialog.asksaveasfilename = MagicMock()  # 模拟asksaveasfilename方法
    
class TestWeightSliderApp(unittest.TestCase):

    # Test whether the load_data function loads the data from the file correctly.
    def test_load_data(self):
        test_file_path = "test_data.txt"   # Create a path to the test file.
        with open(test_file_path, "w") as f:   # Open the file in "w" mode and write the test data.
            f.write("0,0,0\n0,1,0\n0,0,0")   # Write the test data to a file.
        
        expected_data = np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]], dtype=np.uint8)   # Create a NumPy array with the expected data.
        actual_data = main.load_data(test_file_path)   # The load_data function is called to read the test file and get the actual data.
        # Use the np.testing.assert_array_equal function to compare the expected and actual values and raise an exception if they don't match.
        np.testing.assert_array_equal(expected_data, actual_data, "Loaded data should match expected data")

    def test_save_suitability_evaluation_to_txt(self):
        data = np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]], dtype=np.uint8)    # Create a NumPy array containing the suitability assessment data
        test_suitability_path = "test_suitability.txt"   # Create a path to the test suitability file
        # Save the suitability evaluation data to the specified text file using the save_suitability_evaluation_to_txt method
        main.main_win.save_suitability_evaluation_to_txt(data, test_suitability_path)   

        # Open the saved suitability file and read its contents
        with open(test_suitability_path, "r") as f:
            content = f.read()

        # Define the string form of the intended suitability data
        expected_content = "0,0,0\n0,1,0\n0,0,0"
        # Use the self.assertEqual method to compare the contents of the file to what you expect
        self.assertEqual(content, expected_content, "Content of the suitability evaluation file should match the expected content")


    def test_savejpg(self):
        def test_savejpg(self):
         with MockTkinter():   # Use the MockTkinter context manager to simulate the behavior of the functions in the tkinter library
             root = tk.Tk()     # Create a tkinter window
             main_window = main.main_win(root)   # Create the main window object on the tkinter window
    
             test_image_path = "test_image.jpg"   # Create a test file path to save the image 
    
             main_window.savejpg()    # Call the savejpg method to save the output image to the test file
    
             # Use os.path.exists to check if the test file exists
             self.assertTrue(os.path.exists(test_image_path), "Image should be saved successfully")
    
             # Load the saved image and check that its dimensions match those of the output image
             saved_image = cv2.imread(test_image_path)
             self.assertEqual(saved_image.shape, main_window.output_image.shape, "Saved image should have the same dimensions as the output image")

            
            
if __name__ == '__main__':
    unittest.main()