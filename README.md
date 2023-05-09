# **Site Suitability**
***
## **Background/Purpose of the Project**
The goal of this project in Python was to develop software for a company that produces stone to help them explore three important factors to consider when opening a factory in the UK: ***geography***, ***transport***, and ***population***. The software uses ***two-dimensional raster data*** provided by the company for each factor (values range from [0, 255], with higher values indicating a better location for the plant) to generate a suitability image for each factor. Finally, by assigning different weight values to each factor and adding the weighted factors, the comprehensive suitability image and its two-dimensional raster data are generated to give the overall suitability score of each raster location.  
In addition, the software provides a graphical user interface (Graphical User Interface，GUI), allowing users to easily select the weight values of different factors through the slider, and view the suitability image under the weight assignment in real time, which realizes the visualization of the data results. Users can also save the suitability image as JPG format for easy viewing and further analysis and decision making at any time.
***
## **Testing the code**
The unit_test.py file provides a unit test suite for your project.This suite is designed to test the functionality of your project, including image manipulation, loading and saving data, and user interaction using a graphical user interface (GUI). The unit test suite contains multiple test cases to ensure the correct execution of the main script and verify the correct functionality of the GUI elements.  
Unit test scripts use the unittest module to manage and execute test cases. It also uses the unittest.mock module to create mock objects and simulate the behavior of external dependencies such as the Tkinter library.  
The script includes a custom MockTkinter context manager that simulates the Tkinter library behavior for testing purposes. The context manager is used for the test_savejpg test case.

