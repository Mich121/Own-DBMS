import connection
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class UpdateRecord(QWidget):
    def __init__(self):
        super().__init__()
        self.dbname = " "
        self.setGeometry(250,150,1000,500)
        self.setWindowTitle('Update Record')
        self.setWindowIcon(QIcon('icons/database.png'))
        self.setFont(QFont("Times", 14))
        self.setStyleSheet("background-color:#FAAC40; color:white;") 
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
        self.RecordLabel = QLabel("UPDATE RECORD")
        self.RecordLabel.setAlignment(Qt.AlignCenter)
        self.ChooseBtn = QPushButton("CHOOSE")
        self.ChooseBtn.clicked.connect(self.SelectTable)
        self.ChooseTable = QComboBox()
        self.ChooseTable.addItems(self.listoftables)

        self.Table = QTableWidget()
        self.Table.setStyleSheet("selection-background-color:gray; background-color:white; color:#CE7224;")
        self.Table.selectionModel().selectionChanged.connect(self.FuncUpdateRecord)  #inicialize changing value

        self.UpdateRecordImg = QLabel()
        UpdateRecordPixmap = QPixmap('icons/updaterecord240px.png')
        self.UpdateRecordImg.setPixmap(UpdateRecordPixmap)
        self.UpdateRecordImg.setAlignment(Qt.AlignCenter)
        self.UpdateRecordImg.setContentsMargins(0,50,0,0)

        self.UpdateText = QLineEdit()   #write value and click to cell to change value in database
        self.UpdateText.setPlaceholderText("Write value and click appropriate cell to change...")

    def Layout(self):
        #containers
        self.UpdateRecordMainLayout = QHBoxLayout()
        self.UpdateRecordLeft = QVBoxLayout()
        self.UpdateRecordRight = QVBoxLayout()
        #left
        self.UpdateRecordLeft.addWidget(self.RecordLabel)
        self.UpdateRecordLeft.addWidget(self.UpdateRecordImg)
        self.UpdateRecordLeft.addStretch()
        self.UpdateRecordLeft.addWidget(self.ChooseTable)
        self.UpdateRecordLeft.addWidget(self.ChooseBtn)
        self.UpdateRecordLeft.addWidget(self.UpdateText)
        self.UpdateRecordLeft.setAlignment(Qt.AlignCenter)
        #right
        self.UpdateRecordRight.addWidget(self.Table)
        #setting
        self.UpdateRecordMainLayout.addLayout(self.UpdateRecordLeft, 30)
        self.UpdateRecordMainLayout.addLayout(self.UpdateRecordRight, 70)
        self.setLayout(self.UpdateRecordMainLayout)


    def SelectTable(self):
        self.table = self.ChooseTable.currentText() #take table which we will display
        self.cursor.execute(f"SELECT * FROM {self.table}")
        result = self.cursor.fetchall()

        #dimensions of table
        self.cursor.execute(f"SHOW COLUMNS FROM {self.table}")
        self.columns = self.cursor.fetchall()
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

    def FuncUpdateRecord(self, selected):
        #take name of columns
        colum = [i[0] for i in self.columns]
        #get indexes of changeable cell
        for ix in selected.indexes():
            row = ix.row()
            column = ix.column()
        #take values from different column in know row
        Id = []
        for iterator in range(len(colum)):
            Id.append(self.Table.item(row, iterator).text())
        #change value in window and save value from qlineedit
        field = self.UpdateText.text()
        self.Table.setItem(row, column, QTableWidgetItem(field))
        self.UpdateText.setText("") #reset text in qlineedit
        #get column name where we change value
        appropriatecolumn = self.columns[column][0]
        #make query to update cell
        query = f"UPDATE {self.table} SET {appropriatecolumn} = '{field}' WHERE "

        for i, elements in enumerate(colum):
            query += f"{elements} = '{Id[i]}' AND "

        #this operation remove 'AND ', after it query is ready
        lengthofquery = len(query)
        query = query[:lengthofquery - 4]

        try:
            self.cursor.execute(query)
            self.Connect.commit()
        except:
            QMessageBox.information(self,"Warning!","Failed!")


    async def TakeDataBaseName(self, name):
        self.dbname = name


