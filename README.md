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
* ***geology.txt***： Geological two-dimensional array raster data provided by the company
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
