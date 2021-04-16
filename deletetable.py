import connection
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class DeleteTable(QWidget):
    def __init__(self):
        super().__init__()
        self.dbname = " "
        self.setGeometry(250,150,350,500)
        self.setWindowTitle('Delete Table')
        self.setWindowIcon(QIcon('icons/database.png'))
        self.setFont(QFont("Times", 14))
        self.setStyleSheet("background-color:#392F5A; color:white;") 
        self.setFixedSize(self.size())  #block extending of window

    def UI(self):
        self.GetTables()
        self.Widgets()
        self.Layout()
        self.show()

    def GetTables(self):
        self.Connect = connection.connecttoserver("localhost","root","mysql123.installer",self.dbname)
        cursor = self.Connect.cursor()
        cursor.execute("SHOW TABLES")
        self.listoftables = cursor.fetchall()
        self.listoftables = [ i[0] for i in self.listoftables ]   #change to list, in we have tables name in some database
  
    def Widgets(self):
        self.TableLabel = QLabel("DELETE TABLE")
        self.TableLabel.setAlignment(Qt.AlignCenter)
        self.DeleteTableBtn = QPushButton("DELETE")
        self.DeleteTableBtn.clicked.connect(self.DeleteTable)
        self.ChooseTable = QComboBox()
        self.ChooseTable.addItems(self.listoftables)
        self.DeleteTableImg = QLabel()
        DeleteTablePixmap = QPixmap('icons/deletetable240px.png')
        self.DeleteTableImg.setPixmap(DeleteTablePixmap)
        self.DeleteTableImg.setAlignment(Qt.AlignCenter)
        self.DeleteTableImg.setContentsMargins(0,50,0,0) #(left, top, right, bottom)

    def Layout(self):
        self.DeleteTableMainLayout = QVBoxLayout()
        self.DeleteTableMainLayout.addWidget(self.TableLabel)
        self.DeleteTableMainLayout.addWidget(self.DeleteTableImg)
        self.DeleteTableMainLayout.addStretch()
        self.DeleteTableMainLayout.addWidget(self.ChooseTable)
        self.DeleteTableMainLayout.addWidget(self.DeleteTableBtn)
        self.DeleteTableMainLayout.setAlignment(Qt.AlignCenter)
        self.setLayout(self.DeleteTableMainLayout)

    def DeleteTable(self):
        table = self.ChooseTable.currentText()
        try:
            cursor = self.Connect.cursor()
            cursor.execute(f"DROP TABLE {table}")
            self.Connect.commit()
            QMessageBox.information(self, "Warning!", "SUCCESS!")
            self.close()
        except:
            QMessageBox.information(self, "Warning!", "FAILED!")


    def TakeDataBaseName(self,name):
        self.dbname = name
