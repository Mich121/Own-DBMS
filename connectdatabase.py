import connection
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import mysql.connector

class ConnectDataBase(QWidget):
    connect = pyqtSignal(str)
    def __init__(self):
        super().__init__()
        self.database = " "
        self.setGeometry(250,150,350,500)
        self.setWindowTitle('Connect Database')
        self.setWindowIcon(QIcon('icons/database.png'))
        self.setFont(QFont("Times", 14))
        self.setStyleSheet("background-color:#9DD9D2; color:white;") 
        self.setFixedSize(self.size())  #block extending of window
        self.UI()
        self.show()

    def UI(self):
        self.GetDataBase()
        self.Widgets()
        self.Layout()


    def GetDataBase(self):
        mydb = mysql.connector.connect(host="localhost", user="root", password="mysql123.installer")
        cursor = mydb.cursor()
        cursor.execute("SHOW DATABASES")
        self.listofdatabases = cursor.fetchall()
        self.listofdatabases = [ i[0] for i in self.listofdatabases ]   #change to list, in we have database name
        
    def Widgets(self):
        self.DatabaseLabel = QLabel("CONNECT WITH DATABASE")
        self.DatabaseLabel.setAlignment(Qt.AlignCenter)
        self.ChooseDataBase = QComboBox()
        #self.ChooseDataBase.clear()
        self.ChooseDataBase.addItems(self.listofdatabases)
        self.ConnectDataBaseBtn = QPushButton("CONNECT")
        self.ConnectDataBaseBtn.clicked.connect(self.FuncConnectDataBase)

        self.ConnectDataBaseImg = QLabel()
        ConnectDataBasePixmap = QPixmap('icons/connectdatabase240px.png')
        self.ConnectDataBaseImg.setPixmap(ConnectDataBasePixmap)
        self.ConnectDataBaseImg.setAlignment(Qt.AlignCenter)
        self.ConnectDataBaseImg.setContentsMargins(0,50,0,0) #(left, top, right, bottom)

    def Layout(self):
        #create two box 
        self.ConnectDataBaseMainLayout = QVBoxLayout()
        self.ConnectDataBaseForm = QVBoxLayout()

        #top, MainLayout
        self.ConnectDataBaseMainLayout.addWidget(self.DatabaseLabel)
        self.ConnectDataBaseMainLayout.addWidget(self.ConnectDataBaseImg)
        self.ConnectDataBaseMainLayout.addStretch()

        #bottom, BaseForm
        self.ConnectDataBaseForm.addWidget(self.ChooseDataBase)
        self.ConnectDataBaseMainLayout.addLayout(self.ConnectDataBaseForm)
        self.ConnectDataBaseForm.setAlignment(Qt.AlignCenter)
        self.ConnectDataBaseMainLayout.addWidget(self.ConnectDataBaseBtn)

        self.setLayout(self.ConnectDataBaseMainLayout)

    def FuncConnectDataBase(self):
        try:
            self.database = self.ChooseDataBase.currentText()
            Connect = connection.connecttoserver("localhost","root","mysql123.installer",self.database)
            Connect.commit()
            self.connect.emit(self.database)
            self.close()
        except:
            QMessageBox.information(self,"Warning!","Connection failed!")


