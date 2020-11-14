from PyQt5 import QtWidgets, uic
import sys

#Variables
global chosenApps
chosenApps = []

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('form.ui', self)
        self.setWindowTitle("Welcome to IXOS")
        self.show()
        self.button = self.findChild(QtWidgets.QPushButton, 'b1')
        self.button.clicked.connect(self.printButtonPressed)

    def printButtonPressed(self):
        # This is executed when the button is pressed
        print('printButtonPressed')
        dialog = DialogUi()
        dialog.exec_()
        try:
            if acceptedTos:
                print("Continue to app selection")
                self.close()
                dialog = AppDialogUi()
                dialog.exec_()
        except Exception as e:
            print("Error occured, showing error dialogue!\n",e)


class DialogUi(QtWidgets.QDialog):
    def __init__(self):
        super(DialogUi, self).__init__()
        uic.loadUi('dialog.ui', self)
        self.setWindowTitle("Accept TOS")
        self.button = self.findChild(QtWidgets.QPushButton, 'accept')
        self.button.clicked.connect(self.acceptButtonPressed)
        self.button2 = self.findChild(QtWidgets.QPushButton, 'cancel')
        self.button2.clicked.connect(self.cancelButtonPressed)
        self.show()

    def acceptButtonPressed(self):
        # This is executed when the button is pressed
        print('acceptButtonPressed')
        global acceptedTos
        acceptedTos = True
        print(acceptedTos)
        self.close()

    def cancelButtonPressed(self):
        # This is executed when the button is pressed
        print('cancelButtonPressed')
        self.close()

class AppDialogUi(QtWidgets.QDialog):
    def __init__(self):
        super(AppDialogUi, self).__init__()
        uic.loadUi('appdialog.ui', self)
        self.setWindowTitle("Select Applications")
        self.button = self.findChild(QtWidgets.QPushButton, 'continue_2')
        self.button.clicked.connect(self.continueButtonPressed)
        self.button2 = self.findChild(QtWidgets.QPushButton, 'cancel')
        self.button2.clicked.connect(self.cancelButtonPressed)
        self.show()

    def continueButtonPressed(self):
        # This is executed when the button is pressed
        print('continueButtonPressed')

        self.close()

    def cancelButtonPressed(self):
        # This is executed when the button is pressed
        print('cancelButtonPressed')
        self.close()


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()

