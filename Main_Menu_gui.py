from PyQt6 import QtCore, QtWidgets


class Ui_Main_Window(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(350, 300)
        MainWindow.setMinimumSize(QtCore.QSize(350, 300))
        MainWindow.setMaximumSize(QtCore.QSize(350, 300))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.vote_option_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.vote_option_button.setGeometry(QtCore.QRect(110, 100, 131, 51))
        self.vote_option_button.setObjectName("vote_option_button")
        self.exit_option_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.exit_option_button.setGeometry(QtCore.QRect(110, 170, 131, 51))
        self.exit_option_button.setObjectName("exit_option_button")
        self.welcome_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.welcome_label.setGeometry(QtCore.QRect(100, 40, 161, 41))
        self.welcome_label.setScaledContents(False)
        self.welcome_label.setObjectName("welcome_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Main Menu"))
        self.vote_option_button.setText(_translate("MainWindow", "Vote"))
        self.exit_option_button.setText(_translate("MainWindow", "Exit to Results"))
        self.welcome_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt;\">Welcome, choose an action...</span></p></body></html>"))

