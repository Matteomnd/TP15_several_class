from PySide2.QtWidgets import QWidget, QVBoxLayout, QApplication, QHBoxLayout, QPushButton, QTextEdit, QLabel, QDialog
from Partie1 import SQLClientWindow
class LabeledTextField(QWidget):
    def __init__(self,text):
        QWidget.__init__(self)
        self.text= text

        self.layout = QHBoxLayout()

        self.label = QLabel(self.text)
        self.textEdit = QTextEdit()
        self.textEdit.setMaximumHeight(20)

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.textEdit)

        self.setLayout(self.layout)




class ConfigurationDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.layout = QVBoxLayout()
        self.object1 = LabeledTextField("IP address")
        self.layout.addWidget(self.object1)

        self.object2 = LabeledTextField("User")
        self.layout.addWidget(self.object2)

        self.object3 = LabeledTextField("Password")
        self.layout.addWidget(self.object3)

        self.setLayout(self.layout)






if __name__ == "__main__":
   app = QApplication([])
   win = ConfigurationDialog()
   win2= SQLClientWindow()
   win.show()
   win2.show()
   app.exec_()
