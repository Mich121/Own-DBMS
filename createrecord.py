import connection
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class CreateRecord(QWidget):
    def __init__(self):
        super().__init__()
        self.dbname = " "
        self.setGeometry(250,150,1000,500)
        self.setWindowTitle('Create Record')
        self.setWindowIcon(QIcon('icons/database.png'))
        self.setFont(QFont("Times", 14))
        self.setStyleSheet("background-color:#FD9A29; color:white;") 
        self.setFixedSize(self.size())  #block extending of window

    async def UI(self):
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
        self.RecordLabel = QLabel("CREATE RECORD")
        self.RecordLabel.setAlignment(Qt.AlignCenter)
        self.ChooseBtn = QPushButton("CHOOSE")
        self.ChooseBtn.clicked.connect(self.FuncChooseTable)
        self.CreateRecordBtn = QPushButton("CREATE")
        self.CreateRecordBtn.clicked.connect(self.FuncCreateRecord)

        self.ChooseTable = QComboBox()
        self.ChooseTable.addItems(self.listoftables)

        self.Values = QTableWidget()
        self.Values.setStyleSheet("selection-background-color:gray; background-color:white; color:#CE7224;")
        self.Values.setRowCount(10)

        self.CreateRecordImg = QLabel()
        CreateRecordPixmap = QPixmap('icons/createrecord240px.png')
        self.CreateRecordImg.setPixmap(CreateRecordPixmap)
        self.CreateRecordImg.setAlignment(Qt.AlignCenter)
        self.CreateRecordImg.setContentsMargins(0,50,0,0) #(left, top, right, bottom)

    def Layout(self):
        #containers
        self.CreateRecordMainLayout = QHBoxLayout()
        self.CreateRecordLeft = QVBoxLayout()
        self.CreateRecordRight = QVBoxLayout()
        #left
        self.CreateRecordLeft.addWidget(self.RecordLabel)
        self.CreateRecordLeft.addWidget(self.CreateRecordImg)
        self.CreateRecordLeft.addStretch()
        self.CreateRecordLeft.addWidget(self.ChooseTable)
        self.CreateRecordLeft.addWidget(self.ChooseBtn)
        self.CreateRecordLeft.addWidget(self.CreateRecordBtn)
        self.CreateRecordLeft.setAlignment(Qt.AlignCenter)
        #right
        self.CreateRecordRight.addWidget(self.Values)
        #setting
        self.CreateRecordMainLayout.addLayout(self.CreateRecordLeft, 30)
        self.CreateRecordMainLayout.addLayout(self.CreateRecordRight, 70)
        self.setLayout(self.CreateRecordMainLayout)

    def FuncChooseTable(self):
        self.Connect = connection.connecttoserver("localhost","root","mysql123.installer",self.dbname)
        self.cursor = self.Connect.cursor()

        self.table = self.ChooseTable.currentText()
        #take columns names and display to tablewidget
        self.cursor.execute(f"SHOW COLUMNS FROM {self.table}")
        columns = self.cursor.fetchall()
        self.num_of_col = len(columns)
        self.Values.setColumnCount(self.num_of_col)
        for i, columnname in enumerate(columns):
            self.Values.setHorizontalHeaderItem(i, QTableWidgetItem(columnname[0]))


    def FuncCreateRecord(self):
        for row in range(10):
            rowData = []
            for column in range(self.num_of_col):
                values = self.Values.item(row, column)
                if(values and values.text()):
                    rowData.append(values.text())
                else:
                    rowData.append('NULL')

            query = ""
            #we do it because if field is digit you can add normally but if not you must use: 'field'
            for i in rowData:
                if(i.isdigit()):
                    query += i + "," 
                else:
                    query += "'" + i + "',"
            letters = len(query)
            query = query[:letters - 1]
            if 'NULL' in rowData:
                continue
            else:
                self.cursor.execute(f"INSERT INTO {self.table} VALUES ({query})")
                self.Connect.commit()
                
        self.close()


    async def TakeDataBaseName(self, name):
        self.dbname = name

