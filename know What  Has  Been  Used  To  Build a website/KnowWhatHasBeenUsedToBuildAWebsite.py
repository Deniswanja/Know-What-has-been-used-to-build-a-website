from PyQt5.QtWidgets  import *

from  builtwith import  builtwith
import sys

class MainWindow(QWidget):
    def __init__(self):
        self.website_information=""
        QWidget.__init__(self)
        self.setWindowTitle("Know What  has been used to Build a Website :")
        grid_layout=QGridLayout()
        label=QLabel("Enter Website URL:")
        grid_layout.addWidget(label,10,10)
        self.lineEdit=QLineEdit()
        self.lineEdit.setPlaceholderText("Enter the  website  URL :")
        button=QPushButton("Website Build Details")
        button.setStyleSheet("color:yellow")
        button.setStyleSheet("background-color:blue;color:yellow;border-radius:30px;")
        button.clicked.connect(self.get_website_built_Details)
        self.textarea=QPlainTextEdit()
        self.textarea.setReadOnly(True)
        self.textarea.setMinimumWidth(550)
        self.textarea.setMinimumHeight(300)
        self.textarea.setWordWrapMode(True)
        grid_layout.addWidget(self.textarea,12,10)
        grid_layout.addWidget(button,12,12)
        grid_layout.addWidget(self.lineEdit,10,12)

        self.setStyleSheet("Background-color:yellow;font-size:30px;")
        self.setLayout(grid_layout)

    def get_website_built_Details(self):
                 try:
                    self.website_url=self.lineEdit.text()
                    self.website_information=builtwith("http://"+self.website_url)
                    self.textarea.insertPlainText(str(self.website_url)+": "+str(self.website_information))
                 except Error:
                     alert=QMessageBox()
                     alert.setWindowTitle("Wrong  URL Format:")
                     alert.setText("Know URL Given  ,"+str(Error))
                     alert.exec_()



        

app=QApplication(sys.argv)
mainwindow=MainWindow()
mainwindow.show()
app.exec_()











