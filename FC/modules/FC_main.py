# -*- coding: utf-8 -*-

import sys

import PyQt5
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic

CalUI = '../_uiFiles/calculator.ui'

class MainDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self, None)
        uic.loadUi(CalUI, self)

        self.num_pushButton_1.clicked.connect(lambda state, button = self.num_pushButton_1 : self.NumClicked(state, button))
        self.num_pushButton_2.clicked.connect(lambda state, button = self.num_pushButton_2 : self.NumClicked(state, button))
        self.num_pushButton_3.clicked.connect(lambda state, button = self.num_pushButton_3 : self.NumClicked(state, button))
        self.num_pushButton_4.clicked.connect(lambda state, button = self.num_pushButton_4 : self.NumClicked(state, button))
        self.num_pushButton_5.clicked.connect(lambda state, button = self.num_pushButton_5 : self.NumClicked(state, button))
        self.num_pushButton_6.clicked.connect(lambda state, button = self.num_pushButton_6 : self.NumClicked(state, button))
        self.num_pushButton_7.clicked.connect(lambda state, button = self.num_pushButton_7 : self.NumClicked(state, button))
        self.num_pushButton_8.clicked.connect(lambda state, button = self.num_pushButton_8 : self.NumClicked(state, button))
        self.num_pushButton_9.clicked.connect(lambda state, button = self.num_pushButton_9 : self.NumClicked(state, button))
        self.num_pushButton_10.clicked.connect(lambda state, button = self.num_pushButton_10 : self.NumClicked(state, button))

        self.sign_pushButton_1.clicked.connect(lambda state, button = self.sign_pushButton_1 : self.NumClicked(state, button))
        self.sign_pushButton_2.clicked.connect(lambda state, button = self.sign_pushButton_2 : self.NumClicked(state, button))
        self.sign_pushButton_3.clicked.connect(lambda state, button = self.sign_pushButton_3 : self.NumClicked(state, button))
        self.sign_pushButton_4.clicked.connect(lambda state, button = self.sign_pushButton_4 : self.NumClicked(state, button))

        self.result_pushButton.clicked.connect(self.MakeResult)
        self.reset_pushButton.clicked.connect(self.Reset)
        self.del_pushButton.clicked.connect(self.Delete)

    def NumClicked(self, state, button):
        exist_line_text = self.q_lineEdit.text()
        now_num_text = button.text()
        self.q_lineEdit.setText(exist_line_text + now_num_text)

    def MakeResult(self):
        try:
            result = eval(self.q_lineEdit.text())
            self.a_lineEdit.setText(str(result))
        except Exception as e:
            print(e)
            # pass

    def Reset(self):
        self.q_lineEdit.clear()
        #self.q_lineEdit.setText('0')
        self.a_lineEdit.clear()
        #self.a_lineEdit.setText('0')

    def Delete(self):
        exist_line_text = self.q_lineEdit.text()
        exist_line_text = exist_line_text[:-1] # 문자열 가장 마지막 문자를 없앤다
        self.q_lineEdit.setText(exist_line_text)

app = QApplication(sys.argv)
main_dialog = MainDialog()
main_dialog.show()
app.exec_()