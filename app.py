from PyQt5 import QtCore, QtGui, QtWidgets
import MySQLdb as mdb
import ast


class ui_login(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(980, 800)
		MainWindow.setStyleSheet("background-color: rgb(255, 255, 191);")
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.welcome_label = QtWidgets.QLabel(self.centralwidget)
		self.welcome_label.setGeometry(QtCore.QRect(40, 30, 191, 51))
		font = QtGui.QFont()
		font.setPointSize(25)
		self.welcome_label.setFont(font)
		self.welcome_label.setObjectName("welcome_label")
		self.line = QtWidgets.QFrame(self.centralwidget)
		self.line.setGeometry(QtCore.QRect(40, 90, 901, 16))
		font = QtGui.QFont()
		font.setBold(False)
		font.setWeight(50)
		self.line.setFont(font)
		self.line.setAutoFillBackground(False)
		self.line.setLineWidth(3)
		self.line.setFrameShape(QtWidgets.QFrame.HLine)
		self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line.setObjectName("line")

		self.buyer_btn = QtWidgets.QPushButton(self.centralwidget)
		self.buyer_btn.setGeometry(QtCore.QRect(420, 450, 161, 41))
		font = QtGui.QFont()
		font.setPointSize(14)
		font.setBold(False)
		font.setItalic(False)
		font.setWeight(50)
		self.buyer_btn.setFont(font)
		self.buyer_btn.setObjectName("buyer_btn")
		self.buyer_btn.setStyleSheet("background-color: rgb(255, 255, 255);")

		self.seller_btn = QtWidgets.QPushButton(self.centralwidget)
		self.seller_btn.setGeometry(QtCore.QRect(420, 530, 161, 41))
		font = QtGui.QFont()
		font.setPointSize(14)
		self.seller_btn.setFont(font)
		self.seller_btn.setObjectName("seller_btn")
		self.seller_btn.setStyleSheet("background-color: rgb(255, 255, 255);")

		self.deal_btn = QtWidgets.QPushButton(self.centralwidget)
		self.deal_btn.setGeometry(QtCore.QRect(840, 120, 101, 28))
		self.deal_btn.setObjectName("deal_btn")
		self.deal_btn.setStyleSheet("background-color: rgb(255, 255, 255);")

		self.soldprop_btn = QtWidgets.QPushButton(self.centralwidget)
		self.soldprop_btn.setGeometry(QtCore.QRect(840, 170, 101, 28))
		self.soldprop_btn.setObjectName("soldprop_btn")
		self.soldprop_btn.setStyleSheet("background-color: rgb(255, 255, 255);")

		self.image_label = QtWidgets.QLabel(self.centralwidget)
		self.image_label.setGeometry(QtCore.QRect(410, 210, 181, 171))
		self.image_label.setText("")
		self.image_label.setPixmap(QtGui.QPixmap("../../Pictures/admin.jpg"))
		self.image_label.setScaledContents(True)
		self.image_label.setObjectName("image_label")
		self.accnt_label = QtWidgets.QLabel(self.centralwidget)
		self.accnt_label.setGeometry(QtCore.QRect(400, 110, 211, 61))
		font = QtGui.QFont()
		font.setPointSize(18)
		font.setBold(False)
		font.setWeight(50)
		self.accnt_label.setFont(font)
		self.accnt_label.setObjectName("accnt_label")
		MainWindow.setCentralWidget(self.centralwidget)
		self.statusbar = QtWidgets.QStatusBar(MainWindow)
		self.statusbar.setObjectName("statusbar")
		MainWindow.setStatusBar(self.statusbar)
		#push buttons
		#opening of new window
		self.buyer_btn.clicked.connect(self.openbuyer)
		self.seller_btn.clicked.connect(self.openseller)
		self.deal_btn.clicked.connect(self.opendeal)
		self.soldprop_btn.clicked.connect(self.opensoldprop)

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
		self.welcome_label.setText(_translate("MainWindow", "Welcome!"))
		self.buyer_btn.setText(_translate("MainWindow", "BUYER "))
		self.seller_btn.setText(_translate("MainWindow", "SELLER"))
		self.deal_btn.setText(_translate("MainWindow", "CONFIRM DEAL"))
		self.soldprop_btn.setText(_translate("MainWindow", "SOLD Properties"))
		self.accnt_label.setText(_translate("MainWindow", "Create Account"))

	def openbuyer(self):

		self.window = QtWidgets.QMainWindow()
		self.ui = ui_buyer()
		self.ui.setupUi(self.window)
		self.window.show()

	def openseller(self):

		self.window = QtWidgets.QMainWindow()
		self.ui = ui_seller()
		self.ui.setupUi(self.window)
		self.window.show()

	def opendeal(self):

		self.window = QtWidgets.QMainWindow()
		self.ui = ui_dealpage()
		self.ui.setupUi(self.window)
		self.window.show()

	def opensoldprop(self):

		self.window = QtWidgets.QMainWindow()
		self.ui = ui_soldproptable()
		self.ui.setupUi(self.window)
		self.window.show() 


class ui_buyer(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(980, 800)
		font = QtGui.QFont()
		font.setPointSize(8)
		MainWindow.setFont(font)
		MainWindow.setStyleSheet("background-color: rgb(255, 255, 191);")
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.buyerdet_label = QtWidgets.QLabel(self.centralwidget)
		self.buyerdet_label.setGeometry(QtCore.QRect(380, 10, 221, 61))
		font = QtGui.QFont()
		font.setPointSize(18)
		self.buyerdet_label.setFont(font)
		self.buyerdet_label.setObjectName("buyerdet_label")
		self.line = QtWidgets.QFrame(self.centralwidget)
		self.line.setGeometry(QtCore.QRect(60, 70, 871, 20))
		self.line.setLineWidth(3)
		self.line.setFrameShape(QtWidgets.QFrame.HLine)
		self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line.setObjectName("line")

		self.name_label = QtWidgets.QLabel(self.centralwidget)
		self.name_label.setGeometry(QtCore.QRect(300, 120, 71, 31))
		font = QtGui.QFont()
		font.setPointSize(14)
		self.name_label.setFont(font)
		self.name_label.setObjectName("name_label")
		self.email_label = QtWidgets.QLabel(self.centralwidget)
		self.email_label.setGeometry(QtCore.QRect(280, 210, 101, 31))
		font = QtGui.QFont()
		font.setPointSize(14)
		self.email_label.setFont(font)
		self.email_label.setObjectName("email_label")
		self.phone_label = QtWidgets.QLabel(self.centralwidget)
		self.phone_label.setGeometry(QtCore.QRect(270, 310, 101, 21))
		font = QtGui.QFont()
		font.setPointSize(14)
		self.phone_label.setFont(font)
		self.phone_label.setObjectName("phone_label")
		self.budget_label = QtWidgets.QLabel(self.centralwidget)
		self.budget_label.setGeometry(QtCore.QRect(280, 410, 81, 31))
		font = QtGui.QFont()
		font.setPointSize(14)
		self.budget_label.setFont(font)
		self.budget_label.setObjectName("budget_label")
		self.location_label = QtWidgets.QLabel(self.centralwidget)
		self.location_label.setGeometry(QtCore.QRect(270, 500, 91, 31))
		font = QtGui.QFont()
		font.setPointSize(14)
		self.location_label.setFont(font)
		self.location_label.setObjectName("location_label")

		self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
		self.lineEdit.setGeometry(QtCore.QRect(380, 110, 241, 41))
		self.lineEdit.setObjectName("lineEdit")
		self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")

		self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
		self.lineEdit_2.setGeometry(QtCore.QRect(380, 200, 311, 41))
		self.lineEdit_2.setObjectName("lineEdit_2")
		self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")

		self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
		self.lineEdit_3.setGeometry(QtCore.QRect(380, 300, 191, 41))
		self.lineEdit_3.setObjectName("lineEdit_3")
		self.lineEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);")

		self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
		self.lineEdit_4.setGeometry(QtCore.QRect(380, 400, 151, 41))
		self.lineEdit_4.setObjectName("lineEdit_4")
		self.lineEdit_4.setStyleSheet("background-color: rgb(255, 255, 255);")

		self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
		self.lineEdit_5.setGeometry(QtCore.QRect(380, 490, 151, 41))
		self.lineEdit_5.setObjectName("lineEdit_5")
		self.lineEdit_5.setStyleSheet("background-color: rgb(255, 255, 255);")

		self.addbuyer_btn = QtWidgets.QPushButton(self.centralwidget)
		self.addbuyer_btn.setGeometry(QtCore.QRect(190, 690, 231, 41))
		font = QtGui.QFont()
		font.setPointSize(14)
		self.addbuyer_btn.setFont(font)
		self.addbuyer_btn.setObjectName("addbuyer_btn")
		self.addbuyer_btn.setStyleSheet("background-color: rgb(255, 255, 255);")

		self.cancel_btn = QtWidgets.QPushButton(self.centralwidget)
		self.cancel_btn.setGeometry(QtCore.QRect(560, 690, 231, 41))
		font = QtGui.QFont()
		font.setPointSize(14)
		self.cancel_btn.setFont(font)
		self.cancel_btn.setObjectName("cancel_btn")
		self.cancel_btn.setStyleSheet("background-color: rgb(255, 255, 255);")
		MainWindow.setCentralWidget(self.centralwidget)
		self.statusbar = QtWidgets.QStatusBar(MainWindow)
		self.statusbar.setObjectName("statusbar")
		MainWindow.setStatusBar(self.statusbar)
		#push buttons
		self.addbuyer_btn.clicked.connect(self.buyer)
		self.addbuyer_btn.clicked.connect(self.opensellerdata)
		self.cancel_btn.clicked.connect(self.openlogin)


		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
		self.buyerdet_label.setText(_translate("MainWindow", "BUYER DETAILS"))
		self.name_label.setText(_translate("MainWindow", "Name"))
		self.email_label.setText(_translate("MainWindow", "Email-id"))
		self.phone_label.setText(_translate("MainWindow", "Phone no"))
		self.budget_label.setText(_translate("MainWindow", "Budget "))
		self.location_label.setText(_translate("MainWindow", "Location"))
		self.addbuyer_btn.setText(_translate("MainWindow", "Add Buyer "))
		self.cancel_btn.setText(_translate("MainWindow", "Cancel"))

	def buyer(self):
		try:
			db = mdb.connect('localhost', 'root', '', 'pyqt5')

			print('database connected')
			name = self.lineEdit.text()
			Email = self.lineEdit_2.text()
			Phone = self.lineEdit_3.text()
			Budget = self.lineEdit_4.text()
			Location = self.lineEdit_5.text()
			print(name, " ", Email, " ", Phone, " ", Budget, " ", Location)

			print('done')
			cur = db.cursor()
			cur.execute("INSERT INTO buyer(name, email, phone, budget, location)"
				"VALUES(%s, %s, %s, %s, %s)",[name, Email, Phone, Budget, Location ])
		except mdb.Error as e:
			print("error")
			print(e)

	def openlogin(self):
		self.window = QtWidgets.QMainWindow()
		self.ui = ui_login()
		self.ui.setupUi(self.window)
		self.window.show()

	def opensellerdata(self):

		self.window = QtWidgets.QMainWindow()
		self.ui = ui_sellerdata()
		self.ui.setupUi(self.window)
		self.window.show()

class ui_seller(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(980, 800)
		MainWindow.setStyleSheet("background-color: rgb(255, 255, 191);")
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.sellerreg_label = QtWidgets.QLabel(self.centralwidget)
		self.sellerreg_label.setGeometry(QtCore.QRect(380, 10, 251, 51))
		font = QtGui.QFont()
		font.setPointSize(18)
		self.sellerreg_label.setFont(font)
		self.sellerreg_label.setObjectName("sellerreg_label")
		self.llname_label = QtWidgets.QLabel(self.centralwidget)
		self.llname_label.setGeometry(QtCore.QRect(260, 100, 161, 31))
		font = QtGui.QFont()
		font.setPointSize(14)
		self.llname_label.setFont(font)
		self.llname_label.setObjectName("llname_label")
		self.address_label = QtWidgets.QLabel(self.centralwidget)
		self.address_label.setGeometry(QtCore.QRect(320, 170, 91, 21))
		font = QtGui.QFont()
		font.setPointSize(14)
		self.address_label.setFont(font)
		self.address_label.setObjectName("address_label")
		self.contact_label = QtWidgets.QLabel(self.centralwidget)
		self.contact_label.setGeometry(QtCore.QRect(300, 250, 121, 21))
		font = QtGui.QFont()
		font.setPointSize(14)
		self.contact_label.setFont(font)
		self.contact_label.setObjectName("contact_label")
		self.location_label = QtWidgets.QLabel(self.centralwidget)
		self.location_label.setGeometry(QtCore.QRect(320, 330, 91, 21))
		font = QtGui.QFont()
		font.setPointSize(14)
		self.location_label.setFont(font)
		self.location_label.setObjectName("location_label")
		self.proptype_label = QtWidgets.QLabel(self.centralwidget)
		self.proptype_label.setGeometry(QtCore.QRect(270, 400, 151, 31))
		font = QtGui.QFont()
		font.setPointSize(14)
		self.proptype_label.setFont(font)
		self.proptype_label.setObjectName("proptype_label")
		self.ctsno_label = QtWidgets.QLabel(self.centralwidget)
		self.ctsno_label.setGeometry(QtCore.QRect(330, 480, 81, 21))
		font = QtGui.QFont()
		font.setPointSize(14)
		self.ctsno_label.setFont(font)
		self.ctsno_label.setObjectName("ctsno_label")
		self.price_label = QtWidgets.QLabel(self.centralwidget)
		self.price_label.setGeometry(QtCore.QRect(250, 550, 171, 21))
		font = QtGui.QFont()
		font.setPointSize(14)
		self.price_label.setFont(font)
		self.price_label.setObjectName("price_label")
		self.line = QtWidgets.QFrame(self.centralwidget)
		self.line.setGeometry(QtCore.QRect(70, 60, 841, 20))
		self.line.setLineWidth(3)
		self.line.setFrameShape(QtWidgets.QFrame.HLine)
		self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line.setObjectName("line")

		self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
		self.lineEdit.setGeometry(QtCore.QRect(430, 90, 231, 41))
		self.lineEdit.setObjectName("lineEdit")
		self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")

		self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
		self.lineEdit_2.setGeometry(QtCore.QRect(430, 160, 291, 41))
		self.lineEdit_2.setObjectName("lineEdit_2")
		self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")

		self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
		self.lineEdit_3.setGeometry(QtCore.QRect(430, 240, 161, 41))
		self.lineEdit_3.setObjectName("lineEdit_3")
		self.lineEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);")

		self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
		self.lineEdit_4.setGeometry(QtCore.QRect(430, 320, 151, 41))
		self.lineEdit_4.setObjectName("lineEdit_4")
		self.lineEdit_4.setStyleSheet("background-color: rgb(255, 255, 255);")

		self.comboBox = QtWidgets.QComboBox(self.centralwidget)
		self.comboBox.setGeometry(QtCore.QRect(430, 390, 121, 41))
		self.comboBox.setObjectName("comboBox")
		self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
		self.comboBox.addItem("")
		self.comboBox.addItem("")
		self.comboBox.addItem("")
		self.comboBox.addItem("")
		self.comboBox.addItem("")
		self.comboBox.addItem("")
		self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
		self.lineEdit_5.setGeometry(QtCore.QRect(430, 470, 121, 41))
		self.lineEdit_5.setObjectName("lineEdit_5")
		self.lineEdit_5.setStyleSheet("background-color: rgb(255, 255, 255);")

		self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
		self.lineEdit_6.setGeometry(QtCore.QRect(430, 540, 131, 41))
		self.lineEdit_6.setObjectName("lineEdit_6")
		self.lineEdit_6.setStyleSheet("background-color: rgb(255, 255, 255);")

		self.addland_btn = QtWidgets.QPushButton(self.centralwidget)
		self.addland_btn.setGeometry(QtCore.QRect(170, 690, 291, 41))
		font = QtGui.QFont()
		font.setPointSize(14)
		self.addland_btn.setFont(font)
		self.addland_btn.setObjectName("addland_btn")
		self.addland_btn.setStyleSheet("background-color: rgb(255, 255, 255);")

		self.cancel_btn = QtWidgets.QPushButton(self.centralwidget)
		self.cancel_btn.setGeometry(QtCore.QRect(570, 690, 291, 41))
		font = QtGui.QFont()
		font.setPointSize(14)
		self.cancel_btn.setFont(font)
		self.cancel_btn.setObjectName("cancel_btn")
		self.cancel_btn.setStyleSheet("background-color: rgb(255, 255, 255);")
		MainWindow.setCentralWidget(self.centralwidget)
		self.statusbar = QtWidgets.QStatusBar(MainWindow)
		self.statusbar.setObjectName("statusbar")
		MainWindow.setStatusBar(self.statusbar)
		#push buttons
		self.addland_btn.clicked.connect(self.seller)
		self.cancel_btn.clicked.connect(self.openlogin)


		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
		self.sellerreg_label.setText(_translate("MainWindow", "Seller Registration"))
		self.llname_label.setText(_translate("MainWindow", "Landlord Name "))
		self.address_label.setText(_translate("MainWindow", "Address "))
		self.contact_label.setText(_translate("MainWindow", "Contact no"))
		self.location_label.setText(_translate("MainWindow", "Location"))
		self.proptype_label.setText(_translate("MainWindow", "Property Type"))
		self.ctsno_label.setText(_translate("MainWindow", "CTS NO"))
		self.price_label.setText(_translate("MainWindow", "Price Estimation"))
		self.comboBox.setItemText(0, _translate("MainWindow", "1BHK"))
		self.comboBox.setItemText(1, _translate("MainWindow", "2BHK"))
		self.comboBox.setItemText(2, _translate("MainWindow", "3BHK"))
		self.comboBox.setItemText(3, _translate("MainWindow", "1RK"))
		self.comboBox.setItemText(4, _translate("MainWindow", "BUNGALOW"))
		self.comboBox.setItemText(5, _translate("MainWindow", "CHAWL"))
		self.addland_btn.setText(_translate("MainWindow", "Add Landlord"))
		self.cancel_btn.setText(_translate("MainWindow", "Cancel")) 

	def seller(self):
		try:
			db = mdb.connect('localhost', 'root', '', 'pyqt5')

			print('database connected')
			landlord = self.lineEdit.text()
			Address = self.lineEdit_2.text()
			Contact = self.lineEdit_3.text()
			Location = self.lineEdit_4.text()
			CTS = self.lineEdit_5.text()
			Price = self.lineEdit_6.text()
			p_type = self.comboBox.currentText()
			print(type(p_type))
			print(landlord, " ", Address, " ", Contact, " ", Location," ", p_type, " ", CTS, " ", Price)

			print('done')

			cur = db.cursor()
			cur.execute("INSERT INTO seller(landlord, address, contact, location, ptype, cts, price)"
				"VALUES(%s, %s, %s, %s, %s, %s, %s)",[landlord, Address, Contact, Location, p_type, CTS, Price])
		except mdb.Error as e:
			print("error")
			print(e)

	def openlogin(self):
		self.window = QtWidgets.QMainWindow()
		self.ui = ui_login()
		self.ui.setupUi(self.window)
		self.window.show()

def MyConverter(mydata):
		def cvt(mydata):
			try:
				return ast.literal_eval(mydata)

			except Exception:
				return str(mydata)
		return tuple(map(cvt, mydata))

class ui_sellerdata(object):
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
		MainWindow.resize(878, 800)
		MainWindow.setStyleSheet("background-color: rgb(255, 255, 191);")
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
		self.verticalLayout.setObjectName("verticalLayout")
		self.sellerdata_label = QtWidgets.QLabel(self.centralwidget)
		font = QtGui.QFont()
		font.setPointSize(18)
		self.sellerdata_label.setFont(font)
		self.sellerdata_label.setObjectName("sellerdata_label")
		self.verticalLayout.addWidget(self.sellerdata_label)
		self.line = QtWidgets.QFrame(self.centralwidget)
		self.line.setFrameShape(QtWidgets.QFrame.HLine)
		self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line.setObjectName("line")
		self.verticalLayout.addWidget(self.line)
		self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
		self.tableWidget.setRowCount(0)
		self.tableWidget.setColumnCount(7)
		self.tableWidget.setObjectName("tableWidget")
		self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
		item = QtWidgets.QTableWidgetItem()
		self.tableWidget.setHorizontalHeaderItem(0, item)
		item = QtWidgets.QTableWidgetItem()
		self.tableWidget.setHorizontalHeaderItem(1, item)
		item = QtWidgets.QTableWidgetItem()
		self.tableWidget.setHorizontalHeaderItem(2, item)
		item = QtWidgets.QTableWidgetItem()
		self.tableWidget.setHorizontalHeaderItem(3, item)
		item = QtWidgets.QTableWidgetItem()
		self.tableWidget.setHorizontalHeaderItem(4, item)
		item = QtWidgets.QTableWidgetItem()
		self.tableWidget.setHorizontalHeaderItem(5, item)
		item = QtWidgets.QTableWidgetItem()
		self.tableWidget.setHorizontalHeaderItem(6, item)
		self.verticalLayout.addWidget(self.tableWidget)
		self.loaddata_btn = QtWidgets.QPushButton(self.centralwidget)
		self.loaddata_btn.setObjectName("loaddata_btn")
		self.loaddata_btn.setStyleSheet("background-color: rgb(255, 255, 255);")
		self.verticalLayout.addWidget(self.loaddata_btn)
		MainWindow.setCentralWidget(self.centralwidget)
		self.statusbar = QtWidgets.QStatusBar(MainWindow)
		self.statusbar.setObjectName("statusbar")
		MainWindow.setStatusBar(self.statusbar)
		#push button
		self.loaddata_btn.clicked.connect(self.LoadData)

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
		self.sellerdata_label.setText(_translate("MainWindow", "Sellers Data"))
		item = self.tableWidget.horizontalHeaderItem(0)
		item.setText(_translate("MainWindow", "Name"))
		item = self.tableWidget.horizontalHeaderItem(1)
		item.setText(_translate("MainWindow", "Address"))
		item = self.tableWidget.horizontalHeaderItem(2)
		item.setText(_translate("MainWindow", "Contact"))
		item = self.tableWidget.horizontalHeaderItem(3)
		item.setText(_translate("MainWindow", "Location"))
		item = self.tableWidget.horizontalHeaderItem(4)
		item.setText(_translate("MainWindow", "Property Type"))
		item = self.tableWidget.horizontalHeaderItem(5)
		item.setText(_translate("MainWindow", "CTS No"))
		item = self.tableWidget.horizontalHeaderItem(6)
		item.setText(_translate("MainWindow", "Price"))
		self.loaddata_btn.setText(_translate("MainWindow", "Load Data"))

class ui_dealpage(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(980, 800)
		MainWindow.setStyleSheet("background-color: rgb(255, 255, 191);")
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.title_label = QtWidgets.QLabel(self.centralwidget)
		self.title_label.setGeometry(QtCore.QRect(310, 0, 361, 51))
		font = QtGui.QFont()
		font.setPointSize(18)
		self.title_label.setFont(font)
		self.title_label.setObjectName("title_label")
		self.line = QtWidgets.QFrame(self.centralwidget)
		self.line.setGeometry(QtCore.QRect(30, 50, 911, 20))
		self.line.setLineWidth(3)
		self.line.setFrameShape(QtWidgets.QFrame.HLine)
		self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line.setObjectName("line")
		self.buyer_label = QtWidgets.QLabel(self.centralwidget)
		self.buyer_label.setGeometry(QtCore.QRect(90, 120, 131, 31))
		font = QtGui.QFont()
		font.setPointSize(14)
		self.buyer_label.setFont(font)
		self.buyer_label.setObjectName("buyer_label")
		self.seller_label = QtWidgets.QLabel(self.centralwidget)
		self.seller_label.setGeometry(QtCore.QRect(520, 120, 121, 31))
		font = QtGui.QFont()
		font.setPointSize(14)
		self.seller_label.setFont(font)
		self.seller_label.setObjectName("seller_label")
		self.bcontact_label = QtWidgets.QLabel(self.centralwidget)
		self.bcontact_label.setGeometry(QtCore.QRect(70, 200, 151, 31))
		font = QtGui.QFont()
		font.setPointSize(14)
		self.bcontact_label.setFont(font)
		self.bcontact_label.setObjectName("bcontact_label")
		self.scontact_label = QtWidgets.QLabel(self.centralwidget)
		self.scontact_label.setGeometry(QtCore.QRect(500, 200, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(14)
		self.scontact_label.setFont(font)
		self.scontact_label.setObjectName("scontact_label")
		self.addr_label = QtWidgets.QLabel(self.centralwidget)
		self.addr_label.setGeometry(QtCore.QRect(220, 280, 181, 31))
		font = QtGui.QFont()
		font.setPointSize(14)
		self.addr_label.setFont(font)
		self.addr_label.setObjectName("addr_label")
		self.city_label = QtWidgets.QLabel(self.centralwidget)
		self.city_label.setGeometry(QtCore.QRect(340, 350, 61, 31))
		font = QtGui.QFont()
		font.setPointSize(14)
		self.city_label.setFont(font)
		self.city_label.setObjectName("city_label")
		self.val_label = QtWidgets.QLabel(self.centralwidget)
		self.val_label.setGeometry(QtCore.QRect(240, 430, 151, 31))
		font = QtGui.QFont()
		font.setPointSize(14)
		self.val_label.setFont(font)
		self.val_label.setObjectName("val_label")
		self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
		self.lineEdit.setGeometry(QtCore.QRect(230, 110, 221, 41))
		self.lineEdit.setObjectName("lineEdit")
		self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")

		self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
		self.lineEdit_2.setGeometry(QtCore.QRect(660, 110, 221, 41))
		self.lineEdit_2.setObjectName("lineEdit_2")
		self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")

		self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
		self.lineEdit_3.setGeometry(QtCore.QRect(230, 190, 171, 41))
		self.lineEdit_3.setObjectName("lineEdit_3")
		self.lineEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);")

		self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
		self.lineEdit_4.setGeometry(QtCore.QRect(660, 190, 171, 41))
		self.lineEdit_4.setObjectName("lineEdit_4")
		self.lineEdit_4.setStyleSheet("background-color: rgb(255, 255, 255);")

		self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
		self.lineEdit_5.setGeometry(QtCore.QRect(410, 270, 381, 41))
		self.lineEdit_5.setObjectName("lineEdit_5")
		self.lineEdit_5.setStyleSheet("background-color: rgb(255, 255, 255);")

		self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
		self.lineEdit_6.setGeometry(QtCore.QRect(410, 340, 151, 41))
		self.lineEdit_6.setObjectName("lineEdit_6")
		self.lineEdit_6.setStyleSheet("background-color: rgb(255, 255, 255);")

		self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
		self.lineEdit_7.setGeometry(QtCore.QRect(410, 420, 131, 41))
		self.lineEdit_7.setObjectName("lineEdit_7")
		self.lineEdit_7.setStyleSheet("background-color: rgb(255, 255, 255);")

		self.submit_btn = QtWidgets.QPushButton(self.centralwidget)
		self.submit_btn.setGeometry(QtCore.QRect(430, 700, 131, 51))
		self.submit_btn.setObjectName("submit_btn")
		self.submit_btn.setStyleSheet("background-color: rgb(255, 255, 255);")

		self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
		self.lineEdit_8.setGeometry(QtCore.QRect(410, 500, 341, 91))
		self.lineEdit_8.setObjectName("lineEdit_8")
		self.lineEdit_8.setStyleSheet("background-color: rgb(255, 255, 255);")

		self.comment_label = QtWidgets.QLabel(self.centralwidget)
		self.comment_label.setGeometry(QtCore.QRect(280, 510, 111, 31))
		font = QtGui.QFont()
		font.setPointSize(14)
		self.comment_label.setFont(font)
		self.comment_label.setObjectName("comment_label")
		MainWindow.setCentralWidget(self.centralwidget)
		self.statusbar = QtWidgets.QStatusBar(MainWindow)
		self.statusbar.setObjectName("statusbar")
		MainWindow.setStatusBar(self.statusbar)
		#push Button
		self.submit_btn.clicked.connect(self.soldproperty)

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
		self.title_label.setText(_translate("MainWindow", "Purchased Property Details"))
		self.buyer_label.setText(_translate("MainWindow", "Buyer Name"))
		self.seller_label.setText(_translate("MainWindow", "Seller Name"))
		self.bcontact_label.setText(_translate("MainWindow", "Buyer Contact"))
		self.scontact_label.setText(_translate("MainWindow", "Seller Contact"))
		self.addr_label.setText(_translate("MainWindow", "Property Address"))
		self.city_label.setText(_translate("MainWindow", "City"))
		self.val_label.setText(_translate("MainWindow", "Final Valuation "))
		self.submit_btn.setText(_translate("MainWindow", "Submit"))
		self.comment_label.setText(_translate("MainWindow", "Comments"))

	def soldproperty(self):
		try:
			db = mdb.connect('localhost', 'root', '', 'pyqt5')

			print('database connected')
			bname = self.lineEdit.text()
			sname = self.lineEdit_2.text()
			bcontact = self.lineEdit_3.text()
			scontact = self.lineEdit_4.text()
			address = self.lineEdit_5.text()
			city = self.lineEdit_6.text()
			price = self.lineEdit_7.text()
			comments = self.lineEdit_8.text()
			print(bname, " ", sname, " ", bcontact, " ", scontact, " ", address, " ", city, " ", price," ", comments)

			print('done')
			cur = db.cursor()
			cur.execute("INSERT INTO soldproperties(Bname, Sname, Bcontact, Scontact, Propaddress, City, Price, Comments)"
				"VALUES(%s, %s, %s, %s, %s, %s, %s, %s)",[bname, sname, bcontact, scontact, address, city, price, comments ])
		except mdb.Error as e:
			print("error")
			print(e)

def MyConverter(mydata):
        def cvt(mydata):
            try:
                return ast.literal_eval(mydata)

            except Exception:
                return str(mydata)
        return tuple(map(cvt, mydata))


class ui_soldproptable(object):
    def LoadData(self):
        try:
            db = mdb.connect('localhost','root','','pyqt5')

            cur = db.cursor()
            rows = cur.execute("select * from soldproperties")
            soldproperties = cur.fetchall()

            for row in soldproperties:
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
        MainWindow.resize(1000, 800)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 191);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        self.verticalLayout.addWidget(self.tableWidget)
        self.loaddata_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.loaddata_btn.setFont(font)
        self.loaddata_btn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.loaddata_btn.setObjectName("loaddata_btn")
        self.loaddata_btn.clicked.connect(self.LoadData)
        self.verticalLayout.addWidget(self.loaddata_btn)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Sold Properties "))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Buyer Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Seller Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Buyer Contact"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Seller Contact"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Address"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "City"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Final Valuation"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Comments"))
        self.loaddata_btn.setText(_translate("MainWindow", "Load Data"))

if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = ui_login()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())