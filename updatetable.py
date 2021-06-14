import connection
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class UpdateTable(QWidget):
    def __init__(self):
        super().__init__()
        self.dbname = " "
        self.setGeometry(250,150,350,500)
        self.setWindowTitle('Update Table')
        self.setWindowIcon(QIcon('icons/database.png'))
        self.setFont(QFont("Times", 14))
        self.setStyleSheet("background-color:#FAC878; color:white;") 
        self.setFixedSize(self.size())  #block extending of window

    async def UI(self):
        self.GetTables()
        self.Widgets()
        self.Layout()
        self.show()

    def GetTables(self):
        self.Connect = connection.connecttoserver("localhost","root","mysql123.installer",self.dbname)
        self.cursor = self.Connect.cursor()
        self.cursor.execute("SHOW TABLES")
        self.listoftables = self.cursor.fetchall()
        self.listoftables = [ i[0] for i in self.listoftables ]   #change to list, in we have tables name in some database
  
    def Widgets(self):
        self.TableLabel = QLabel("UPDATE TABLE")
        self.TableLabel.setAlignment(Qt.AlignCenter)
        self.UpdateTableBtn = QPushButton("UPDATE")
        self.UpdateTableBtn.clicked.connect(self.UpdateTable)
        self.ChooseTable = QComboBox()
        self.ChooseTable.addItems(self.listoftables)
        self.NameNewTable = QLineEdit()
        self.NameNewTable.setPlaceholderText("New column write name and type...")
        self.NameDeleteTable = QLineEdit()
        self.NameDeleteTable.setPlaceholderText("Delete column write name...")
        self.UpdateTableImg = QLabel()
        UpdateTablePixmap = QPixmap('icons/updatetable240px.png')
        self.UpdateTableImg.setPixmap(UpdateTablePixmap)
        self.UpdateTableImg.setAlignment(Qt.AlignCenter)
        self.UpdateTableImg.setContentsMargins(0,50,0,0) #(left, top, right, bottom)

    def Layout(self):
        self.UpdateTableMainLayout = QVBoxLayout()
        self.UpdateTableMainLayout.addWidget(self.TableLabel)
        self.UpdateTableMainLayout.addWidget(self.UpdateTableImg)
        self.UpdateTableMainLayout.addStretch()
        self.UpdateTableMainLayout.addWidget(self.ChooseTable)
        self.UpdateTableMainLayout.addWidget(self.NameNewTable)
        self.UpdateTableMainLayout.addWidget(self.NameDeleteTable)
        self.UpdateTableMainLayout.addWidget(self.UpdateTableBtn)

        self.UpdateTableMainLayout.setAlignment(Qt.AlignCenter)
        self.setLayout(self.UpdateTableMainLayout)

    def UpdateTable(self):
        table = self.ChooseTable.currentText()
        new = self.NameNewTable.text()
        delete = self.NameDeleteTable.text()
        try:
            if new != "":
                self.cursor.execute(f"ALTER TABLE {table} ADD COLUMN {new}")
                self.Connect.commit()
            if delete != "":
                self.cursor.execute(f"ALTER TABLE {table} DROP COLUMN {delete}")
                self.Connect.commit()
            QMessageBox.information(self,"Warning!","Success!")

            self.NameNewTable.setText("")
            self.NameDeleteTable.setText("")
        except:
            QMessageBox.information(self,"Warning!","Failed!")

    
    async def TakeDataBaseName(self, name):
        self.dbname = name