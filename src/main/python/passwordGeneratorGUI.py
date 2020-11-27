# Building with help from https://build-system.fman.io/pyqt5-tutorial

from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QCheckBox, QFileDialog, QMessageBox
import os
import functions as fns
import datetime

MINDEFAULTLENGTH = 8

class PasswordGenerator(QWidget):
    def __init__(self, parent=None):
        super(PasswordGenerator, self).__init__(parent)

        optionsWidget = QWidget()
        passwordLengthWidget = QWidget()
        resultWidget = QWidget()
        execWidget = QWidget()
        groupWidget = QWidget()

        # Get the correct layout - top-level
        windowLayout = QVBoxLayout()
        groupLayout = QHBoxLayout()

        optionsLayout = QVBoxLayout()
        passwordLengthLayout = QVBoxLayout()
        resultLayout = QHBoxLayout()
        execLayout = QHBoxLayout()

        # Create Buttons
        runButton = QPushButton('Generate')
        runButton.clicked.connect(self.generateNewPassword)
        
        closeButton = QPushButton('Quit')
        closeButton.clicked.connect(self.closeMe)

        # Create data entry fields
        self.resultEntry = QLineEdit()
        self.passLengthEntry = QLineEdit()
        self.passLengthEntry.setText(str(MINDEFAULTLENGTH))

        # Create options entry
        self.useUppercase = QCheckBox('Use uppercase letters')
        self.useUppercase.setChecked(True)
        self.usenumbers = QCheckBox('Use numbers')
        self.usenumbers.setChecked(True)
        self.usespecials = QCheckBox('Use special characters')
        self.usespecials.setChecked(True)

        # Upper block
        optionsLayout.addWidget(self.useUppercase)
        optionsLayout.addWidget(self.usenumbers)
        optionsLayout.addWidget(self.usespecials)
        optionsWidget.setLayout(optionsLayout)
        optionsWidget.show()

        # Pre-mid block...
        passwordLengthLayout.addWidget(QLabel('Number of characters:'))
        passwordLengthLayout.addWidget(self.passLengthEntry)
        passwordLengthWidget.setLayout(passwordLengthLayout)
        passwordLengthWidget.show()

        # Mid block 
        resultLayout.addWidget(QLabel('New Password:'))
        resultLayout.addWidget(self.resultEntry)
        resultWidget.setLayout(resultLayout)
        resultWidget.show()

        # Lower block
        execLayout.addWidget(runButton)
        execLayout.addWidget(closeButton)
        execWidget.setLayout(execLayout)
        execWidget.show()

        # Sort out a few more bits...
        groupLayout.addWidget(optionsWidget)
        groupLayout.addWidget(passwordLengthWidget)
        groupWidget.setLayout(groupLayout)
        groupWidget.show()

        windowLayout.addWidget(groupWidget)
        windowLayout.addWidget(resultWidget)
        windowLayout.addWidget(execWidget)
        self.setLayout(windowLayout)

    #################################
    def closeMe(self):
        self.close()
    
    #################################
    def generateNewPassword(self):
        passwordLengthRaw = self.passLengthEntry.text()

        if not passwordLengthRaw.isnumeric():
            self.resultEntry.setText('')
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText('Password length is empty or not integer!')
            msg.setWindowTitle('Failed')
            msg.setDetailedText('Enter an integer and try again.')
            msg.exec_()
            return
        
        passwordLength = int(passwordLengthRaw)
        newPassword = fns.generate_random_password(length=passwordLength, useUpper=self.useUppercase.isChecked(), useNumbers=self.usenumbers.isChecked(), 
            useSpecial=self.usespecials.isChecked())
        
        self.resultEntry.setText(newPassword)
        return
    