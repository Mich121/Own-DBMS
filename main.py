import sys
import style
import mysql.connector
import connection, connectdatabase, createdatabase, deletedatabase
import createtable, deletetable, selecttable, updatetable
import createrecord, deleterecord, selectrecord, updaterecord
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import asyncio
import time

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.dbName = " "
        mydb = mysql.connector.connect(host="localhost", user="root", password="mysql123.installer")
        self.setGeometry(250,150,1000,800)
        self.setWindowTitle('Database Management App')
        self.setWindowIcon(QIcon('icons/database.png'))
        self.setFixedSize(self.size())  #block extending of window
        self.UI()
        self.show()

    def UI(self):
        self.tabWidget()
        self.widgets()
        self.layouts()

    def tabWidget(self):
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)    #thanks that we can see tables
        self.tab1 = QWidget()
        self.tabs.addTab(self.tab1, "")

    def widgets(self):
        #ConnectDatabaseBox
        self.connectdatabaseImg = QLabel()
        connectdatabasePixmap = QPixmap('icons/connectdatabase.png')
        self.connectdatabaseImg.setPixmap(connectdatabasePixmap)
        self.connectdatabaseImg.setAlignment(Qt.AlignCenter)
        self.connectdatabaseBtn = QPushButton(f"CONNECT DATABASE \nconnected with:{self.dbName}")
        self.connectdatabaseBtn.clicked.connect(self.FuncConnectDataBaseBtn)
        #CreateDatabaseBox
        self.createdatabaseImg = QLabel()
        createdatabasePixmap = QPixmap('icons/createdatabase.png')
        self.createdatabaseImg.setPixmap(createdatabasePixmap)
        self.createdatabaseImg.setAlignment(Qt.AlignCenter)
        self.createdatabaseBtn = QPushButton("CREATE DATABASE")
        self.createdatabaseBtn.clicked.connect(self.FuncCreateDataBaseBtn)
        #DeleteDatabaseBox
        self.deletedatabaseImg = QLabel()
        deletedatabasePixmap = QPixmap('icons/deletedatabase.png')
        self.deletedatabaseImg.setPixmap(deletedatabasePixmap)
        self.deletedatabaseImg.setAlignment(Qt.AlignCenter)
        self.deletedatabaseBtn = QPushButton("DELETE DATABASE")
        self.deletedatabaseBtn.clicked.connect(self.FuncDeleteDataBaseBtn)
        #CreateTableBox
        self.createtableImg = QLabel()
        createtablePixmap = QPixmap('icons/createtable.png')
        self.createtableImg.setPixmap(createtablePixmap)
        self.createtableImg.setAlignment(Qt.AlignCenter)
        self.createtableBtn = QPushButton("CREATE TABLE")
        self.createtableBtn.clicked.connect(self.FuncCreateTableBtn)
        #SelectTableBox
        self.selecttableImg = QLabel()
        selecttablePixmap = QPixmap('icons/selecttable.png')
        self.selecttableImg.setPixmap(selecttablePixmap)
        self.selecttableImg.setAlignment(Qt.AlignCenter)
        self.selecttableBtn = QPushButton("SELECT TABLE")
        self.selecttableBtn.clicked.connect(self.FuncSelectTableBtn)
        #DeleteTableBox
        self.deletetableImg = QLabel()
        deletetablePixmap = QPixmap('icons/deletetable.png')
        self.deletetableImg.setPixmap(deletetablePixmap)
        self.deletetableImg.setAlignment(Qt.AlignCenter)
        self.deletetableBtn = QPushButton("DELETE TABLE")
        self.deletetableBtn.clicked.connect(self.FuncDeleteTableBtn)
        #UpdateTableBox
        self.updatetableImg = QLabel()
        updatetablePixmap = QPixmap('icons/updatetable.png')
        self.updatetableImg.setPixmap(updatetablePixmap)
        self.updatetableImg.setAlignment(Qt.AlignCenter)
        self.updatetableBtn = QPushButton("UPDATE TABLE")
        self.updatetableBtn.clicked.connect(self.FuncUpdateTableBtn)
        #CreateRecordBox
        self.createrecordImg = QLabel()
        createrecordPixmap = QPixmap('icons/createrecord.png')
        self.createrecordImg.setPixmap(createrecordPixmap)
        self.createrecordImg.setAlignment(Qt.AlignCenter)
        self.createrecordBtn = QPushButton("CREATE RECORD")
        self.createrecordBtn.clicked.connect(self.FuncCreateRecord)
        #SelectRecordBox
        self.selectrecordImg = QLabel()
        selectrecordPixmap = QPixmap('icons/selectrecord.png')
        self.selectrecordImg.setPixmap(selectrecordPixmap)
        self.selectrecordImg.setAlignment(Qt.AlignCenter)
        self.selectrecordBtn = QPushButton("SELECT RECORD")
        self.selectrecordBtn.clicked.connect(self.FuncSelectRecord)
        #DeleteRecordBox
        self.deleterecordImg = QLabel()
        deleterecordPixmap = QPixmap('icons/deleterecord.png')
        self.deleterecordImg.setPixmap(deleterecordPixmap)
        self.deleterecordImg.setAlignment(Qt.AlignCenter)
        self.deleterecordBtn = QPushButton("DELETE RECORD")
        self.deleterecordBtn.clicked.connect(self.FuncDeleteRecord)
        #UpdateRecordBox
        self.updaterecordImg = QLabel()
        updaterecordPixmap = QPixmap('icons/updaterecord.png')
        self.updaterecordImg.setPixmap(updaterecordPixmap)
        self.updaterecordImg.setAlignment(Qt.AlignCenter)
        self.updaterecordBtn = QPushButton("UPDATE RECORD")
        self.updaterecordBtn.clicked.connect(self.FuncUpdateRecord)

    def layouts(self):
        ###############################Main window
        self.MainLayout = QVBoxLayout()
        ###################################################Top
        self.TopMainGroupBox = QGroupBox()
        self.TopMainLayout = QVBoxLayout()
        ###
        self.ConnectDatabaseBox = QHBoxLayout()
        self.ConnectDatabaseGroupBox = QGroupBox()
        self.ConnectDatabaseBox.addWidget(self.connectdatabaseImg)
        self.ConnectDatabaseBox.addWidget(self.connectdatabaseBtn)
        self.ConnectDatabaseGroupBox.setLayout(self.ConnectDatabaseBox)
        self.ConnectDatabaseGroupBox.setStyleSheet("background-color:#9DD9D2;")
        self.TopMainLayout.addWidget(self.ConnectDatabaseGroupBox)
        ###
        self.CreateDatabaseBox = QHBoxLayout()
        self.CreateDatabaseGroupBox = QGroupBox()
        self.CreateDatabaseBox.addWidget(self.createdatabaseImg)
        self.CreateDatabaseBox.addWidget(self.createdatabaseBtn)
        self.CreateDatabaseGroupBox.setLayout(self.CreateDatabaseBox)
        self.CreateDatabaseGroupBox.setStyleSheet("background-color:#FF8811;")
        self.TopMainLayout.addWidget(self.CreateDatabaseGroupBox)
        ###
        self.DeleteDatabaseBox = QHBoxLayout()
        self.DeleteDatabaseGroupBox = QGroupBox()
        self.DeleteDatabaseBox.addWidget(self.deletedatabaseImg)
        self.DeleteDatabaseBox.addWidget(self.deletedatabaseBtn)
        self.DeleteDatabaseGroupBox.setLayout(self.DeleteDatabaseBox)
        self.DeleteDatabaseGroupBox.setStyleSheet("background-color:#F4D06F;")
        self.TopMainLayout.addWidget(self.DeleteDatabaseGroupBox)
        ###
        self.TopMainGroupBox.setLayout(self.TopMainLayout)
        self.TopMainGroupBox.setStyleSheet(style.TopMainGroupBox())
        self.MainLayout.addWidget(self.TopMainGroupBox)
        ###################################################Table
        self.TableBox = QHBoxLayout()
        self.Table1 = QVBoxLayout()
        self.Table2 = QVBoxLayout()
        self.TableGroupBox = QGroupBox()

        self.CreateTableBox = QHBoxLayout()
        self.CreateTableGroupBox = QGroupBox()
        self.CreateTableBox.addWidget(self.createtableImg)
        self.CreateTableBox.addWidget(self.createtableBtn)
        self.CreateTableGroupBox.setStyleSheet("background-color:#6B8496;")
        self.CreateTableGroupBox.setLayout(self.CreateTableBox)
        self.Table1.addWidget(self.CreateTableGroupBox)
        ###
        self.SelectTableBox = QHBoxLayout()
        self.SelectTableGroupBox = QGroupBox()
        self.SelectTableBox.addWidget(self.selecttableImg)
        self.SelectTableBox.addWidget(self.selecttableBtn)
        self.SelectTableGroupBox.setStyleSheet("background-color:#FAAC40;")
        self.SelectTableGroupBox.setLayout(self.SelectTableBox)
        self.Table1.addWidget(self.SelectTableGroupBox)
        ###
        self.DeleteTableBox = QHBoxLayout()
        self.DeleteTableGroupBox = QGroupBox()
        self.DeleteTableBox.addWidget(self.deletetableImg)
        self.DeleteTableBox.addWidget(self.deletetableBtn)
        self.DeleteTableGroupBox.setStyleSheet("background-color:#464569;")
        self.DeleteTableGroupBox.setLayout(self.DeleteTableBox)
        self.Table2.addWidget(self.DeleteTableGroupBox)
        ###
        self.UpdateTableBox = QHBoxLayout()
        self.UpdateTableGroupBox = QGroupBox()
        self.UpdateTableBox.addWidget(self.updatetableImg)
        self.UpdateTableBox.addWidget(self.updatetableBtn)
        self.UpdateTableGroupBox.setStyleSheet("background-color:#FAC878;")
        self.UpdateTableGroupBox.setLayout(self.UpdateTableBox)
        self.Table2.addWidget(self.UpdateTableGroupBox)

        self.TableBox.addLayout(self.Table1)
        self.TableBox.addLayout(self.Table2)
        self.TableGroupBox.setLayout(self.TableBox)
        self.TableGroupBox.setStyleSheet(style.TableGroupBox())
        self.MainLayout.addWidget(self.TableGroupBox)
        ###################################################Record
        self.RecordBox = QHBoxLayout()
        self.Record1 = QVBoxLayout()
        self.Record2 = QVBoxLayout()
        self.RecordGroupBox = QGroupBox()

        self.CreateRecordBox = QHBoxLayout()
        self.CreateRecordGroupBox = QGroupBox()
        self.CreateRecordBox.addWidget(self.createrecordImg)
        self.CreateRecordBox.addWidget(self.createrecordBtn)
        self.CreateRecordGroupBox.setStyleSheet("background-color:#FD9A29;")
        self.CreateRecordGroupBox.setLayout(self.CreateRecordBox)
        self.Record1.addWidget(self.CreateRecordGroupBox)
        ###
        self.SelectRecordBox = QHBoxLayout()
        self.SelectRecordGroupBox = QGroupBox()
        self.SelectRecordBox.addWidget(self.selectrecordImg)
        self.SelectRecordBox.addWidget(self.selectrecordBtn)
        self.SelectRecordGroupBox.setStyleSheet("background-color:#525A78;")
        self.SelectRecordGroupBox.setLayout(self.SelectRecordBox)
        self.Record1.addWidget(self.SelectRecordGroupBox)
        ###
        self.DeleteRecordBox = QHBoxLayout()
        self.DeleteRecordGroupBox = QGroupBox()
        self.DeleteRecordBox.addWidget(self.deleterecordImg)
        self.DeleteRecordBox.addWidget(self.deleterecordBtn)
        self.DeleteRecordGroupBox.setStyleSheet("background-color:#789AA5;")
        self.DeleteRecordGroupBox.setLayout(self.DeleteRecordBox)
        self.Record2.addWidget(self.DeleteRecordGroupBox)
        ###
        self.UpdateRecordBox = QHBoxLayout()
        self.UpdateRecordGroupBox = QGroupBox()
        self.UpdateRecordBox.addWidget(self.updaterecordImg)
        self.UpdateRecordBox.addWidget(self.updaterecordBtn)
        self.UpdateRecordGroupBox.setStyleSheet("background-color:#FAAC40;")
        self.UpdateRecordGroupBox.setLayout(self.UpdateRecordBox)
        self.Record2.addWidget(self.UpdateRecordGroupBox)

        self.RecordBox.addLayout(self.Record1)
        self.RecordBox.addLayout(self.Record2)
        self.RecordGroupBox.setLayout(self.RecordBox)
        self.RecordGroupBox.setStyleSheet(style.RecordGroupBox())
        self.MainLayout.addWidget(self.RecordGroupBox)
        #######################################
        self.setLayout(self.MainLayout)
        self.tab1.setLayout(self.MainLayout)

    def FuncConnectDataBaseBtn(self):
        self.connectdatabase = connectdatabase.ConnectDataBase()
        self.connectdatabase.connect.connect(self.UpdateConnectionText)
        self.connectdatabase.show()
    
    @pyqtSlot(str)
    def UpdateConnectionText(self, databasename):
        self.dbName = databasename
        self.connectdatabaseBtn.setText(f"CONNECT DATABASE \nconnected with: {self.dbName}")

    @pyqtSlot(str)
    def UpdateDeleteText(self, databasename):
        if self.dbName == databasename:
            self.connectdatabaseBtn.setText(f"CONNECT DATABASE \nconnected with: ")

    def FuncCreateDataBaseBtn(self):
        self.createdatabase = createdatabase.CreateDataBase()

    def FuncDeleteDataBaseBtn(self):
        self.deletedatabase = deletedatabase.DeleteDataBase()
        self.deletedatabase.delete.connect(self.UpdateDeleteText)

    def FuncCreateTableBtn(self):
        if self.dbName != " ":
            self.createtable = createtable.CreateTable()
            self.createtable.TakeDataBaseName(self.dbName)
        else:
            QMessageBox.information(self,"Warning!","You must choose database to create new table!")

    def FuncDeleteTableBtn(self):
        if self.dbName != " ":
            self.deletetable = deletetable.DeleteTable()
            asyncio.run(self.deletetable.TakeDataBaseName(self.dbName))
            asyncio.run(self.deletetable.UI())
        else:
            QMessageBox.information(self,"Warning!","You must choose database to delete table!")
    
    def FuncSelectTableBtn(self):
        if self.dbName != " ":
            self.selecttable = selecttable.SelectTable()
            asyncio.run(self.selecttable.TakeDataBaseName(self.dbName))
            asyncio.run(self.selecttable.UI())
        else:
            QMessageBox.information(self,"Warning!","You must choose database to select table!")

    def FuncUpdateTableBtn(self):
        if self.dbName != " ":
            self.updatetable = updatetable.UpdateTable()
            asyncio.run(self.updatetable.TakeDataBaseName(self.dbName))
            asyncio.run(self.updatetable.UI())
        else:
            QMessageBox.information(self,"Warning!","You must choose database to update table!")

    def FuncCreateRecord(self):
        if self.dbName != " ":
            self.createrecord = createrecord.CreateRecord()
            asyncio.run(self.createrecord.TakeDataBaseName(self.dbName))
            asyncio.run(self.createrecord.UI())
        else:
            QMessageBox.information(self,"Warning!","You must choose database to create record!")

    def FuncDeleteRecord(self):
        if self.dbName != " ":
            self.deleterecord = deleterecord.DeleteRecord()
            asyncio.run(self.deleterecord.TakeDataBaseName(self.dbName))
            asyncio.run(self.deleterecord.UI())
        else:
            QMessageBox.information(self,"Warning!","You must choose database to delete records!")

    def FuncUpdateRecord(self):
        if self.dbName != " ":
            self.updaterecord = updaterecord.UpdateRecord()
            asyncio.run(self.updaterecord.TakeDataBaseName(self.dbName))
            asyncio.run(self.updaterecord.UI())
        else:
            QMessageBox.information(self,"Warning!","You must choose database to update records!")

    def FuncSelectRecord(self):
        if self.dbName != " ":
            self.selectrecord = selectrecord.SelectRecord()
            asyncio.run(self.selectrecord.TakeDataBaseName(self.dbName))
            asyncio.run(self.selectrecord.UI())
        else:
            QMessageBox.information(self,"Warning!","You must choose database to select records!")
"""
    #this function it is unnecessary, i want to use it to delay window constructor and see only loading screen but it didnt work
    @property
    def delayinicialize(self):
        if not self._di:
            print("lazy initialization")
            self._di =  [i for i in range(100000)]
        return self._di
"""

class LoadingScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(900, 600)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.CustomizeWindowHint)
        self.labelanim = QLabel(self)
        self.loadingscreen = QMovie('icons/loadring.gif')
        self.labelanim.setMovie(self.loadingscreen)
        self.timer = QTimer()
        self.loadingscreen.start()
        self.timer.singleShot(1500, self.stopAnimation)
        self.show()

    def stopAnimation(self):
        self.loadingscreen.stop()
        self.close()

def main():
    app = QApplication([])
    loadingscreen = LoadingScreen()
    window = Window()
    app.exec_()

if __name__ == '__main__':
    main()