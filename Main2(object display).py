
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import random as rd

Digit_list = [[rd.randint(1, 200), rd.randint(1, 200), rd.randint(1, 200)] for i in range(10)]


class Trapecia:
    def __init__(self, digit):
        self.fudze1 = digit[0]
        self.fudze2 = digit[1]
        self.simagle = digit[2]

    def __str__(self):
        return str(self.fudze1) + " " + str(self.fudze2) + " " + str(self.simagle)

    def fartobi(self):
        return (self.fudze1 + self.fudze2) / 2 * self.simagle

    def __le__(self, other):
        return self.fartobi() <= other.fartobi()

    def __eq__(self, other):
        return self.fartobi() == other.fartobi()


class Martkutxedi(Trapecia):
    def __init__(self, digit):
        super().__init__(digit)
        self.simagle = None

    def __str__(self):
        return str(self.fudze1) + " " + str(self.fudze2)

    def fartobi(self):
        return self.fudze1 * self.fudze2


class Kvadrati(Martkutxedi):
    def __init__(self, digit):
        super().__init__(digit)
        self.fudze2 = None

    def __str__(self):
        return str(self.fudze1)

    def fartobi(self):
        return self.fudze1 ** 2


trapecia1 = Trapecia(Digit_list[0])
trapecia2 = Trapecia(Digit_list[1])
print(trapecia1)
print(trapecia2)
print(trapecia1.fartobi())
print(trapecia2.fartobi())
print(trapecia1 <= trapecia2)
print(trapecia1 == trapecia2)
martx1 = Martkutxedi(Digit_list[0])
print(martx1)
kvad1 = Kvadrati(Digit_list[0])
print(kvad1)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ShapeMenu = QtWidgets.QComboBox(self.centralwidget)
        self.ShapeMenu.setGeometry(QtCore.QRect(40, 100, 191, 41))
        self.ShapeMenu.setObjectName("ShapeMenu")
        self.ShapeMenu.addItem("")
        self.ShapeMenu.addItem("")
        self.ShapeMenu.addItem("")
        self.ImageDisplay = QtWidgets.QLabel(self.centralwidget)
        self.ImageDisplay.setGeometry(QtCore.QRect(380, 60, 271, 251))
        self.ImageDisplay.setText("")
        self.ImageDisplay.setScaledContents(True)
        self.ImageDisplay.setObjectName("ImageDisplay")
        self.CalculateAreaButton = QtWidgets.QPushButton(self.centralwidget)
        self.CalculateAreaButton.setGeometry(QtCore.QRect(50, 410, 121, 41))
        self.CalculateAreaButton.setObjectName("CalculateAreaButton")
        self.AreaDisplay = QtWidgets.QLabel(self.centralwidget)
        self.AreaDisplay.setGeometry(QtCore.QRect(310, 410, 371, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.AreaDisplay.setFont(font)
        self.AreaDisplay.setObjectName("AreaDisplay")
        self.selectButton = QtWidgets.QPushButton(self.centralwidget)
        self.selectButton.setGeometry(QtCore.QRect(80, 180, 101, 31))
        self.selectButton.setObjectName("selectButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.selectButton.clicked.connect(self.pressed)
        self.CalculateAreaButton.clicked.connect(self.area)

        self.CalculateAreaButton.clicked.connect(self.showpopup)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ShapeMenu.setItemText(0, _translate("MainWindow", "Trapezoid"))
        self.ShapeMenu.setItemText(1, _translate("MainWindow", "Square"))
        self.ShapeMenu.setItemText(2, _translate("MainWindow", "Rectangle"))
        self.CalculateAreaButton.setText(_translate("MainWindow", "Calculate Area!"))
        self.AreaDisplay.setText(_translate("MainWindow", "Area of the selected shape is:"))
        self.selectButton.setText(_translate("MainWindow", "Select"))

    def pressed(self):
        if self.ShapeMenu.currentText() == "Trapezoid":
            self.ImageDisplay.setPixmap(QtGui.QPixmap("Shapes\Trapezoid.png"))
        if self.ShapeMenu.currentText() == "Square":
            self.ImageDisplay.setPixmap(QtGui.QPixmap("Shapes\Square.png"))
        if self.ShapeMenu.currentText() == "Rectangle":
            self.ImageDisplay.setPixmap(QtGui.QPixmap("Shapes\Rectangle.png"))

    def area(self):
        if self.ShapeMenu.currentText() == "Trapezoid":
            self.AreaDisplay.setText("Area of the selected shaepe is: " + str(trapecia1.fartobi()))
        if self.ShapeMenu.currentText() == "Square":
            self.AreaDisplay.setText("Area of the selected shaepe is: " + str(martx1.fartobi()))
        if self.ShapeMenu.currentText() == "Rectangle":
            self.AreaDisplay.setText("Area of the selected shaepe is: " + str(kvad1.fartobi()))

    def showpopup(self):
        msg = QMessageBox()
        msg.setWindowTitle("Options")
        msg.setText("Select an option!")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Cancel | QMessageBox.Retry | QMessageBox.Ignore | QMessageBox.Cancel)
        msg.setDefaultButton(QMessageBox.Retry)
        # msg.setInformativeText("-")
        # msg.setDetailedText("Details")
        x = msg.exec_()

    # def close1(self):
        # self.window2 = QtWidgets.QMainWindow()
        # self.ui = Ui_fo


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
