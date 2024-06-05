import os, sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from IPython.lib import guisupport
from qtconsole.inprocess import QtInProcessKernelManager
from qtconsole.rich_jupyter_widget import RichJupyterWidget
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from qtconsole.manager import QtKernelManager

class QIPythonWidget(RichJupyterWidget):
    """
    A custom widget that provides an interactive Python console.

    This widget extends the RichJupyterWidget class and adds additional functionality
    for executing Python commands, printing text, and managing variables in the kernel.

    Args:
        customBanner (str, optional): Custom banner text to be displayed in the console.
            Defaults to None.

    Attributes:
        font_size (int): The font size of the console.
        kernel_manager (QtInProcessKernelManager): The kernel manager for the widget.
        kernel_client (KernelClient): The kernel client for the widget.

    Signals:
        exit_requested: Signal emitted when the widget is requested to exit.

    Methods:
        print_text(text): Prints the specified text in the console.
        pushVariables(variableDict): Pushes the specified variables to the kernel.
        clearTerminal(): Clears the console.
        executeCommand(command): Executes the specified command in the console.
    """

    def __init__(self, customBanner=None, *args, **kwargs):
        super(QIPythonWidget, self).__init__(*args, **kwargs)
        if customBanner is not None:
            self.banner = customBanner
        self.font_size = 6
        self.kernel_manager = kernel_manager = QtInProcessKernelManager()
        kernel_manager.start_kernel(show_banner=False)
        kernel_manager.kernel.gui = 'qt'
        self.kernel_client = kernel_client = self._kernel_manager.client()
        kernel_client.start_channels()

        def stop():
            kernel_client.stop_channels()
            kernel_manager.shutdown_kernel()
            guisupport.get_app_qt().exit()

        self.exit_requested.connect(stop)
        # self.kernel_manager

    def print_text(self, text):
        """
        Prints the specified text in the console.

        Args:
            text (str): The text to be printed.
        """
        self._append_plain_text(text)

    def pushVariables(self, variableDict):
        """
        Pushes the specified variables to the kernel.

        Args:
            variableDict (dict): A dictionary containing the variables to be pushed.
        """
        self.kernel_manager.kernel.shell.push(variableDict)

    def clearTerminal(self):
        """
        Clears the console.
        """
        self._control.clear()

    def executeCommand(self, command):
        """
        Executes the specified command in the console.

        Args:
            command (str): The command to be executed.
        """
        self._execute(command, False)
        
def print_process_id():
    print(('Process ID is:', os.getpid()))
    
    
class ApplicationGui(QtWidgets.QMainWindow):
    """
    This class represents the main application GUI.

    Attributes:
        ipyConsole (QIPythonWidget): The IPython console widget.
    """

    def __init__(self, parent=None):
        super(ApplicationGui, self).__init__(parent)
        qtCreatorFile = "Application.ui"  # Enter file here.
        uic.loadUi(qtCreatorFile, self)
        self.show()
        self.ipyConsole = QIPythonWidget("Welcome to Application !!!, Developed By harsh.narula@iitbombay.org:\n\n ")
        self.layoutipy.addWidget(self.ipyConsole)
        self.ipyConsole.clearTerminal()
        self.ipyConsole.executeCommand("import numpy as np")
        self.ipyConsole.executeCommand("np.random.random(10)")      
        self.Dumptoipy()
        
    def Dumptoipy(self):
        """
        Dumps the current instance variables to the IPython console.
        """
        self.ipyConsole.pushVariables(dict(self=self))
         
    def Clearipy(self):
        """
        Clears the IPython console.
        """
        self.ipyConsole.executeCommand("if 'self' in globals(): del self")
    
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = ApplicationGui()
    window.show()
    window.setStyle(QtWidgets.QStyleFactory.create('cleanlooks'))
    sys.exit(app.exec_())