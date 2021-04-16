import connection
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class CreateTable(QWidget):
    def __init__(self):
        super().__init__()
        self.dbname = " "
        self.setGeometry(250,150,500,500)
        self.setWindowTitle('Create Table')
        self.setWindowIcon(QIcon('icons/database.png'))
        self.setFont(QFont("Times", 14))
        self.setStyleSheet("background-color:#6B8496; color:white;") 
        self.setFixedSize(self.size())  #block extending of window
        self.UI()
        self.show()

    def UI(self):
        self.Widgets()
        self.Layout()
  
    def Widgets(self):
        self.TableLabel = QLabel("CREATE TABLE")
        self.TableLabel.setAlignment(Qt.AlignCenter)

        self.CreateTableBtn = QPushButton("CREATE")
        self.CreateTableBtn.clicked.connect(self.CreateTable)
        
        self.NameNewTable = QLineEdit()
        self.NameNewTable.setPlaceholderText("New Table Name...")
        self.Query = QLineEdit()
        self.Query.setPlaceholderText("Fields...")


        self.CreateTableImg = QLabel()
        CreateTablePixmap = QPixmap('icons/createtable240px.png')
        self.CreateTableImg.setPixmap(CreateTablePixmap)
        self.CreateTableImg.setAlignment(Qt.AlignCenter)
        self.CreateTableImg.setContentsMargins(0,50,0,0) #(left, top, right, bottom)

    def Layout(self):
        self.CreateTableMainLayout = QVBoxLayout()
        self.CreateTableMainLayout.addWidget(self.TableLabel)
        self.CreateTableMainLayout.addWidget(self.CreateTableImg)
        self.CreateTableMainLayout.addStretch()
        self.CreateTableMainLayout.addWidget(self.NameNewTable)
        self.CreateTableMainLayout.addWidget(self.Query)
        self.CreateTableMainLayout.addWidget(self.CreateTableBtn)

        self.CreateTableMainLayout.setAlignment(Qt.AlignCenter)
        self.setLayout(self.CreateTableMainLayout)

    def CreateTable(self):
        name = self.NameNewTable.text()
        fields = self.Query.text()
        try:
            Connect = connection.connecttoserver("localhost","root","mysql123.installer",self.dbname)
            cursor = Connect.cursor()
            cursor.execute(f"CREATE TABLE {name} ({fields})")
            Connect.commit()

            QMessageBox.information(self, "Warning!", "SUCCESS!")
            self.close()
        except:
            QMessageBox.information(self, "Warning!", "FAILED!")


    def TakeDataBaseName(self,name):
        self.dbname = name

