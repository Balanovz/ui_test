from PyQt5.QtWidgets import QMainWindow, QPushButton
from PyQt5.QtCore import pyqtSlot
from PyQt5 import uic


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("/home/user/Документы/testForKirill/lastTest.ui", self)
        self.setup_btn = self.findChild(QPushButton, "pushButton")
        self.setup_btn2 = self.findChild(QPushButton, "pushButton_4")
        self.dac_btn = self.findChild(QPushButton, "pushButton_2")
        self.mb_btn = self.findChild(QPushButton, "pushButton_5")
        self.key_btn = self.findChild(QPushButton, "pushButton_3")


        self.dac_btn.clicked.connect(self.change_dac)

        self.mb_btn.clicked.connect(self.change_mb)
        self.key_btn.clicked.connect(self.change_key)

    def change_dac(self):
        if self.dac_btn.isChecked():
            self.dac_btn.setStyleSheet(
                """
                #pushButton_2
                {
                    qproperty-icon: url(/home/user/Документы/testForKirill/icons/green_circle.svg);
                    border: 1.5px solid black;
                    border-radius: 10px;
                    background-color: rgb(222, 235, 255);
                    qproperty-iconSize: 20px 20px;
                }
                #pushButton_2:hover
                {
                     border: 3px solid black;
                }
                """
            )
        else:
            self.dac_btn.setStyleSheet(
                """
                #pushButton_2
                {
                    qproperty-icon: url(/home/user/Документы/testForKirill/icons/red_circle.svg);
                    border: 1.5px solid black;
                    border-radius: 10px;
                    background-color: rgb(222, 235, 255);
                    qproperty-iconSize: 20px 20px;
                }
                #pushButton_2:hover
                {
                     border: 3px solid black;
                }
                """
            )

    def change_mb(self):
        if self.mb_btn.isChecked():
            self.mb_btn.setStyleSheet(
                """
                #pushButton_5
                {
                    qproperty-icon: url(/home/user/Документы/testForKirill/icons/green_circle.svg);
                    border: 1.5px solid black;
                    border-radius: 10px;
                    background-color: rgb(222, 235, 255);
                    qproperty-iconSize: 20px 20px;
                }
                #pushButton_5:hover
                {
                     border: 3px solid black;
                }
                """
            )
        else:
            self.mb_btn.setStyleSheet(
                """
                #pushButton_5
                {
                    qproperty-icon: url(/home/user/Документы/testForKirill/icons/red_circle.svg);
                    border: 1.5px solid black;
                    border-radius: 10px;
                    background-color: rgb(222, 235, 255);
                    qproperty-iconSize: 20px 20px;
                }
                #pushButton_5:hover
                {
                     border: 3px solid black;
                }
                """
            )

    def change_key(self):
        if self.key_btn.isChecked():
            self.key_btn.setStyleSheet(
                """
                #pushButton_3
                {
                    border: 1.5px solid black;
                    border-radius: 10px;
                    background-color: rgb(204, 255, 204);
                }

                #pushButton_3:hover
                {
                    border: 3px solid black;
                }
                """
            )
        else:
            self.key_btn.setStyleSheet(
                """
                #pushButton_3
                {
                    border: 1.5px solid black;
                    border-radius: 10px;
                    background-color: rgb(255, 204, 204);
                }

                #pushButton_3:hover
                {
                    border: 3px solid black;
                }
                """
            )
