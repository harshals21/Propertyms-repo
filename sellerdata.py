# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sellerdata.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import MySQLdb as mdb
import ast

def MyConverter(mydata):
		def cvt(mydata):
			try:
				return ast.literal_eval(mydata)

			except Exception:
				return str(mydata)
		return tuple(map(cvt, mydata))


class Ui_MainWindow(object):
	def LoadData(self):
		try:
			db = mdb.connect('localhost','root','','pyqt5')

			cur = db.cursor()
			rows = cur.execute("select * from seller")
			seller = cur.fetchall()

			for row in seller:
				self.addTable(MyConverter(row))

			cur.close()
		except mdb.Error as e:
			print("error")
			print(e)



	def addTable(self, columns):
		rowPosition = self.tableWidget.rowCount()
		self.tableWidget.insertRow(rowPosition)

		for i, column in enumerate(columns):
			self.tableWidget.setItem(rowPosition, i, QtWidgets.QTableWidgetItem(str(column)))


	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(844, 653)
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
		self.verticalLayout.setObjectName("verticalLayout")
		self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
		self.tableWidget.setRowCount(10)
		self.tableWidget.setColumnCount(7)
		self.tableWidget.setObjectName("tableWidget")
		self.verticalLayout.addWidget(self.tableWidget)
		self.pushButton = QtWidgets.QPushButton(self.centralwidget)
		font = QtGui.QFont()
		font.setPointSize(10)
		self.pushButton.setFont(font)
		self.pushButton.setObjectName("pushButton")
		self.pushButton.clicked.connect(self.LoadData)
		self.verticalLayout.addWidget(self.pushButton)
		MainWindow.setCentralWidget(self.centralwidget)
		self.statusbar = QtWidgets.QStatusBar(MainWindow)
		self.statusbar.setObjectName("statusbar")
		MainWindow.setStatusBar(self.statusbar)

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
		self.pushButton.setText(_translate("MainWindow", "Load Data"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
