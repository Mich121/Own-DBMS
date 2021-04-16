import mysql.connector

def connecttoserver(host, username, password, database):
    connection = None
    try:
        connection = mysql.connector.connect(host=host, user=username, password=password, database=database)
    except:
        QMessageBox.information(self,"Warning!","Connection failed!")
    return connection