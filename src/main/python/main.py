from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import QApplication
from passwordGeneratorGUI import PasswordGenerator

import sys

if __name__ == '__main__':
    # General needs
    appctxt = ApplicationContext()
    app = QApplication([])
    window = PasswordGenerator()
    
    window.setWindowTitle('Password Generator')
    window.show()

    # Run
    exit_code = appctxt.app.exec_() 
    sys.exit(exit_code)