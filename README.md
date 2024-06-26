
# PyQtInteractiveConsole

<div style="text-align: justify">
PyQtInteractiveConsole is a Python-based project that provides an interactive Python console within a PyQt5 application. It leverages the Jupyter Qt console's rich widgets and the IPython kernel for executing Python commands, managing variables, and printing text. It also allows customization of the console's appearance, including the banner text and font size.

The Python script uses PyQt5 to create a GUI application with an embedded IPython console. The script defines two classes: QIPythonWidget and ApplicationGui. QIPythonWidget is a custom widget that extends the RichJupyterWidget class from the qtconsole package. This widget provides an interactive Python console within the GUI. It has methods for executing Python commands, printing text, and managing variables in the kernel. The __init__ method initializes the widget, starts the kernel, and sets up the kernel client. The print_text method is used to print specified text in the console. The pushVariables method pushes specified variables to the kernel. The clearTerminal method clears the console, and the executeCommand method executes a specified command in the console.ApplicationGui is the main application GUI, which is a subclass of QtWidgets.QMainWindow. It contains an instance of QIPythonWidget as an attribute. In the __init__ method, it loads a UI file, shows the window, initializes the IPython console, and executes some commands. The Dumptoipy method dumps the current instance variables to the IPython console. The Clearipy method clears the IPython console. The print_process_id function prints the process ID of the current process. The script's entry point is at the bottom. If the script is run as the main module, it creates a QApplication, an instance of ApplicationGui, shows the window, sets the style of the window, and starts the application's main loop.
</div>

![Image description](Capture.PNG)

Harsh Kumar Narula
<harsh.narula@iitbombay.org>
