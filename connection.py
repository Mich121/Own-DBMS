import mysql.connector
from PyQt5.QtWidgets import QMessageBox

def connecttoserver(host, username, password, database):
    connection = None
    try:
        connection = mysql.connector.connect(host=host, user=username, password=password, database=database)
    except:
        QMessageBox.information("Warning!","Connection failed!")
    return connection