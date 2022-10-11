# -*- coding: utf-8 -*-
#  
# Development Tool for Editing Mathematical Contents
#
# TODO:
# 1. Download Text Data from AWS DB, e.g. MySQL
# 2. Edit Such Math Text
# 3. Upload the Text to the DB
#
# # Layout, Spacer, Button, Item View, Item Widget, Container, Input Widget, Display Widget [class name]
#


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_devtool(object):
    def setupUi(self, MainWindow_devtool):
        # Main Window [QMainWindow]
        MainWindow_devtool.setObjectName("MainWindow_devtool")
        MainWindow_devtool.resize(913, 893)
        # Central Widget [QWidget]
        self.centralwidget = QtWidgets.QWidget(MainWindow_devtool)
        self.centralwidget.setObjectName("centralwidget")
        # Display Widget [QLabel]
        self.label_db_connect = QtWidgets.QLabel(self.centralwidget)
        self.label_db_connect.setGeometry(QtCore.QRect(30, 20, 111, 21))
        self.label_db_connect.setObjectName("label_db_connect")
        # Display Widget [QLabel]
        self.label_db_choose = QtWidgets.QLabel(self.centralwidget)
        self.label_db_choose.setGeometry(QtCore.QRect(170, 20, 101, 21))
        self.label_db_choose.setObjectName("label_db_choose")
        # Display Widget [QLabel]
        self.pushButton_connect = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_connect.setGeometry(QtCore.QRect(470, 20, 75, 23))
        self.pushButton_connect.setObjectName("pushButton_connect")
        self.pushButton_connect.clicked.connect(self.onClickConnectDB)  # onClickConnetDB method when clicked
        # Display Widget [QLabel]
        self.label_db_select = QtWidgets.QLabel(self.centralwidget)
        self.label_db_select.setGeometry(QtCore.QRect(30, 60, 101, 21))
        self.label_db_select.setObjectName("label_db_select")
        # Display Widget [QLabel]
        self.label_db_text = QtWidgets.QLabel(self.centralwidget)
        self.label_db_text.setGeometry(QtCore.QRect(30, 100, 61, 16))
        self.label_db_text.setObjectName("label_db_text")
        # Input Widget [QPlainTextEdit]
        self.plainTextEdit_pro_sol = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_pro_sol.setGeometry(QtCore.QRect(90, 100, 771, 711))
        self.plainTextEdit_pro_sol.setObjectName("plainTextEdit_pro_sol")
        # Display Widget [QLabel]
        self.label_db_update = QtWidgets.QLabel(self.centralwidget)
        self.label_db_update.setGeometry(QtCore.QRect(30, 830, 131, 21))
        self.label_db_update.setObjectName("label_db_update")
        # Button [QPushButton]
        self.pushButton_store = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_store.setGeometry(QtCore.QRect(170, 830, 75, 23))
        self.pushButton_store.setObjectName("pushButton_store")
        # Central Widget [QWidget]
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(280, 20, 181, 21))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        # Layout [QHBoxLayout]
        self.horizontalLayout_db_choose = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_db_choose.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_db_choose.setObjectName("horizontalLayout_db_choose")
        # Button [QRadioButton]
        self.radioButton_db_01 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton_db_01.setObjectName("radioButton_db_01")
        self.radioButton_db_01.setChecked(True)  # defaulted
        self.horizontalLayout_db_choose.addWidget(self.radioButton_db_01)
        # Button [QRadioButton]
        self.radioButton_db_02 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton_db_02.setObjectName("radioButton_db_02")
        self.horizontalLayout_db_choose.addWidget(self.radioButton_db_02)
        # Central Widget [QWidget]
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(320, 60, 111, 21))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        # Layout [QHBoxLayout]
        self.horizontalLayout_pro_sol = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_pro_sol.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_pro_sol.setObjectName("horizontalLayout_pro_sol")
        # Button [QRadioButton]
        self.radioButton_sol = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        self.radioButton_sol.setObjectName("radioButton_sol")
        self.radioButton_sol.setChecked(True)
        self.horizontalLayout_pro_sol.addWidget(self.radioButton_sol)
        # Button [QRadioButton]
        self.radioButton_pro = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        self.radioButton_pro.setObjectName("radioButton_pro")
        self.horizontalLayout_pro_sol.addWidget(self.radioButton_pro)
        # Input Widget [QLineEdit]
        self.lineEdit_db_pkey = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_db_pkey.setGeometry(QtCore.QRect(240, 60, 61, 21))
        self.lineEdit_db_pkey.setObjectName("lineEdit_db_pkey")
        # Display Widget [QLabel]
        self.label_db_pkey = QtWidgets.QLabel(self.centralwidget)
        self.label_db_pkey.setGeometry(QtCore.QRect(170, 65, 71, 16))
        self.label_db_pkey.setObjectName("label_db_pkey")
        # Button [QPushButton]
        self.pushButton_select = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_select.setGeometry(QtCore.QRect(470, 60, 75, 23))
        self.pushButton_select.setObjectName("pushButton_select")
        # [QMenuBar]
        MainWindow_devtool.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow_devtool)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 913, 21))
        self.menubar.setObjectName("menubar")
        MainWindow_devtool.setMenuBar(self.menubar)
        # [QStatusBar]
        self.statusbar = QtWidgets.QStatusBar(MainWindow_devtool)
        self.statusbar.setObjectName("statusbar")
        MainWindow_devtool.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow_devtool)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_devtool)

    def retranslateUi(self, MainWindow_devtool):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_devtool.setWindowTitle(_translate("MainWindow_devtool", "Lambda Algo Development Tool"))
        self.label_db_connect.setText(_translate("MainWindow_devtool", "데이터베이스 연결"))
        self.label_db_choose.setText(_translate("MainWindow_devtool", "데이터베이스 선택"))
        self.pushButton_connect.setText(_translate("MainWindow_devtool", "연결하기"))
        self.label_db_select.setText(_translate("MainWindow_devtool", "데이터 불러오기"))
        self.label_db_text.setText(_translate("MainWindow_devtool", "편집하기"))
        self.label_db_update.setText(_translate("MainWindow_devtool", "데이터베이스 업데이트"))
        self.pushButton_store.setText(_translate("MainWindow_devtool", "저장하기"))
        self.radioButton_db_01.setText(_translate("MainWindow_devtool", "Lambda-DB"))
        self.radioButton_db_02.setText(_translate("MainWindow_devtool", "Algo-DB"))
        self.radioButton_sol.setText(_translate("MainWindow_devtool", "해설"))
        self.radioButton_pro.setText(_translate("MainWindow_devtool", "문제"))
        self.label_db_pkey.setText(_translate("MainWindow_devtool", "문제 아이디"))
        self.pushButton_select.setText(_translate("MainWindow_devtool", "불러오기"))


    def onClickConnectDB(self):
        print('clicked')



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow_devtool = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_devtool()
    ui.setupUi(MainWindow_devtool)
    MainWindow_devtool.show()
    sys.exit(app.exec_())
