# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(770, 624)
        MainWindow.setStyleSheet("background: rgb(93, 64, 255);\n"
"color:rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.delete_btn = QtWidgets.QPushButton(self.centralwidget)
        self.delete_btn.setGeometry(QtCore.QRect(20, 60, 75, 23))
        self.delete_btn.setStyleSheet("background:rgb(255, 186, 65);\n"
"border: 2px colid white")
        self.delete_btn.setObjectName("delete_btn")
        self.text_edit = QtWidgets.QTextEdit(self.centralwidget)
        self.text_edit.setGeometry(QtCore.QRect(220, 60, 501, 471))
        self.text_edit.setStyleSheet("background:rgb(255, 186, 65);")
        self.text_edit.setObjectName("text_edit")
        self.title_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.title_edit.setGeometry(QtCore.QRect(220, 20, 491, 20))
        self.title_edit.setObjectName("title_edit")
        self.save_btn = QtWidgets.QPushButton(self.centralwidget)
        self.save_btn.setGeometry(QtCore.QRect(20, 30, 75, 21))
        self.save_btn.setObjectName("save_btn")
        self.del_tag_btn = QtWidgets.QPushButton(self.centralwidget)
        self.del_tag_btn.setGeometry(QtCore.QRect(100, 460, 81, 23))
        self.del_tag_btn.setStyleSheet("background:rgb(255, 186, 65);")
        self.del_tag_btn.setObjectName("del_tag_btn")
        self.search_btn = QtWidgets.QPushButton(self.centralwidget)
        self.search_btn.setGeometry(QtCore.QRect(130, 500, 75, 23))
        self.search_btn.setObjectName("search_btn")
        self.add_tag_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_tag_btn.setGeometry(QtCore.QRect(10, 460, 75, 23))
        self.add_tag_btn.setObjectName("add_tag_btn")
        self.tag_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.tag_edit.setGeometry(QtCore.QRect(10, 500, 113, 20))
        self.tag_edit.setObjectName("tag_edit")
        self.create_btn = QtWidgets.QPushButton(self.centralwidget)
        self.create_btn.setGeometry(QtCore.QRect(20, 0, 75, 23))
        self.create_btn.setStyleSheet("background:rgb(255, 186, 65);")
        self.create_btn.setObjectName("create_btn")
        self.notes_list = QtWidgets.QListWidget(self.centralwidget)
        self.notes_list.setGeometry(QtCore.QRect(10, 110, 161, 192))
        self.notes_list.setStyleSheet("background:rgb(255, 186, 65);")
        self.notes_list.setObjectName("notes_list")
        self.tag_list = QtWidgets.QListWidget(self.centralwidget)
        self.tag_list.setGeometry(QtCore.QRect(10, 320, 161, 121))
        self.tag_list.setStyleSheet("background:rgb(255, 186, 65);\n"
"")
        self.tag_list.setObjectName("tag_list")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 770, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "замітки"))
        self.delete_btn.setText(_translate("MainWindow", "видалити"))
        self.save_btn.setText(_translate("MainWindow", "зберегти"))
        self.del_tag_btn.setText(_translate("MainWindow", "Видалити тег"))
        self.search_btn.setText(_translate("MainWindow", "Пошук"))
        self.add_tag_btn.setText(_translate("MainWindow", "Додати тег"))
        self.create_btn.setText(_translate("MainWindow", "Нова замітка"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