![image](https://user-images.githubusercontent.com/124676681/236950351-2ba203e9-7237-445a-9e30-21749e641190.png)
***
## **Main Function**
- [x] Color images showing geological, transportation, and population data 
- [x] The weights of geological, transportation, and demographic data are adjusted in real time using slider controls 
- [x] Displays a weighted image calculated from the weights set by the user 
- [x] Save the weighted images as files in JPEG format 
- [x] Save the suitability evaluation matrix to a text file
***
## **Environment Dependencies**
1. This project is recommended to run with Python ***3.7*** and ***higher***.
    1. Set up your Python environment on ***Windows***:
        1. Download Python installer, recommended download from the official website: https://www.python.org/downloads/
        2. Run the installer, select Custom Install, and check Add Python to your system environment variable.
        3. Once the installation is complete, open a command prompt or PowerShell and type ***python -V***. If the Python version is outputted correctly, your Python environment has been configured.
    2. Set up your Python environment on ***Mac OS***:
        1. The Mac OS comes with Python, but you may need to install the Xcode command-line tool to support Python development.
        2. To install Python using Homebrew, you can use the following command: ***brew install python***
        3. Configuring a virtual environment can help manage Python dependencies. You can use the venv module to create virtual environments.
    3. Set up your Python environment on ***Linux***:
        1. Python comes preinstalled on most Linux systems. You can check if it is installed by running the following command: ***python -V***
        2. Use your system package manager to install Python and Python packages. On Ubuntu and Debian systems, it can be installed using the following command: ***sudo apt-get install python3 python3-pip***
        3. The venv module can be used to create virtual environments to isolate the dependencies of different projects.  
2. After installing Python, make sure you have installed pip, which is a package manager for Python. Since ***Python 3.4***, pip is usually installed with Python. To check if you already have pip installed, enter the following at the command line: ***pip --version*** ， If you see the version information for pip, then you have installed pip successfully. If not, please refer to the https://pip.pypa.io/en/stable/installation/ installation PIP.  
Next, you need to create a virtual environment to install the project's dependencies. From the command line, go to the directory where your project is located and run the following command: ***python -m venv venv*** ， This will create a virtual environment called "venv" in the project directory. To activate the virtual environment, run the following command:
    1. For Windows users: ***venv\Scripts\activate***
    2. For macOS/Linux users: ***source venv/bin/activate***  
    
Once the virtual environment is activated, you can install the required dependencies for your project via pip. At the command line, enter the following: ***pip install opencv-python pandas numpy tk matplotlib os unittest*** ， This command will install libraries such as cv2 (OpenCV), pandas, numpy, tkinter, matplotlib, os, and unittest.  
To check if these libraries have been successfully installed in your virtual environment, you can run the following command: ***pip list*** ， This will display the installed packages and their versions. If you see the names of the required libraries, they have been successfully installed.  
Here are the Python libraries and their versions needed for this project:
* cv2 (OpenCV)：4.0.0 and higher
* pandas：1.0.0 and higher
* numpy：1.16.0 and higher
* tkinter：8.6.0 and higher
* matplotlib：3.0.0 and higher
* os
* unittest  

Common ways to configure python libraries are：
1. Installing Python libraries with pip: Python libraries can be installed using the pip tool, either from the command line or in the terminal with the following command: pip install library name. For example, to install the cv2 library, you can use the following command: ***pip install opencv-python***. If you want to install a specific version of the library, you can use a command like this: ***pip installLibrary name == version number***.
2. Installing Python libraries with Anaconda: If you are using Anaconda Python environment, you can use the conda tool to install Python libraries. This can be installed from the command line or terminal using the following command: ***conda install library name***. For example, to install the numpy library, you can use the following command: ***conda install numpy***.
3. Install Python libraries in IDE: If you are using a Python IDE like PyCharm, Spyder, etc., you can install libraries directly in the IDE. Library management options can usually be found in the IDE's Settings or preferences. For example, in PyCharm, the library manager can be found under ***File->Settings->Project->Project Interpreter***.

Some libraries (such as cv2 and matplotlib) may require the use of system libraries to support certain features (such as graphical interfaces). In this case, it is necessary to ensure that the appropriate system libraries are installed and that the correct environment variables (e.g., LD_LIBRARY_PATH) are configured. If you have problems installing the library, refer to the tutorials and help files in the official documentation or community forums.
***
## **FileDescription**
* [***geology.txt***](/geology.txt)： Geological two-dimensional array raster data provided by the company
* ***transport.txt***： Two-dimensional array raster data of traffic provided by the company
* ***population.txt***： Population two-dimensional array raster data provided by the company
* ***Suitability_evaluation.txt***： Generated final suitability two-dimensional array raster data according to the selected weight values (this file will be updated in real time according to the different weight values selected by the user)
* ***test_data.txt***： The file is a test file for the test_load_data test case. This file contains simple test data to verify that the load_data function in the main script loads data from the file correctly.
* ***test_suitability.txt***： The file is a test file for the test_save_suitability_evaluation_to_txt test case. This file is used to verify that the save_suitability_evaluation_to_txt method in the main script correctly saves the suitability evaluation data to a text file.
* ***main.py***： This file is the code and comments that implement all the features of this project
* ***unit_test.py***： This file is the test code of the project, which is used to test whether the project code can run successfully. If there is an error, the error will be pointed out in detail, so as to facilitate the correction of bugs
* ***result_1.jpg***： The file is the final suitability image generated after selecting the corresponding weight value (the image will be saved as jpg format, users can input the file name, save path and whether to save)
* ***test_image.jpg***： This file is used to test whether the save function can run normally. If the file can be generated normally, the code can run normally
* ***README.md***： This file is a description of the project and the tests, so that the reader can understand the project and how the code runs
***
## **How to use this project**
1. Prepare: Store your geological, transportation, and population data as text files and name them ***geology.txt***, ***transport.txt***, and ***population.txt*** respectively. These text files should contain comma-separated numbers, with each line representing a row of pixels of the image. Make sure the files are in the same directory as the code files. (The above text file will be automatically loaded when you run the program)
2. Run the program: From the command line, navigate to the directory containing the code files, and run the program by typing the following: ***python main.py***
3. Adjusting weights: The program will open a window containing geological, traffic, and population images as well as weighted images. You'll see three sliders controlling the weights for geological, transportation, and population data, respectively. Adjust these weights using the slider to assign the appropriate weight to each dataset according to your needs. (In the program, we set a limit that the weight values cannot be 0 at the same time.If the sliders are all 0, a window will pop up to remind the user to correct. In addition, the sum of the ideal weight values is set to 1. If the sum of the actual weight values is greater than or less than 1, the weights will be distributed proportionally so that the result is 1.)


![image](https://user-images.githubusercontent.com/124676681/236950922-d4fc067c-78bb-48c6-af13-521d98d7345f.png)
![image](https://user-images.githubusercontent.com/124676681/236951127-6a62d14a-09b5-4568-b54f-edd588a0bbfe.png)
![image](https://user-images.githubusercontent.com/124676681/236951176-d88aedb5-b7b1-40ad-b5ea-562a032cdad7.png)

5. Update the image: After adjusting the weights, click the ***"refresh"*** button. The program will calculate the weighted image based on the weights you choose and update the displayed image in the window.
6. save the weighted image: If you are satisfied with the calculated weighted image, click the ***"Save"*** button. This will open a file dialog box where you can select where you want to save the weighted image as a JPEG format file. Select a location and click "Save", the image will be saved to the location of your choice.
7. End the program: After you have done everything, you can close the program and exit by clicking the Close button in the top right corner of the window.



![image](https://user-images.githubusercontent.com/124676681/236950708-da1444bf-2515-463d-a39b-776ec07f9a65.png)
***
## **Code Structure**
1. ***main.py***
    1. ***def load_data(file_path: str)***： The function load_data takes an input parameter file_path, which indicates the path of the text file to read. The data is first read from the text file using the read_csv function from the pandas library. The function uses a comma as a separator and has no list head.The function then converts the read data to a numpy array and uses the dtype argument to specify that the data type is np.uint8, which is an unsigned 8-bit integer.Finally, the function returns a numpy array containing the read data.
    2. The ***main_win*** class is the main class of the application and is responsible for creating GUI components, handling user events and handling image data. This class contains the following methods:
        1. ***def __init__(self,root:tk.Tk)***: This is an initializer that takes a single argument of type tk.Tk,root, for the GUI window object. In this method, the components of your program are created and configured.
        2. ***root.title("Weight Slider App")***: Sets the title of the window to "Weight Slider App".
        3. Create a Matplotlib graph object called figure and set the size of the graph to 12x12 inches. Next, you add an axis object named ax to the graph at a position from (0, 0) to (1, 1).
        4. Create a Tkinter available Matplotlib canvas object with figure as a graphical parameter and place it on the root window. The Matplotlib canvas is placed on the GUI window, filling the entire window and positioned at the top.
        5. Create three slider controls (geology weight, traffic weight, and population weight) and place them on the root window. The sliders range from 0 to 1 with a step size of 0.001 and are displayed horizontally.
        6. Sets the initial value of the slider control.
        7. Create two button controls, bt1 and bt2, for refreshing and saving images, respectively. The self.refresh method is called when the "refresh" button is clicked Call the self.savejpg method when the "save" button is clicked.
        8. Layout the slider control and add the button control to the right side of the GUI window.
        9. Create a label that displays the sum of the weights. Listen for slider changes and update the weight sum.
        10. ***def update_total_weight(self,event)***: A method that updates the sum of the weights. Get the current values of the three slider controls and calculate the sum of the weights. If the weights do not sum to 1, update the value of the slider control to ensure that the weights do.
        11. ***def refresh(self)*** ：method for refreshing an image The new image is calculated based on the weights and normalized. Four images (geology, traffic, population, and adaptation assessment) are displayed on a canvas. Save the fitness evaluation results to a text file.
        12. ***def savejpg(self)***: A method to save the image. The file dialog box pops up to get the file path selected by the user. Save the resulting array as an image in JPEG format. The user is prompted to save successfully and the file path is displayed.
    3. ***if __name__ == "__main__"***: The main entry point for the program. Create a window and instantiate main_win
2. ***unit_test.py***
    1. ***test_load_data***: This test case checks whether the load_data function in the main script correctly loads the data in the given file.
    2. ***test_save_suitability_evaluation_to_txt***: This test case verifies that the save_suitability_evaluation_to_txt method in the main script saves the suitability evaluation data to a text file, as expected.
    3. ***test_savejpg***: This test case ensures that the savejpg method in the main script saves an output image with the correct dimensions to a file.
***
## ***Matters Need Attention***
1. When adjusting the slider, make sure the sum of all weights is 1. If the total weight is not 1, the application will automatically adjust the weight.
2. If all weights are set to 0, an error message box will pop up prompting the user to adjust at least one of the weights.
3. After the weight values are reassigned, the refresh button must be clicked for the final suitability image to change
***
## **Thoughts and Problems Encountered While Writing the Project**
1. ***Editorial Thought***
    1. python library of choice: OpenCV is mainly used for reading and processing image data, including image conversion, filtering, color space conversion, image stitching, etc. In this project, we read and processed three image data using OpenCV, and then synthesized them into a single adaptive evaluation image. Matplotlib is mainly used for plotting charts and images, including histograms, line charts, scatter plots, bar charts, and so on. In this project, we used Matplotlib to display and save the fitness evaluation images. The underlying implementation differs: OpenCV is written in C++, and Matplotlib is written in Python, which makes OpenCV faster to execute, while Matplotlib is easier to use and write. The interface is also different.OpencV's interface is mostly functions and classes, whereas Matplotlib is object-based and provides a variety of customizable plotting methods and parameters. But in this project, both play an important role, and I think both are suitable for use.
2. ***Problem Encountered***
    1. When loading the file, I tried to add an automatic pop-up file selection window. This part of the code was successful, but when I tried to achieve a feature that the order of file selection was consistent with the order of the weight slider and the order of the weight image, my code didn't succeed. Three things happened at runtime:
        1. The image was not loaded successfully
        2. The program is stuck and needs to exit and reenter
        3. The image loads, but it's a little weird

<img width="489" alt="1683586151235" src="https://user-images.githubusercontent.com/124676681/236955220-3bbd8659-6136-4df0-8b6a-25c9b7f4d1c4.png">

    2. For the final suitability image: I wanted to implement the real-time update function of the image, that is, I didn't need to click the refresh button, and as the slider moved, the image would automatically change accordingly, but I didn't succeed.
    3. For the distribution of weight values: When calculating the sum of weight values, I add the weights of the three, which may lead to the sum of weight values greater than or less than 1. In this case, according to the algorithm I wrote, 1 will be divided by the current weight value to obtain a proportion. Multiplying the weight values of the three impact factors with this proportion will obtain the weight values of the three factors in proportion under this condition. In an ideal world, this weight should always sum to 1, but due to the shortcomings of the method itself, small errors may occur, such as 0.99 and 1.01 when setting two decimal places, 0.999 and 1.001 when setting three decimal places. This error can be reduced by increasing the number of decimal places. But it can't be eliminated. In addition, too many digits will also cause some trouble to the balance and adjustment of the influence factors of the site selection in real life.
***
## **Summary and Reflection**
In my opinion, this code is a good implementation of what the company wanted, which is to easily select the weight of each factor and visualize the appropriateness. And to a certain extent, it can provide reference for the site selection of the company's factory. But that doesn't mean the code is perfect. As I mentioned above, there is a lot that could be improved.

    
