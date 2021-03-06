import sys
from PyQt5 import QtWidgets
import design
import sqlite3


class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.bd_select)

    def bd_select(self):
        self.listView.clear()
        '''connect = sqlite3.connect('Chinook_Sqlite.sqlite')
        cursor = connect.cursor()
        cursor.execute("SELECT Name FROM Artist ORDER BY Name LIMIT 3")
        result = cursor.fetchall()
        '''
        result = ['rfr', 'rcg', '1212', 13]
        self.listView.addItem('sdgfsg')

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()

