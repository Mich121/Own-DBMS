import connection
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import mysql.connector

class DeleteDataBase(QWidget):
    delete = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.database = " "
        self.setGeometry(250,150,350,500)
        self.setWindowTitle('Delete Database')
        self.setWindowIcon(QIcon('icons/database.png'))
        self.setFont(QFont("Times", 14))
        self.setStyleSheet("background-color:#F4D06F; color:white;") 
        self.setFixedSize(self.size())  #block extending of window
        self.UI()
        self.show()

    def UI(self):
        self.GetDataBase()
        self.Widgets()
        self.Layout()

    def GetDataBase(self):
        self.mydb = mysql.connector.connect(host="localhost", user="root", password="mysql123.installer")
        self.cursor = self.mydb.cursor()
        self.cursor.execute("SHOW DATABASES")
        self.listofdatabases = self.cursor.fetchall()
        self.listofdatabases = [ i[0] for i in self.listofdatabases ]   #change to list, in we have database name
  
    def Widgets(self):
        self.DatabaseLabel = QLabel("DELETE DATABASE")
        self.DatabaseLabel.setAlignment(Qt.AlignCenter)
        self.ChooseDataBase = QComboBox()
        self.ChooseDataBase.addItems(self.listofdatabases)
        self.DeleteDataBaseBtn = QPushButton("DELETE")
        self.DeleteDataBaseBtn.clicked.connect(self.DeleteDataBase)

        self.DeleteDataBaseImg = QLabel()
        DeleteDataBasePixmap = QPixmap('icons/deletedatabase240px.png')
        self.DeleteDataBaseImg.setPixmap(DeleteDataBasePixmap)
        self.DeleteDataBaseImg.setAlignment(Qt.AlignCenter)
        self.DeleteDataBaseImg.setContentsMargins(0,50,0,0) #(left, top, right, bottom)

    def Layout(self):
        #create two box 
        self.DeleteDataBaseMainLayout = QVBoxLayout()
        self.DeleteDataBaseForm = QVBoxLayout()

        #top, MainLayout
        self.DeleteDataBaseMainLayout.addWidget(self.DatabaseLabel)
        self.DeleteDataBaseMainLayout.addWidget(self.DeleteDataBaseImg)
        self.DeleteDataBaseMainLayout.addStretch()

        #bottom, BaseForm
        self.DeleteDataBaseForm.addWidget(self.ChooseDataBase)
        self.DeleteDataBaseMainLayout.addLayout(self.DeleteDataBaseForm)
        self.DeleteDataBaseForm.setAlignment(Qt.AlignCenter)
        self.DeleteDataBaseMainLayout.addWidget(self.DeleteDataBaseBtn)
        self.setLayout(self.DeleteDataBaseMainLayout)

    def DeleteDataBase(self):
        try:
            self.database = self.ChooseDataBase.currentText()
            query =  (f"DROP DATABASE {self.database}")
            self.cursor.execute(query)
            self.mydb.commit()

            QMessageBox.information(self, "Warning!", "SUCCESS!")
            self.delete.emit(self.database)
            self.close()
        except:
            QMessageBox.information(self, "Warning!", "FAILED!")


