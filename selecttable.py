import connection
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class SelectTable(QWidget):
    def __init__(self):
        super().__init__()
        self.dbname = " "
        self.setGeometry(250,150,1000,500)
        self.setWindowTitle('Select Table')
        self.setWindowIcon(QIcon('icons/database.png'))
        self.setFont(QFont("Times", 14))
        self.setStyleSheet("background-color:#FAAC40; color:white;") 
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
        #left layout widget
        self.TableLabel = QLabel("SELECT TABLE")
        self.TableLabel.setAlignment(Qt.AlignCenter)
        self.SelectTableBtn = QPushButton("SELECT")
        self.SelectTableBtn.clicked.connect(self.SelectTable)
        self.ChooseTable = QComboBox()
        self.ChooseTable.addItems(self.listoftables)
        self.SelectTableImg = QLabel()
        SelectTablePixmap = QPixmap('icons/selecttable240px.png')
        self.SelectTableImg.setPixmap(SelectTablePixmap)
        self.SelectTableImg.setAlignment(Qt.AlignCenter)
        self.SelectTableImg.setContentsMargins(0,50,0,0) #(left, top, right, bottom)
        #right layout widget
        self.Table = QTableWidget()
        self.Table.setMinimumSize(QSize(0, 0))
        self.Table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.Table.setStyleSheet("selection-background-color:gray; background-color:white; color:#CE7224;")

    def Layout(self):
        #containers
        self.SelectTableMainLayout = QHBoxLayout()
        self.SelectTableLeft = QVBoxLayout()
        self.SelectTableRight = QVBoxLayout()
        #left layout
        self.SelectTableLeft.addWidget(self.TableLabel)
        self.SelectTableLeft.addWidget(self.SelectTableImg)
        self.SelectTableLeft.addStretch()
        self.SelectTableLeft.addWidget(self.ChooseTable)
        self.SelectTableLeft.addWidget(self.SelectTableBtn)
        self.SelectTableLeft.setAlignment(Qt.AlignCenter)
        #right layout
        self.SelectTableRight.addWidget(self.Table)

        #setting all
        self.SelectTableMainLayout.addLayout(self.SelectTableLeft, 20)  #20% width of tablemainlayout
        self.SelectTableMainLayout.addLayout(self.SelectTableRight, 80)
        self.setLayout(self.SelectTableMainLayout)

    def SelectTable(self):
        table = self.ChooseTable.currentText() #take table which we will display
        Connect = connection.connecttoserver("localhost","root","mysql123.installer",self.dbname)
        cursor = Connect.cursor()
        cursor.execute(f"SELECT * FROM {table}")
        result = cursor.fetchall()

        #dimensions of table
        cursor.execute(f"SHOW COLUMNS FROM {table}")
        columns = cursor.fetchall()
        num_of_col = len(columns)
        cursor.execute(f"SELECT COUNT(*) FROM {table}")
        rows = cursor.fetchall()
        self.Table.setRowCount(rows[0][0])  #rows it is [(number,)] why we use rows[0][0]
        self.Table.setColumnCount(num_of_col)

        #display data from table
        self.Table.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.Table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.Table.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        #change column name
        for i, columnname in enumerate(columns):
         self.Table.setHorizontalHeaderItem(i, QTableWidgetItem(columnname[0]))


    def TakeDataBaseName(self, name):
        self.dbname = name
