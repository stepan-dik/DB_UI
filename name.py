# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Inserting_gui.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(558, 459)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.lab_start_phone = QtWidgets.QLabel(self.centralWidget)
        self.lab_start_phone.setGeometry(QtCore.QRect(30, 220, 21, 31))
        self.lab_start_phone.setObjectName("lab_start_phone")
        self.textf_name = QtWidgets.QPlainTextEdit(self.centralWidget)
        self.textf_name.setGeometry(QtCore.QRect(20, 160, 221, 31))
        self.textf_name.setObjectName("textf_name")
        self.dateEdit = QtWidgets.QDateEdit(self.centralWidget)
        self.dateEdit.setGeometry(QtCore.QRect(20, 280, 110, 32))
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.dateEdit.setCalendarPopup(True)
        self.lab_stuff = QtWidgets.QLabel(self.centralWidget)
        self.lab_stuff.setGeometry(QtCore.QRect(290, 70, 131, 31))
        self.lab_stuff.setObjectName("lab_stuff")
        self.lab_phone = QtWidgets.QLabel(self.centralWidget)
        self.lab_phone.setGeometry(QtCore.QRect(30, 190, 131, 31))
        self.lab_phone.setObjectName("lab_phone")
        self.lab_product_name = QtWidgets.QLabel(self.centralWidget)
        self.lab_product_name.setGeometry(QtCore.QRect(30, 70, 131, 31))
        self.lab_product_name.setObjectName("lab_product_name")
        self.lab_date = QtWidgets.QLabel(self.centralWidget)
        self.lab_date.setGeometry(QtCore.QRect(30, 250, 131, 31))
        self.lab_date.setObjectName("lab_date")
        self.button_proceed = QtWidgets.QPushButton(self.centralWidget)
        self.button_proceed.setGeometry(QtCore.QRect(20, 340, 141, 34))
        self.button_proceed.setObjectName("button_proceed")
        self.textf_product_name = QtWidgets.QPlainTextEdit(self.centralWidget)
        self.textf_product_name.setGeometry(QtCore.QRect(20, 100, 221, 31))
        self.textf_product_name.setObjectName("textf_product_name")
        self.textf_stuff = QtWidgets.QPlainTextEdit(self.centralWidget)
        self.textf_stuff.setGeometry(QtCore.QRect(280, 100, 261, 151))
        self.textf_stuff.setObjectName("textf_stuff")
        self.lab_receiver = QtWidgets.QLabel(self.centralWidget)
        self.lab_receiver.setGeometry(QtCore.QRect(290, 250, 131, 31))
        self.lab_receiver.setObjectName("lab_receiver")
        self.button_search = QtWidgets.QPushButton(self.centralWidget)
        self.button_search.setGeometry(QtCore.QRect(20, 20, 231, 34))
        self.button_search.setObjectName("button_search")
        self.lab_name = QtWidgets.QLabel(self.centralWidget)
        self.lab_name.setGeometry(QtCore.QRect(30, 130, 131, 31))
        self.lab_name.setObjectName("lab_name")
        self.textf_phone = QtWidgets.QPlainTextEdit(self.centralWidget)
        self.textf_phone.setGeometry(QtCore.QRect(50, 220, 191, 31))
        self.textf_phone.setObjectName("textf_phone")
        self.cBox_receiver = QtWidgets.QComboBox(self.centralWidget)
        self.cBox_receiver.setGeometry(QtCore.QRect(280, 280, 161, 32))
        self.cBox_receiver.setMaxVisibleItems(3)
        self.cBox_receiver.setObjectName("cBox_receiver")
        self.cBox_receiver.addItem("")
        self.cBox_receiver.addItem("")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # self.center()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lab_start_phone.setText(_translate("MainWindow", "+7"))
        self.lab_stuff.setText(_translate("MainWindow", "Примечания"))
        self.lab_phone.setText(_translate("MainWindow", "Телефон"))
        self.lab_product_name.setText(_translate("MainWindow", "Название изделия"))
        self.lab_date.setText(_translate("MainWindow", "Дата"))
        self.button_proceed.setText(_translate("MainWindow", "Принять в ремонт"))
        self.lab_receiver.setText(_translate("MainWindow", "Принял"))
        self.button_search.setText(_translate("MainWindow", "Поиск по принятым изделиям"))
        self.lab_name.setText(_translate("MainWindow", "ФИО"))
        self.cBox_receiver.setItemText(0, _translate("MainWindow", "Дик А.И."))
        self.cBox_receiver.setItemText(1, _translate("MainWindow", "Бруй В.И."))

