import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt5.uic import loadUi
import sqlite3


class CoffeeApp(QMainWindow):
    def __init__(self):
        super(CoffeeApp, self).__init__()
        loadUi("main.ui", self)
        self.setWindowTitle("Coffee App")
        self.show()
        self.connection = sqlite3.connect("coffee.sqlite")
        self.cursor = self.connection.cursor()
        self.fill_table()

    def fill_table(self):
        self.tableWidget.setRowCount(0)
        self.cursor.execute("SELECT * FROM coffee")
        data = self.cursor.fetchall()
        for row_num, row_data in enumerate(data):
            self.tableWidget.insertRow(row_num)
            for column_num, column_data in enumerate(row_data):
                self.tableWidget.setItem(
                    row_num, column_num, QTableWidgetItem(str(column_data))
                )

    def closeEvent(self, event):
        self.connection.close()
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CoffeeApp()
    sys.exit(app.exec_())
