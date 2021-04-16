import connection
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import mysql.connector

class CreateDataBase(QWidget):
    def __init__(self):
        super().__init__()
        self.database = " "
        self.setGeometry(250,150,350,500)
        self.setWindowTitle('Create Database')
        self.setWindowIcon(QIcon('icons/database.png'))
        self.setFont(QFont("Times", 14))
        self.setStyleSheet("background-color:#FF8811; color:white;") 
        self.setFixedSize(self.size())  #block extending of window
        self.UI()
        self.show()

    def UI(self):
        self.Widgets()
        self.Layout()
  
    def Widgets(self):
        self.DatabaseLabel = QLabel("CREATE DATABASE")
        self.DatabaseLabel.setAlignment(Qt.AlignCenter)

        self.CreateDataBaseBtn = QPushButton("CREATE")
        self.CreateDataBaseBtn.clicked.connect(self.CreateDataBase)
        
        self.NameNewDB = QLineEdit()
        self.NameNewDB.setPlaceholderText("New Database Name...")

        self.CreateDataBaseImg = QLabel()
        CreateDataBasePixmap = QPixmap('icons/createdatabase240px.png')
        self.CreateDataBaseImg.setPixmap(CreateDataBasePixmap)
        self.CreateDataBaseImg.setAlignment(Qt.AlignCenter)
        self.CreateDataBaseImg.setContentsMargins(0,50,0,0) #(left, top, right, bottom)

    def Layout(self):
        self.CreateDataBaseMainLayout = QVBoxLayout()
        self.CreateDataBaseMainLayout.addWidget(self.DatabaseLabel)
        self.CreateDataBaseMainLayout.addWidget(self.CreateDataBaseImg)
        self.CreateDataBaseMainLayout.addStretch()
        self.CreateDataBaseMainLayout.addWidget(self.NameNewDB)
        self.CreateDataBaseMainLayout.addWidget(self.CreateDataBaseBtn)

        self.CreateDataBaseMainLayout.setAlignment(Qt.AlignCenter)
        self.setLayout(self.CreateDataBaseMainLayout)

    def CreateDataBase(self):
        name = self.NameNewDB.text()
        mydb = mysql.connector.connect(host="localhost", user="root", password="mysql123.installer")
        cursor = mydb.cursor()
        try:
            query =  (f"CREATE DATABASE {name}")
            cursor.execute(query)
            mydb.commit()

            QMessageBox.information(self, "Warning!", "SUCCESS!")
            self.close()
        except:
            QMessageBox.information(self, "Warning!", "FAILED!")



