import connection
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import asyncio

class SelectRecord(QWidget):
    def __init__(self):
        super().__init__()
        self.dbname = " "
        self.setGeometry(250,150,1000,500)
        self.setWindowTitle('Select Record')
        self.setWindowIcon(QIcon('icons/database.png'))
        self.setFont(QFont("Times", 14))
        self.setStyleSheet("background-color:#525A78; color:white;") 
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
        self.RecordLabel = QLabel("SELECT RECORD")
        self.RecordLabel.setAlignment(Qt.AlignCenter)
        self.ChooseBtn = QPushButton("SELECT")
        self.ChooseBtn.clicked.connect(self.SelectTable)
        self.ChooseTable = QComboBox()
        self.ChooseTable.addItems(self.listoftables)

        self.Table = QTableWidget()
        self.Table.setStyleSheet("selection-background-color:gray; background-color:white; color:#CE7224;")
        self.Table.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.SelectRecordImg = QLabel()
        SelectRecordPixmap = QPixmap('icons/updaterecord240px.png')
        self.SelectRecordImg.setPixmap(SelectRecordPixmap)
        self.SelectRecordImg.setAlignment(Qt.AlignCenter)
        self.SelectRecordImg.setContentsMargins(0,50,0,0)

        self.SelectText = QLineEdit()   #write value and click to cell to change value in database
        self.SelectText.setPlaceholderText("Find in table...")

    def Layout(self):
        #containers
        self.SelectRecordMainLayout = QHBoxLayout()
        self.SelectRecordLeft = QVBoxLayout()
        self.SelectRecordRight = QVBoxLayout()
        #left
        self.SelectRecordLeft.addWidget(self.RecordLabel)
        self.SelectRecordLeft.addWidget(self.SelectRecordImg)
        self.SelectRecordLeft.addStretch()
        self.SelectRecordLeft.addWidget(self.ChooseTable)
        self.SelectRecordLeft.addWidget(self.ChooseBtn)
        self.SelectRecordLeft.addWidget(self.SelectText)
        self.SelectRecordLeft.setAlignment(Qt.AlignCenter)
        #right
        self.SelectRecordRight.addWidget(self.Table)
        #setting
        self.SelectRecordMainLayout.addLayout(self.SelectRecordLeft, 30)
        self.SelectRecordMainLayout.addLayout(self.SelectRecordRight, 70)
        self.setLayout(self.SelectRecordMainLayout)


    def SelectTable(self):
        self.table = self.ChooseTable.currentText()
        regex = self.SelectText.text() #text which filter our query

        #find columns to construct query
        query = f"SELECT * FROM {self.table} WHERE "
        self.cursor.execute(f"SHOW COLUMNS FROM {self.table}")
        self.columns = self.cursor.fetchall()
          
        columnsnamelist = [i[0] for i in self.columns]
        for elements in columnsnamelist:
            query += f"{elements} LIKE '%{regex}%' OR "

        #remove 'OR ' from last iteration, after it query is ready to use
        numberofletters = len(query)
        query = query[:numberofletters - 3]

        #finding if text "" show whole tables else execute query
        if regex == "":
            self.cursor.execute(f"SELECT * FROM {self.table}")
            result = self.cursor.fetchall()
        else:
            self.cursor.execute(query)
            result = self.cursor.fetchall()

        #dimensions of table
        num_of_col = len(self.columns)
        self.cursor.execute(f"SELECT COUNT(*) FROM {self.table}")
        rows = self.cursor.fetchall()
        self.Table.setRowCount(rows[0][0])  #rows it is [(number,)] why we use rows[0][0]
        self.Table.setColumnCount(num_of_col)

        #display data from table
        self.Table.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.Table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.Table.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        #change column name
        for i, columnname in enumerate(self.columns):
         self.Table.setHorizontalHeaderItem(i, QTableWidgetItem(columnname[0]))



    async def TakeDataBaseName(self, name):
        self.dbname = name


