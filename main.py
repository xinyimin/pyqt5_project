#coding = 'utf-8'

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import loginui_ui

 
#demo
def buttonClicked(girl):
    girl.textBrowser.append("hello world! This is my first pyQt5 program.")
 
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    MainWindow.shadow = QtWidgets.QGraphicsDropShadowEffect(MainWindow)
    MainWindow.shadow.setBlurRadius(15)
    MainWindow.shadow.setXOffset(10)
    MainWindow.shadow.setYOffset(10)
    MainWindow.shadow.setColor(QtGui.QColor(0, 0, 0, 110))
    MainWindow.setGraphicsEffect(MainWindow.shadow)
    MainWindow.setWindowFlag(QtCore.Qt.FramelessWindowHint)
    MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
    ui = loginui_ui.Ui_LoginWindow()
    ui.setupUi(MainWindow)
    ui.pushButton.clicked.connect(lambda:buttonClicked(ui))
    ui.pushButton_Register.clicked.connect(lambda:ui.stackedWidget_2.setCurrentIndex(0))
    ui.pushButton_Login.clicked.connect(lambda:ui.stackedWidget_2.setCurrentIndex(1))
                                           
    MainWindow.show()
    sys.exit(app.exec_())