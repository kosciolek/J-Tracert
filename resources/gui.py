# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Z:\git\J-Tracert\resources\gui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(900, 600))
        MainWindow.setMaximumSize(QtCore.QSize(900, 600))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei Light")
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setWindowTitle("J-Tracert")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/apps.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 150, 311, 161))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.listWidget.setFont(font)
        self.listWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.listWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.listWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.listWidget.setDragEnabled(False)
        self.listWidget.setObjectName("listWidget")
        self.mapImg = QtWidgets.QLabel(self.centralwidget)
        self.mapImg.setGeometry(QtCore.QRect(340, 70, 541, 511))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mapImg.sizePolicy().hasHeightForWidth())
        self.mapImg.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.mapImg.setFont(font)
        self.mapImg.setStyleSheet("")
        self.mapImg.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.mapImg.setFrameShadow(QtWidgets.QFrame.Plain)
        self.mapImg.setLineWidth(1)
        self.mapImg.setText("")
        self.mapImg.setPixmap(QtGui.QPixmap(":/map.png"))
        self.mapImg.setAlignment(QtCore.Qt.AlignCenter)
        self.mapImg.setObjectName("mapImg")
        self.ipInput = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.ipInput.setGeometry(QtCore.QRect(10, 10, 161, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ipInput.sizePolicy().hasHeightForWidth())
        self.ipInput.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei Light")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.ipInput.setFont(font)
        self.ipInput.setAutoFillBackground(False)
        self.ipInput.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.ipInput.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.ipInput.setLineWidth(1)
        self.ipInput.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.ipInput.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.ipInput.setTabStopWidth(80)
        self.ipInput.setCursorWidth(2)
        self.ipInput.setBackgroundVisible(False)
        self.ipInput.setCenterOnScroll(True)
        self.ipInput.setObjectName("ipInput")
        self.publicAddrLabel = QtWidgets.QLabel(self.centralwidget)
        self.publicAddrLabel.setGeometry(QtCore.QRect(10, 50, 311, 51))
        self.publicAddrLabel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.publicAddrLabel.setObjectName("publicAddrLabel")
        self.traceButton = QtWidgets.QPushButton(self.centralwidget)
        self.traceButton.setGeometry(QtCore.QRect(180, 10, 141, 31))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.traceButton.setFont(font)
        self.traceButton.setObjectName("traceButton")
        self.timeoutsNumber = QtWidgets.QLabel(self.centralwidget)
        self.timeoutsNumber.setGeometry(QtCore.QRect(10, 110, 151, 31))
        self.timeoutsNumber.setObjectName("timeoutsNumber")
        self.notice = QtWidgets.QLabel(self.centralwidget)
        self.notice.setGeometry(QtCore.QRect(340, 15, 451, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.notice.setFont(font)
        self.notice.setObjectName("notice")
        self.infoText = QtWidgets.QLabel(self.centralwidget)
        self.infoText.setGeometry(QtCore.QRect(10, 330, 311, 251))
        self.infoText.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.infoText.setObjectName("infoText")
        self.processingLabel = QtWidgets.QLabel(self.centralwidget)
        self.processingLabel.setGeometry(QtCore.QRect(0, 0, 901, 601))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei Light")
        self.processingLabel.setFont(font)
        self.processingLabel.setStyleSheet("background-color:rgba(255, 255, 255, 1)")
        self.processingLabel.setObjectName("processingLabel")
        self.hopsNumber = QtWidgets.QLabel(self.centralwidget)
        self.hopsNumber.setGeometry(QtCore.QRect(190, 110, 111, 31))
        self.hopsNumber.setObjectName("hopsNumber")
        self.notice_2 = QtWidgets.QLabel(self.centralwidget)
        self.notice_2.setGeometry(QtCore.QRect(610, 10, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.notice_2.setFont(font)
        self.notice_2.setObjectName("notice_2")
        self.listWidget.raise_()
        self.mapImg.raise_()
        self.ipInput.raise_()
        self.publicAddrLabel.raise_()
        self.traceButton.raise_()
        self.timeoutsNumber.raise_()
        self.notice.raise_()
        self.infoText.raise_()
        self.hopsNumber.raise_()
        self.notice_2.raise_()
        self.processingLabel.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.ipInput, self.traceButton)
        MainWindow.setTabOrder(self.traceButton, self.listWidget)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.ipInput.setPlaceholderText(_translate("MainWindow", "8.8.8.8 | google.com"))
        self.publicAddrLabel.setText(_translate("MainWindow", "Public IPv4:"))
        self.traceButton.setText(_translate("MainWindow", "Trace!"))
        self.timeoutsNumber.setText(_translate("MainWindow", "Tracert timeouts: --"))
        self.notice.setText(_translate("MainWindow", "Downloading data might take a while."))
        self.infoText.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#b9b9b9;\">Hop Data</span></p></body></html>"))
        self.processingLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:17pt; font-weight:600; color:#7e7e7e;\">Processing</span></p><p align=\"center\"><br/></p><p align=\"center\"><span style=\" color:#7e7e7e;\">The application is downloading data.</span></p><p align=\"center\"><span style=\" color:#7e7e7e;\">This might take a while.</span></p></body></html>"))
        self.hopsNumber.setText(_translate("MainWindow", "Hops: --"))
        self.notice_2.setText(_translate("MainWindow", "Status:"))

import resource_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
