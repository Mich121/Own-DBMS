import connection
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class DeleteRecord(QWidget):
    def __init__(self):
        super().__init__()
        self.dbname = " "
        self.setGeometry(250,150,1000,500)
        self.setWindowTitle('Delete Record')
        self.setWindowIcon(QIcon('icons/database.png'))
        self.setFont(QFont("Times", 14))
        self.setStyleSheet("background-color:#789AA5; color:white;") 
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
        self.RecordLabel = QLabel("DELETE RECORD")
        self.RecordLabel.setAlignment(Qt.AlignCenter)
        self.ChooseBtn = QPushButton("CHOOSE")
        self.ChooseBtn.clicked.connect(self.SelectTable)

        self.ChooseTable = QComboBox()
        self.ChooseTable.addItems(self.listoftables)

        self.Table = QTableWidget()
        self.Table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.Table.setStyleSheet("selection-background-color:gray; background-color:white; color:#CE7224;")
        self.Table.doubleClicked.connect(self.FuncDeleteRecord) #delete record after double clicking

        self.DeleteRecordImg = QLabel()
        DeleteRecordPixmap = QPixmap('icons/deleterecord240px.png')
        self.DeleteRecordImg.setPixmap(DeleteRecordPixmap)
        self.DeleteRecordImg.setAlignment(Qt.AlignCenter)
        self.DeleteRecordImg.setContentsMargins(0,50,0,0) #(left, top, right, bottom)

    def Layout(self):
        #containers
        self.DeleteRecordMainLayout = QHBoxLayout()
        self.DeleteRecordLeft = QVBoxLayout()
        self.DeleteRecordRight = QVBoxLayout()
        #left
        self.DeleteRecordLeft.addWidget(self.RecordLabel)
        self.DeleteRecordLeft.addWidget(self.DeleteRecordImg)
        self.DeleteRecordLeft.addStretch()
        self.DeleteRecordLeft.addWidget(self.ChooseTable)
        self.DeleteRecordLeft.addWidget(self.ChooseBtn)
        self.DeleteRecordLeft.setAlignment(Qt.AlignCenter)
        #right
        self.DeleteRecordRight.addWidget(self.Table)
        #setting
        self.DeleteRecordMainLayout.addLayout(self.DeleteRecordLeft, 30)
        self.DeleteRecordMainLayout.addLayout(self.DeleteRecordRight, 70)
        self.setLayout(self.DeleteRecordMainLayout)


    def SelectTable(self):
        self.table = self.ChooseTable.currentText() #take table which we will display
        self.cursor.execute(f"SELECT * FROM {self.table}")
        result = self.cursor.fetchall()

        #dimensions of table
        self.cursor.execute(f"SHOW COLUMNS FROM {self.table}")
        columns = self.cursor.fetchall()
        num_of_col = len(columns)
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
        for i, columnname in enumerate(columns):
         self.Table.setHorizontalHeaderItem(i, QTableWidgetItem(columnname[0]))

        self.firstcolumnname = columns[0][0]   #take first column name we use it in FuncDeleteRecord

    def FuncDeleteRecord(self):
        row = self.Table.currentRow()
        #delete row in aplication
        self.Table.removeRow(row)
        #delete row in database
        field = self.Table.item(row, 0).text()
        try:
            self.cursor.execute(f"DELETE FROM {self.table} WHERE {self.firstcolumnname} = {field}")
            self.Connect.commit()
        except:
            QMessageBox.information(self,"Warning!","Failed!")


    async def TakeDataBaseName(self, name):
        self.dbname = name


